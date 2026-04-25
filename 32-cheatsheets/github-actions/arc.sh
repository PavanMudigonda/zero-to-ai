#!/bin/bash
set -e  # Exit immediately if any command fails

# ========================================
# GitHub Actions Runner Controller (ARC)
# Setup Script - Based on Official Quickstart
# ========================================
#
# USAGE:
#
# Option 1: Personal Access Token (for testing/development)
#   GITHUB_PAT='ghp_xxxxx' ./arc.sh
#
# Option 2: GitHub App (RECOMMENDED for production)
#   GITHUB_APP_ID='123456' \
#   GITHUB_APP_INSTALLATION_ID='987654' \
#   GITHUB_APP_PRIVATE_KEY=$'-----BEGIN RSA PRIVATE KEY-----\nMIIE...\n-----END RSA PRIVATE KEY-----' \
#   ./arc.sh
#
# ========================================
#
# WHAT IS ARC?
# Actions Runner Controller (ARC) is a Kubernetes operator that orchestrates 
# self-hosted GitHub Actions runners in your cluster. It provides:
#   - Auto-scaling based on workflow demand
#   - Ephemeral runners (created/destroyed per job for security)
#   - Enterprise-grade runner management at scale
#
# ARCHITECTURE:
# ARC uses a two-tier architecture:
#   1. Controller: Watches GitHub for workflow jobs, manages runner lifecycle
#   2. Runner Scale Sets: Groups of runners that scale based on demand
#
# WHY USE ARC?
# - Cost savings (runners scale down to zero when idle)
# - Better security (ephemeral runners prevent secret leakage)
# - Simplified management vs manually maintaining runner VMs
# - Native Kubernetes integration (use existing cluster resources)
#
# INTERVIEW TOPICS:
# - Kubernetes Operators and Custom Resource Definitions (CRDs)
# - Auto-scaling patterns in Kubernetes
# - GitHub Actions architecture and webhook-based scaling
# - Security best practices (namespace isolation, secret management)
# - Authentication: GitHub Apps vs Personal Access Tokens
# ========================================

# Configuration Variables
CONTROLLER_NAMESPACE="arc-systems"    # Namespace for ARC controller pods
RUNNER_NAMESPACE="arc-runners"        # Namespace for ephemeral runner pods (SEPARATE for security)
INSTALLATION_NAME="arc-runner-set"    # Name used in workflow "runs-on:" field
GITHUB_CONFIG_URL="https://github.com/PavanMudigondaTR/gh-arc-demo"  # Repo/Org/Enterprise URL

# ========================================
# AUTHENTICATION METHODS
# ========================================
# ARC supports two authentication methods:
#
# 1. PERSONAL ACCESS TOKEN (PAT) - Simple but less secure
#    - Set GITHUB_PAT environment variable
#    - Required scopes: repo, admin:org (or admin:enterprise)
#    - Issues: Tied to user account, no audit trail, expiration management
#
# 2. GITHUB APP (RECOMMENDED for production) - More secure and scalable
#    - Set GITHUB_APP_ID, GITHUB_APP_INSTALLATION_ID, GITHUB_APP_PRIVATE_KEY
#    - Benefits:
#      * Not tied to individual user (survives employee changes)
#      * Fine-grained permissions
#      * Better audit trail (actions attributed to app, not user)
#      * Higher rate limits
#      * Can be scoped to specific repos/orgs
#
# INTERVIEW NOTE: Always prefer GitHub Apps over PATs in production!
# PATs are acceptable for:
#   - Local development/testing
#   - Personal projects
#   - Quick prototypes
#
# GitHub Apps are required for:
#   - Production environments
#   - Enterprise deployments
#   - Multi-team setups
#   - Compliance/audit requirements
# ========================================

GITHUB_PAT="${GITHUB_PAT:-}"                              # Personal Access Token (Option 1)
GITHUB_APP_ID="${GITHUB_APP_ID:-}"                        # GitHub App ID (Option 2)
GITHUB_APP_INSTALLATION_ID="${GITHUB_APP_INSTALLATION_ID:-}"  # App Installation ID (Option 2)
GITHUB_APP_PRIVATE_KEY="${GITHUB_APP_PRIVATE_KEY:-}"      # App Private Key (Option 2)

# WHY SEPARATE NAMESPACES?
# Security best practice: Controller needs cluster-wide permissions to manage runners,
# but runners themselves should be isolated. If a runner is compromised during a 
# malicious workflow, it can't access the controller or other sensitive resources.

# Detect authentication method
AUTH_METHOD=""
if [ -n "$GITHUB_APP_ID" ] && [ -n "$GITHUB_APP_INSTALLATION_ID" ] && [ -n "$GITHUB_APP_PRIVATE_KEY" ]; then
  AUTH_METHOD="github_app"
  echo "✓ Using GitHub App authentication (recommended for production)"
elif [ -n "$GITHUB_PAT" ]; then
  AUTH_METHOD="pat"
  echo "✓ Using Personal Access Token authentication"
else
  echo "Error: No authentication method configured!"
  echo ""
  echo "Option 1: Personal Access Token (Simple, for testing)"
  echo "  GITHUB_PAT='your-token' ./arc.sh"
  echo "  Required scopes: repo, admin:org"
  echo ""
  echo "Option 2: GitHub App (Recommended for production)"
  echo "  GITHUB_APP_ID='123456' \\"
  echo "  GITHUB_APP_INSTALLATION_ID='987654' \\"
  echo "  GITHUB_APP_PRIVATE_KEY=\$'-----BEGIN RSA PRIVATE KEY-----\n...\n-----END RSA PRIVATE KEY-----' \\"
  echo "  ./arc.sh"
  echo ""
  echo "HOW TO CREATE A GITHUB APP:"
  echo "  1. Go to GitHub Settings → Developer settings → GitHub Apps → New GitHub App"
  echo "  2. Set Homepage URL (any valid URL)"
  echo "  3. Uncheck 'Webhook → Active'"
  echo "  4. Set Repository permissions:"
  echo "     - Actions: Read and write"
  echo "     - Administration: Read and write"
  echo "     - Checks: Read"
  echo "     - Metadata: Read"
  echo "  5. Set Organization permissions (if org-level runners):"
  echo "     - Self-hosted runners: Read and write"
  echo "  6. Click 'Create GitHub App'"
  echo "  7. Note the App ID"
  echo "  8. Generate and download private key"
  echo "  9. Install app to your org/repo and note Installation ID"
  echo "     (Installation ID is in URL: /settings/installations/<ID>)"
  echo ""
  exit 1
fi

echo "Starting ARC installation..."

# ========================================
# Step 0: Environment Check
# ========================================
# MINIKUBE-SPECIFIC ISSUE:
# Minikube's Docker daemon may have TLS certificate verification issues
# when pulling from ghcr.io (GitHub Container Registry).
# 
# INTERVIEW NOTE: Be aware of environment-specific challenges:
#   - Local dev (minikube/kind) vs Cloud (AKS/EKS/GKE)
#   - Private registry authentication
#   - Network policies and egress rules
#   - Image pull secrets for private registries
if kubectl config current-context 2>/dev/null | grep -q "minikube"; then
  echo ""
  echo "🔍 Minikube detected - Ensuring proper configuration..."
  echo ""
  echo "If you encounter ImagePullBackOff errors, run these commands:"
  echo "  minikube delete"
  echo "  minikube start --insecure-registry='10.0.0.0/8,ghcr.io'"
  echo ""
  sleep 2
fi

# ========================================
# Step 1: Install ARC Controller
# ========================================
# WHAT THIS DOES:
# Deploys the ARC controller using Helm, which installs:
#   - Deployment: Controller pod that watches GitHub API
#   - ServiceAccount: Identity for the controller
#   - RBAC: ClusterRole/ClusterRoleBinding for permissions
#   - CRDs: Custom resource definitions (AutoScalingRunnerSet, etc.)
#
# WHY HELM?
# Helm is a package manager for Kubernetes that:
#   - Templating for reusable configs
#   - Versioning and rollback capabilities
#   - Dependency management
#   - Values.yaml for customization
#
# OCI REGISTRY:
# oci://ghcr.io means Helm chart stored as OCI artifact (like Docker images)
# Modern approach vs traditional Helm repository URLs
#
# INTERVIEW TOPICS:
# - Helm chart structure (Chart.yaml, values.yaml, templates/)
# - Helm upgrade --install (idempotent operation)
# - OCI registries vs traditional Helm repos
# - Kubernetes operators and reconciliation loops
echo ""
echo "Step 1: Installing ARC controller in namespace: ${CONTROLLER_NAMESPACE}"
helm upgrade --install arc \
    --namespace "${CONTROLLER_NAMESPACE}" \
    --create-namespace \
    oci://ghcr.io/actions/actions-runner-controller-charts/gha-runner-scale-set-controller

# Wait for controller to be ready
# INTERVIEW NOTE: kubectl wait is better than sleep loops
# Uses Kubernetes watch API for efficient polling
# Condition types: Ready, Initialized, ContainersReady, PodScheduled
echo "Waiting for controller to be ready..."
sleep 10  # Brief delay for pod creation
kubectl wait --for=condition=ready pod \
    --all \
    -n "${CONTROLLER_NAMESPACE}" \
    --timeout=60s || echo "Note: Controller may still be initializing, continuing..."

# ========================================
# Step 2: Configure Runner Scale Set
# ========================================
# WHAT IS A SCALE SET?
# A logical group of runners that:
#   - Share the same configuration (container image, resources, labels)
#   - Scale independently based on workflow demand
#   - Are ephemeral (destroyed after each job)
#
# HOW SCALING WORKS:
# 1. GitHub webhook notifies ARC of new workflow jobs
# 2. Controller creates listener pod (long-lived, watches for jobs)
# 3. Listener receives job assignments from GitHub
# 4. Controller spins up ephemeral runner pods
# 5. Runner executes job, reports back to GitHub
# 6. Runner pod is deleted after job completes
#
# GITHUBCONFIGURL:
# Determines scope of runners:
#   - Repository: https://github.com/owner/repo
#   - Organization: https://github.com/org-name
#   - Enterprise: https://github.com/enterprises/enterprise-name
#
# AUTHENTICATION:
# githubConfigSecret creates a Kubernetes Secret with credentials.
# The controller uses this to:
#   - Register/unregister runners
#   - Poll for workflow jobs (or receive webhook events)
#   - Report runner status
#
# PAT Authentication:
#   --set githubConfigSecret.github_token="..."
#
# GitHub App Authentication (more secure):
#   --set githubConfigSecret.github_app_id="..."
#   --set githubConfigSecret.github_app_installation_id="..."
#   --set githubConfigSecret.github_app_private_key="..."
#
# INTERVIEW TOPICS:
# - Kubernetes Secrets vs ConfigMaps (when to use each)
# - Webhook vs polling architectures
# - Horizontal Pod Autoscaler (HPA) vs custom scaling (ARC uses custom)
# - StatefulSet vs Deployment (runners use neither - custom resources)
# - OAuth Apps vs GitHub Apps (Apps have better security model)
echo ""
echo "Step 2: Installing runner scale set in namespace: ${RUNNER_NAMESPACE}"
echo "Configuration URL: ${GITHUB_CONFIG_URL}"
echo "Installation name (use this in workflows): ${INSTALLATION_NAME}"
echo "Authentication method: ${AUTH_METHOD}"

# Build Helm command based on auth method
if [ "$AUTH_METHOD" == "github_app" ]; then
  # GitHub App authentication (RECOMMENDED)
  helm upgrade --install "${INSTALLATION_NAME}" \
      --namespace "${RUNNER_NAMESPACE}" \
      --create-namespace \
      --set githubConfigUrl="${GITHUB_CONFIG_URL}" \
      --set githubConfigSecret.github_app_id="${GITHUB_APP_ID}" \
      --set githubConfigSecret.github_app_installation_id="${GITHUB_APP_INSTALLATION_ID}" \
      --set githubConfigSecret.github_app_private_key="${GITHUB_APP_PRIVATE_KEY}" \
      oci://ghcr.io/actions/actions-runner-controller-charts/gha-runner-scale-set
else
  # PAT authentication (simple but less secure)
  helm upgrade --install "${INSTALLATION_NAME}" \
      --namespace "${RUNNER_NAMESPACE}" \
      --create-namespace \
      --set githubConfigUrl="${GITHUB_CONFIG_URL}" \
      --set githubConfigSecret.github_token="${GITHUB_PAT}" \
      oci://ghcr.io/actions/actions-runner-controller-charts/gha-runner-scale-set
fi

# WHAT GETS CREATED:
# - AutoScalingRunnerSet CR: Defines desired runner configuration
# - Listener Deployment: Long-lived pod that watches for jobs
# - Ephemeral Runner Set: Configuration for temporary runner pods
# - Secret: Contains authentication credentials (PAT or GitHub App key)
#
# GITHUB APP vs PAT COMPARISON:
#
# | Feature              | PAT                      | GitHub App                |
# |---------------------|--------------------------|---------------------------|
# | Tied to user        | Yes (problem!)           | No (survives user changes)|
# | Rate limits         | 5,000 req/hour           | 15,000 req/hour           |
# | Permissions         | Broad scopes             | Fine-grained              |
# | Audit trail         | Attributed to user       | Attributed to app         |
# | Expiration          | Manual renewal           | Keys don't expire         |
# | Multi-org support   | Need PAT per org         | One app, multiple orgs    |
# | Best for            | Testing, personal use    | Production, enterprise    |
#
# INTERVIEW SCENARIO:
# "An employee who created the PAT left the company. What happens?"
# Answer: PAT stops working, all runners go offline. With GitHub App,
# the app exists independently of any user, so runners keep working.

# ========================================
# Step 3: Verify Installation
# ========================================
# VERIFICATION CHECKLIST:
# ✓ Helm releases deployed successfully
# ✓ Controller pod is Running (handles runner lifecycle)
# ✓ Listener pod is Running (watches for workflow jobs)
#
# TROUBLESHOOTING COMMANDS:
# kubectl describe pod <pod-name> -n <namespace>  # Shows events and state
# kubectl logs <pod-name> -n <namespace>          # Shows container logs
# kubectl get events -n <namespace>               # Shows recent events
# helm status <release-name> -n <namespace>       # Shows release details
#
# INTERVIEW NOTE: 
# Understand Kubernetes pod lifecycle:
#   Pending → ImagePullBackOff/ErrImagePull (image issues)
#   Pending → CrashLoopBackOff (app crashes on start)
#   Running → Ready (health checks passed)
echo ""
echo "Step 3: Verifying installation..."
echo ""
echo "Helm releases:"
helm list -A  # -A shows all namespaces

echo ""
echo "Controller pods (should show Running):"
kubectl get pods -n "${CONTROLLER_NAMESPACE}"

echo ""
echo "Listener pod (should show Running):"
kubectl get pods -n "${RUNNER_NAMESPACE}"

# ========================================
# Success Message
# ========================================
# WORKFLOW INTEGRATION:
# The 'runs-on' field in your workflow MUST match the INSTALLATION_NAME
# Example:
#   runs-on: arc-runner-set  # Matches our INSTALLATION_NAME variable
#
# JOB EXECUTION FLOW:
# 1. Workflow triggered (push/PR/manual/schedule)
# 2. GitHub evaluates 'runs-on' and routes to ARC
# 3. Listener receives job assignment
# 4. Controller creates ephemeral runner pod
# 5. Runner downloads repo, executes steps
# 6. Results sent to GitHub, pod deleted
#
# MONITORING IN PRODUCTION:
# - kubectl get pods -n arc-runners -w  # Watch runner pods
# - Metrics: Prometheus + Grafana
# - Logging: Fluent Bit → CloudWatch/Elasticsearch
# - Alerting: Alert on pod failures, scaling issues
echo ""
echo "========================================="
echo "✅ ARC Installation Complete!"
echo "========================================="
echo ""
echo "Next steps:"
echo "1. Use 'runs-on: ${INSTALLATION_NAME}' in your workflow files"
echo "2. Trigger a workflow to test the setup"
echo "3. Monitor runner pods: kubectl get pods -n ${RUNNER_NAMESPACE} -w"
echo ""
echo "Example workflow:"
cat <<'EOF'
name: Test ARC
on: workflow_dispatch
jobs:
  test:
    runs-on: arc-runner-set  # This must match INSTALLATION_NAME
    steps:
      - run: echo "🎉 Running on ARC!"
EOF
echo ""

# ========================================
# Optional: Organization/Enterprise Setup
# ========================================
# SCOPE LEVELS EXPLAINED:
#
# 1. REPOSITORY LEVEL (what we use above):
#    GITHUB_CONFIG_URL="https://github.com/owner/repo"
#    - Runners only available to single repo
#    - PAT needs: repo scope
#    - Use case: Dedicated resources per project
#
# 2. ORGANIZATION LEVEL:
#    GITHUB_CONFIG_URL="https://github.com/YOUR_ORG"
#    - Runners shared across all repos in org
#    - PAT needs: repo + admin:org scopes
#    - Use case: Shared runner pool for teams
#    - Can use runner groups for access control
#
# 3. ENTERPRISE LEVEL:
#    GITHUB_CONFIG_URL="https://github.com/enterprises/YOUR_ENTERPRISE"
#    - Runners shared across all orgs in enterprise
#    - PAT needs: repo + admin:enterprise scopes
#    - Use case: Central platform team managing runners
#    - Highest level of control and governance
#
# RUNNER GROUPS (Org/Enterprise only):
# Additional Helm values to assign to specific teams:
#   --set runnerGroup="backend-team"
# Allows restricting which repos can use which runners
#
# INTERVIEW TOPICS:
# - Multi-tenancy in Kubernetes (namespaces, RBAC, resource quotas)
# - GitHub permissions model (repo/org/enterprise hierarchy)
# - Cost allocation and chargeback models
# - Capacity planning for shared runner pools
#
# Uncomment and modify to install org/enterprise level runners:
#
# For Organization:
# GITHUB_CONFIG_URL="https://github.com/YOUR_ORG"
# 
# For Enterprise:
# GITHUB_CONFIG_URL="https://github.com/enterprises/YOUR_ENTERPRISE"

# ========================================
# ADDITIONAL INTERVIEW PREP NOTES
# ========================================
#
# KEY CONCEPTS TO UNDERSTAND:
#
# 1. KUBERNETES OPERATORS:
#    - Custom controllers that extend Kubernetes API
#    - Watch for CR changes, reconcile desired vs actual state
#    - Control loop: observe → diff → act → repeat
#
# 2. CUSTOM RESOURCES (CRs):
#    - AutoScalingRunnerSet: Defines runner configuration
#    - EphemeralRunnerSet: Manages temporary runner pods
#    - EphemeralRunner: Represents individual runner pod
#
# 3. EPHEMERAL RUNNERS:
#    - Fresh pod for each job (no state carried over)
#    - Security: Prevents secret leakage between jobs
#    - Isolation: Each job has clean environment
#
# 4. SCALING STRATEGIES:
#    - Pull-based: Listener polls GitHub for jobs
#    - Webhook-based: GitHub sends events (deprecated in ARC v2)
#    - Metrics: Can scale based on queue depth
#
# 5. ALTERNATIVES TO ARC:
#    - GitHub-hosted runners (simpler, more expensive)
#    - VM-based self-hosted runners (harder to manage)
#    - Other tools: Jenkins, GitLab Runner, CircleCI
#
# 6. PRODUCTION CONSIDERATIONS:
#    - Resource limits/requests on runner pods
#    - Node selectors/tolerations for dedicated nodes
#    - Network policies for security
#    - Image pull secrets for private registries
#    - Monitoring and alerting
#    - Backup/DR for runner configurations
#    - Cost optimization (spot instances, autoscaling)
#
# 7. AUTHENTICATION DEEP DIVE:
#    
#    GITHUB APP SETUP (Production):
#    a) Create app: GitHub Settings → Developer settings → GitHub Apps
#    b) Configure permissions:
#       - Repository: Actions (read/write), Administration (read/write), Metadata (read)
#       - Organization: Self-hosted runners (read/write)
#    c) Generate private key (RSA, keep secure!)
#    d) Install app to org/repo
#    e) Get App ID and Installation ID
#    f) Store private key in secret manager (NOT in git)
#    
#    PAT SETUP (Development/Testing only):
#    a) GitHub Settings → Developer settings → Personal access tokens
#    b) Select scopes: repo, admin:org (or admin:enterprise)
#    c) Set expiration (max 1 year)
#    d) Store in environment variable or secret manager
#    
#    CREDENTIAL ROTATION:
#    - GitHub App: Generate new private key, update secret, delete old key
#    - PAT: Generate new token, update secret, revoke old token
#    - Automate rotation with tools like:
#      * External Secrets Operator (sync from Vault/AWS Secrets Manager)
#      * Sealed Secrets (GitOps-friendly encrypted secrets)
#      * SOPS (Secrets OPerationS, encrypt in git)
#
# COMMON INTERVIEW QUESTIONS:
#
# Q: Why use ARC instead of GitHub-hosted runners?
# A: Cost (runs in your cluster), compliance (data stays in your network),
#    customization (install any tools), and performance (faster for large repos).
#
# Q: How does ARC handle scaling?
# A: Listener pod receives job assignments from GitHub, controller creates
#    ephemeral runner pods on-demand, pods deleted after job completes.
#
# Q: What happens if controller pod crashes?
# A: Running jobs continue, but new jobs won't scale. Kubernetes will restart
#    the pod. Use multiple replicas + PodDisruptionBudget for HA.
#
# Q: How do you secure runner pods?
# A: Namespace isolation, RBAC, NetworkPolicies, PodSecurityPolicies/Standards,
#    ephemeral pods (no persistence), secret management via external systems.
#
# Q: How would you monitor ARC in production?
# A: Metrics (pod count, job duration), logs (centralized logging), alerts
#    (pod failures, scaling issues), distributed tracing for workflow execution.
#
# Q: Why use GitHub App instead of PAT for authentication?
# A: GitHub Apps are not tied to user accounts (survive employee changes),
#    have higher rate limits (15k vs 5k req/hour), provide better audit trails,
#    offer fine-grained permissions, and support multiple organizations with
#    a single app. PATs are only suitable for development/testing.
#
# Q: How do you handle credential rotation for runners?
# A: For GitHub Apps: generate new private key, update Kubernetes secret,
#    restart listener pods, delete old key. Automate with External Secrets
#    Operator to sync from Vault/AWS Secrets Manager. For PATs: generate
#    new token before expiration, update secret, revoke old token.
#
# Q: What's the difference between GitHub App ID and Installation ID?
# A: App ID identifies the GitHub App itself (static, same across all installs).
#    Installation ID identifies a specific installation of that app to an
#    org/repo (unique per installation). You need both for authentication.
