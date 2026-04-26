# Helm Cheatsheet - Lead DevOps Architect Interview Prep

## Table of Contents
1. [Helm Basics](#helm-basics)
2. [Charts](#charts)
3. [Repositories](#repositories)
4. [Releases](#releases)
5. [Values & Configuration](#values--configuration)
6. [Chart Development](#chart-development)
7. [Templates](#templates)
8. [Hooks](#hooks)
9. [Dependencies](#dependencies)
10. [Interview Scenarios](#interview-scenarios)

---

## Helm Basics

### 1. Installation
```bash
# macOS
brew install helm

# Linux
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash

# Verify
helm version
```

### 2. Initialize Helm
```bash
# Add default repository
helm repo add stable https://charts.helm.sh/stable
helm repo add bitnami https://charts.bitnami.com/bitnami

# Update repositories
helm repo update

# List repositories
helm repo list

# Search charts
helm search repo nginx
helm search hub wordpress
```

---

## Charts

### 3. Install Charts
```bash
# Install chart
helm install my-release bitnami/nginx

# Install with custom name
helm install web-server bitnami/nginx

# Install in specific namespace
helm install my-release bitnami/nginx --namespace production --create-namespace

# Dry run
helm install my-release bitnami/nginx --dry-run --debug

# Generate manifest without installing
helm template my-release bitnami/nginx > manifest.yaml
```

### 4. List & Inspect Charts
```bash
# List installed releases
helm list
helm list --all-namespaces
helm list -n production

# Get release details
helm get all my-release
helm get values my-release
helm get manifest my-release
helm get notes my-release

# Show chart info
helm show chart bitnami/nginx
helm show values bitnami/nginx
helm show all bitnami/nginx
```

---

## Repositories

### 5. Manage Repositories
```bash
# Add repository
helm repo add gitlab https://charts.gitlab.io/

# Update repositories
helm repo update

# Remove repository
helm repo remove stable

# Search repository
helm search repo nginx
helm search repo nginx --versions

# Search Helm Hub
helm search hub prometheus
```

### 6. Create Local Repository
```bash
# Package chart
helm package ./mychart

# Create repository index
helm repo index . --url https://charts.example.com

# Serve local repository
helm serve
```

---

## Releases

### 7. Upgrade Releases
```bash
# Upgrade release
helm upgrade my-release bitnami/nginx

# Upgrade with new values
helm upgrade my-release bitnami/nginx --set service.type=LoadBalancer

# Upgrade from file
helm upgrade my-release bitnami/nginx -f values.yaml

# Force upgrade
helm upgrade my-release bitnami/nginx --force

# Upgrade with atomic rollback
helm upgrade my-release bitnami/nginx --atomic

# Install or upgrade
helm upgrade my-release bitnami/nginx --install
```

### 8. Rollback Releases
```bash
# Rollback to previous version
helm rollback my-release

# Rollback to specific revision
helm rollback my-release 2

# View revision history
helm history my-release

# Get specific revision
helm get values my-release --revision 2
```

### 9. Uninstall Releases
```bash
# Uninstall release
helm uninstall my-release

# Uninstall and keep history
helm uninstall my-release --keep-history

# Uninstall with namespace
helm uninstall my-release -n production
```

---

## Values & Configuration

### 10. Override Values
```bash
# Set individual values
helm install my-release bitnami/nginx --set service.type=LoadBalancer

# Set multiple values
helm install my-release bitnami/nginx \
  --set service.type=LoadBalancer \
  --set replicaCount=3

# Use values file
helm install my-release bitnami/nginx -f custom-values.yaml

# Multiple values files (last wins)
helm install my-release bitnami/nginx -f base-values.yaml -f prod-values.yaml

# Set array values
helm install my-release bitnami/nginx --set ingress.hosts[0]=example.com

# Set nested values
helm install my-release bitnami/nginx --set resources.limits.cpu=200m
```

### 11. Values File Examples
```yaml
# custom-values.yaml
replicaCount: 3

image:
  repository: nginx
  tag: "1.21"
  pullPolicy: IfNotPresent

service:
  type: LoadBalancer
  port: 80

resources:
  limits:
    cpu: 200m
    memory: 256Mi
  requests:
    cpu: 100m
    memory: 128Mi

ingress:
  enabled: true
  className: nginx
  hosts:
    - host: example.com
      paths:
        - path: /
          pathType: Prefix

autoscaling:
  enabled: true
  minReplicas: 2
  maxReplicas: 10
  targetCPUUtilizationPercentage: 80
```

---

## Chart Development

### 12. Create Chart
```bash
# Create new chart
helm create mychart

# Chart structure:
mychart/
├── Chart.yaml          # Chart metadata
├── values.yaml         # Default values
├── charts/             # Chart dependencies
├── templates/          # Kubernetes manifests
│   ├── NOTES.txt       # Post-install notes
│   ├── _helpers.tpl    # Template helpers
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── ingress.yaml
│   └── tests/
└── .helmignore         # Files to ignore
```

### 13. Chart.yaml
```yaml
apiVersion: v2
name: mychart
description: A Helm chart for Kubernetes
type: application
version: 1.0.0
appVersion: "1.16.0"

keywords:
  - nginx
  - web
  - http

maintainers:
  - name: DevOps Team
    email: devops@example.com

sources:
  - https://github.com/example/mychart

dependencies:
  - name: redis
    version: "17.0.0"
    repository: https://charts.bitnami.com/bitnami
    condition: redis.enabled
```

### 14. Lint & Package
```bash
# Lint chart
helm lint ./mychart

# Package chart
helm package ./mychart

# Sign package
helm package --sign --key 'keyname' --keyring path/to/keyring.secret ./mychart

# Verify package
helm verify mychart-1.0.0.tgz
```

---

## Templates

### 15. Template Syntax
```yaml
# templates/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ include "mychart.fullname" . }}
  labels:
    {{- include "mychart.labels" . | nindent 4 }}
spec:
  replicas: {{ .Values.replicaCount }}
  selector:
    matchLabels:
      {{- include "mychart.selectorLabels" . | nindent 6 }}
  template:
    metadata:
      labels:
        {{- include "mychart.selectorLabels" . | nindent 8 }}
    spec:
      containers:
      - name: {{ .Chart.Name }}
        image: "{{ .Values.image.repository }}:{{ .Values.image.tag | default .Chart.AppVersion }}"
        imagePullPolicy: {{ .Values.image.pullPolicy }}
        ports:
        - name: http
          containerPort: {{ .Values.service.port }}
          protocol: TCP
        {{- if .Values.resources }}
        resources:
          {{- toYaml .Values.resources | nindent 10 }}
        {{- end }}
```

### 16. Template Functions
```yaml
# _helpers.tpl
{{/* Generate full name */}}
{{- define "mychart.fullname" -}}
{{- printf "%s-%s" .Release.Name .Chart.Name | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/* Common labels */}}
{{- define "mychart.labels" -}}
helm.sh/chart: {{ .Chart.Name }}-{{ .Chart.Version }}
app.kubernetes.io/name: {{ include "mychart.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}

# Usage in templates
{{- include "mychart.labels" . | nindent 4 }}

# Built-in functions
{{ .Values.name | upper }}
{{ .Values.name | lower }}
{{ .Values.name | quote }}
{{ .Values.name | default "default-value" }}
{{ .Values.list | toYaml | nindent 2 }}
{{ .Values.dict | toJson }}
{{ required "A valid .Values.name is required!" .Values.name }}

# Conditionals
{{- if .Values.ingress.enabled }}
# ingress config
{{- end }}

{{- if and .Values.enabled (eq .Values.type "production") }}
# production config
{{- end }}

# Loops
{{- range .Values.hosts }}
- host: {{ . }}
{{- end }}
```

### 17. Test Templates
```bash
# Render templates locally
helm template my-release ./mychart

# Debug rendering
helm install my-release ./mychart --dry-run --debug

# Show specific template
helm template my-release ./mychart -s templates/deployment.yaml
```

---

## Hooks

### 18. Hook Types
```yaml
# templates/pre-install-job.yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: {{ include "mychart.fullname" . }}-pre-install
  annotations:
    "helm.sh/hook": pre-install
    "helm.sh/hook-weight": "-5"
    "helm.sh/hook-delete-policy": hook-succeeded
spec:
  template:
    spec:
      containers:
      - name: pre-install
        image: busybox
        command: ['sh', '-c', 'echo Pre-install hook']
      restartPolicy: Never

# Hook annotations:
# "helm.sh/hook": pre-install, post-install, pre-delete, post-delete, pre-upgrade, post-upgrade, pre-rollback, post-rollback, test
# "helm.sh/hook-weight": "-5" (lower runs first)
# "helm.sh/hook-delete-policy": before-hook-creation, hook-succeeded, hook-failed
```

### 19. Test Hooks
```yaml
# templates/tests/test-connection.yaml
apiVersion: v1
kind: Pod
metadata:
  name: "{{ include "mychart.fullname" . }}-test"
  annotations:
    "helm.sh/hook": test
spec:
  containers:
    - name: wget
      image: busybox
      command: ['wget']
      args: ['{{ include "mychart.fullname" . }}:{{ .Values.service.port }}']
  restartPolicy: Never
```

```bash
# Run tests
helm test my-release

# Show test logs
helm test my-release --logs
```

---

## Dependencies

### 20. Manage Dependencies
```yaml
# Chart.yaml
dependencies:
  - name: redis
    version: "17.0.0"
    repository: https://charts.bitnami.com/bitnami
    condition: redis.enabled
  
  - name: postgresql
    version: "12.0.0"
    repository: https://charts.bitnami.com/bitnami
    condition: postgresql.enabled

# values.yaml
redis:
  enabled: true
  auth:
    password: mypassword

postgresql:
  enabled: false
```

```bash
# Update dependencies
helm dependency update ./mychart

# List dependencies
helm dependency list ./mychart

# Build dependencies
helm dependency build ./mychart
```

---

## Interview Scenarios

### Scenario 1: Deploy Multi-Tier Application
```yaml
# Chart.yaml
apiVersion: v2
name: webapp
description: Web application with database
version: 1.0.0
dependencies:
  - name: postgresql
    version: "12.0.0"
    repository: https://charts.bitnami.com/bitnami
  - name: redis
    version: "17.0.0"
    repository: https://charts.bitnami.com/bitnami

# values.yaml
app:
  replicaCount: 3
  image:
    repository: myapp
    tag: "1.0.0"

postgresql:
  auth:
    password: dbpassword
    database: myappdb

redis:
  auth:
    password: redispassword

# Install
helm dependency update ./webapp
helm install my-webapp ./webapp \
  --set app.replicaCount=5 \
  --set postgresql.auth.password=SecurePass123
```

### Scenario 2: Blue-Green Deployment
```bash
# Deploy blue version
helm install blue-app ./mychart \
  --set image.tag=v1.0 \
  --set service.selector.version=blue

# Deploy green version
helm install green-app ./mychart \
  --set image.tag=v2.0 \
  --set service.selector.version=green

# Switch traffic (update ingress)
helm upgrade production-ingress ./ingress-chart \
  --set backend.version=green

# Remove old version
helm uninstall blue-app
```

### Scenario 3: Canary Deployment
```yaml
# values-canary.yaml
replicaCount: 1
image:
  tag: "v2.0"
service:
  labels:
    version: canary
weight: 10  # 10% traffic

# values-stable.yaml
replicaCount: 9
image:
  tag: "v1.0"
service:
  labels:
    version: stable
weight: 90  # 90% traffic

# Install both
helm install stable ./mychart -f values-stable.yaml
helm install canary ./mychart -f values-canary.yaml

# Gradually increase canary traffic
helm upgrade canary ./mychart -f values-canary.yaml --set replicaCount=5,weight=50
helm upgrade stable ./mychart -f values-stable.yaml --set replicaCount=5,weight=50

# Full cutover
helm upgrade stable ./mychart -f values-canary.yaml
helm uninstall canary
```

### Scenario 4: Secrets Management
```yaml
# Use with sealed-secrets
apiVersion: bitnami.com/v1alpha1
kind: SealedSecret
metadata:
  name: {{ include "mychart.fullname" . }}-secret
spec:
  encryptedData:
    password: AgBX7...encrypted...

# Or use external secrets operator
apiVersion: external-secrets.io/v1beta1
kind: ExternalSecret
metadata:
  name: {{ include "mychart.fullname" . }}
spec:
  secretStoreRef:
    name: aws-secretsmanager
  target:
    name: app-secret
  data:
    - secretKey: password
      remoteRef:
        key: /prod/db/password
```

---

## Quick Reference

```bash
# Common workflows
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update
helm search repo nginx
helm install my-nginx bitnami/nginx
helm list
helm upgrade my-nginx bitnami/nginx
helm rollback my-nginx
helm uninstall my-nginx

# Development
helm create mychart
helm lint mychart
helm template my-release mychart
helm install my-release mychart --dry-run --debug
helm package mychart
helm test my-release

# Debugging
helm get values my-release
helm get manifest my-release
helm history my-release
helm diff upgrade my-release ./mychart -f values.yaml
```

---

**Prepared for**: Lead DevOps Architect Interview  
**Last Updated**: February 15, 2026  
**Total Commands**: 70+ Helm operations
