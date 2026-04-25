# Google Cloud Platform (GCP) & gcloud CLI Cheatsheet

## Table of Contents
1. [gcloud CLI Basics](#gcloud-cli-basics)
2. [Authentication & Configuration](#authentication--configuration)
3. [Compute Engine (VMs)](#compute-engine-vms)
4. [Cloud Storage (GCS)](#cloud-storage-gcs)
5. [Google Kubernetes Engine (GKE)](#google-kubernetes-engine-gke)
6. [Cloud Functions](#cloud-functions)
7. [Cloud Run](#cloud-run)
8. [Cloud SQL](#cloud-sql)
9. [IAM & Security](#iam--security)
10. [Networking (VPC)](#networking-vpc)
11. [Load Balancing](#load-balancing)
12. [Container Registry & Artifact Registry](#container-registry--artifact-registry)
13. [Cloud Build](#cloud-build)
14. [App Engine](#app-engine)
15. [BigQuery](#bigquery)
16. [Pub/Sub](#pubsub)
17. [Cloud Monitoring & Logging](#cloud-monitoring--logging)
18. [Secret Manager](#secret-manager)
19. [Cloud DNS](#cloud-dns)
20. [Resource Management](#resource-management)

---

## gcloud CLI Basics

### 1. Installation & Version
```bash
# Install gcloud CLI (macOS)
brew install --cask google-cloud-sdk

# Install gcloud CLI (Linux)
curl https://sdk.cloud.google.com | bash
exec -l $SHELL

# Install gcloud CLI (Windows)
# Download from: https://cloud.google.com/sdk/docs/install

# Check version
gcloud version

# Update gcloud CLI
gcloud components update

# Install additional components
gcloud components install kubectl
gcloud components install alpha
gcloud components install beta

# List installed components
gcloud components list

# Remove component
gcloud components remove COMPONENT_ID
```

### 2. Help & Documentation
```bash
# General help
gcloud help

# Command-specific help
gcloud compute instances help
gcloud compute instances create --help

# List all gcloud commands
gcloud meta list-commands

# Interactive mode
gcloud interactive

# Format output as JSON
gcloud compute instances list --format=json

# Format output as YAML
gcloud compute instances list --format=yaml

# Format output as table
gcloud compute instances list --format="table(name,zone,status)"

# Filter results
gcloud compute instances list --filter="zone:us-central1-a"

# Limit results
gcloud compute instances list --limit=10
```

---

## Authentication & Configuration

### 3. Authentication
```bash
# Login to gcloud
gcloud auth login

# Login with service account
gcloud auth activate-service-account --key-file=KEY_FILE.json

# Application default credentials (for local development)
gcloud auth application-default login

# Revoke credentials
gcloud auth revoke ACCOUNT

# List authenticated accounts
gcloud auth list

# Set active account
gcloud config set account ACCOUNT
```

### 4. Configuration Management
```bash
# Initialize gcloud configuration
gcloud init

# List configurations
gcloud config configurations list

# Create new configuration
gcloud config configurations create CONFIG_NAME

# Activate configuration
gcloud config configurations activate CONFIG_NAME

# Delete configuration
gcloud config configurations delete CONFIG_NAME

# Set project
gcloud config set project PROJECT_ID

# Set default region
gcloud config set compute/region us-central1

# Set default zone
gcloud config set compute/zone us-central1-a

# Get configuration value
gcloud config get-value project
gcloud config get-value compute/region

# List all configuration properties
gcloud config list

# Unset property
gcloud config unset compute/zone
```

### 5. Projects
```bash
# List projects
gcloud projects list

# Describe project
gcloud projects describe PROJECT_ID

# Create project
gcloud projects create PROJECT_ID --name="Project Name"

# Delete project
gcloud projects delete PROJECT_ID

# Set active project
gcloud config set project PROJECT_ID

# Get current project
gcloud config get-value project

# Add IAM policy binding to project
gcloud projects add-iam-policy-binding PROJECT_ID \
  --member="user:email@example.com" \
  --role="roles/editor"
```

---

## Compute Engine (VMs)

### 6. Instance Management
```bash
# List instances
gcloud compute instances list
gcloud compute instances list --filter="zone:us-central1-a"

# Create instance
gcloud compute instances create INSTANCE_NAME \
  --zone=us-central1-a \
  --machine-type=e2-medium \
  --image-family=ubuntu-2004-lts \
  --image-project=ubuntu-os-cloud \
  --boot-disk-size=20GB \
  --boot-disk-type=pd-standard \
  --tags=web-server,ssh

# Create instance with startup script
gcloud compute instances create INSTANCE_NAME \
  --zone=us-central1-a \
  --machine-type=e2-medium \
  --metadata-from-file=startup-script=startup.sh

# Create instance with custom network
gcloud compute instances create INSTANCE_NAME \
  --zone=us-central1-a \
  --machine-type=e2-medium \
  --network=custom-vpc \
  --subnet=custom-subnet \
  --no-address  # No external IP

# Create preemptible instance
gcloud compute instances create INSTANCE_NAME \
  --zone=us-central1-a \
  --preemptible

# Start instance
gcloud compute instances start INSTANCE_NAME --zone=us-central1-a

# Stop instance
gcloud compute instances stop INSTANCE_NAME --zone=us-central1-a

# Restart instance
gcloud compute instances reset INSTANCE_NAME --zone=us-central1-a

# Delete instance
gcloud compute instances delete INSTANCE_NAME --zone=us-central1-a

# Describe instance
gcloud compute instances describe INSTANCE_NAME --zone=us-central1-a
```

### 7. SSH & Remote Access
```bash
# SSH into instance
gcloud compute ssh INSTANCE_NAME --zone=us-central1-a

# SSH with specific user
gcloud compute ssh USER@INSTANCE_NAME --zone=us-central1-a

# SCP file to instance
gcloud compute scp LOCAL_FILE INSTANCE_NAME:REMOTE_PATH --zone=us-central1-a

# SCP file from instance
gcloud compute scp INSTANCE_NAME:REMOTE_FILE LOCAL_PATH --zone=us-central1-a

# SCP directory recursively
gcloud compute scp --recurse LOCAL_DIR INSTANCE_NAME:REMOTE_PATH --zone=us-central1-a

# Execute command on instance
gcloud compute ssh INSTANCE_NAME --zone=us-central1-a --command="ls -la"
```

### 8. Machine Types & Images
```bash
# List machine types
gcloud compute machine-types list --filter="zone:us-central1-a"

# List images
gcloud compute images list
gcloud compute images list --project=ubuntu-os-cloud

# List image families
gcloud compute images list --filter="family:ubuntu-2004-lts"

# Create custom image from disk
gcloud compute images create IMAGE_NAME --source-disk=DISK_NAME --source-disk-zone=us-central1-a

# Delete image
gcloud compute images delete IMAGE_NAME

# Describe image
gcloud compute images describe IMAGE_NAME
```

### 9. Disks
```bash
# List disks
gcloud compute disks list

# Create disk
gcloud compute disks create DISK_NAME \
  --size=100GB \
  --type=pd-standard \
  --zone=us-central1-a

# Create SSD disk
gcloud compute disks create DISK_NAME \
  --size=100GB \
  --type=pd-ssd \
  --zone=us-central1-a

# Attach disk to instance
gcloud compute instances attach-disk INSTANCE_NAME \
  --disk=DISK_NAME \
  --zone=us-central1-a

# Detach disk from instance
gcloud compute instances detach-disk INSTANCE_NAME \
  --disk=DISK_NAME \
  --zone=us-central1-a

# Delete disk
gcloud compute disks delete DISK_NAME --zone=us-central1-a

# Create snapshot
gcloud compute disks snapshot DISK_NAME \
  --snapshot-names=SNAPSHOT_NAME \
  --zone=us-central1-a

# List snapshots
gcloud compute snapshots list

# Delete snapshot
gcloud compute snapshots delete SNAPSHOT_NAME
```

### 10. Instance Templates & Groups
```bash
# Create instance template
gcloud compute instance-templates create TEMPLATE_NAME \
  --machine-type=e2-medium \
  --image-family=ubuntu-2004-lts \
  --image-project=ubuntu-os-cloud \
  --boot-disk-size=20GB \
  --tags=web-server

# List instance templates
gcloud compute instance-templates list

# Delete instance template
gcloud compute instance-templates delete TEMPLATE_NAME

# Create managed instance group
gcloud compute instance-groups managed create GROUP_NAME \
  --template=TEMPLATE_NAME \
  --size=3 \
  --zone=us-central1-a

# Set autoscaling
gcloud compute instance-groups managed set-autoscaling GROUP_NAME \
  --zone=us-central1-a \
  --min-num-replicas=2 \
  --max-num-replicas=10 \
  --target-cpu-utilization=0.75

# Update instances in group
gcloud compute instance-groups managed rolling-action start-update GROUP_NAME \
  --version=template=NEW_TEMPLATE \
  --zone=us-central1-a

# List instance groups
gcloud compute instance-groups managed list

# Delete instance group
gcloud compute instance-groups managed delete GROUP_NAME --zone=us-central1-a
```

---

## Cloud Storage (GCS)

### 11. Bucket Management
```bash
# List buckets
gsutil ls

# Create bucket
gsutil mb gs://BUCKET_NAME
gsutil mb -l us-central1 gs://BUCKET_NAME  # Specific location
gsutil mb -c STANDARD gs://BUCKET_NAME     # Storage class

# Delete bucket
gsutil rb gs://BUCKET_NAME
gsutil rb -r gs://BUCKET_NAME  # Remove all objects first

# Bucket info
gsutil ls -L -b gs://BUCKET_NAME

# Set bucket storage class
gsutil defstorageclass set NEARLINE gs://BUCKET_NAME

# Enable versioning
gsutil versioning set on gs://BUCKET_NAME

# Lifecycle configuration
gsutil lifecycle set lifecycle.json gs://BUCKET_NAME
```

### 12. Object Operations
```bash
# List objects in bucket
gsutil ls gs://BUCKET_NAME
gsutil ls -r gs://BUCKET_NAME  # Recursive
gsutil ls -l gs://BUCKET_NAME  # Long format with size

# Upload file
gsutil cp FILE.txt gs://BUCKET_NAME/
gsutil cp -r DIR gs://BUCKET_NAME/  # Upload directory

# Download file
gsutil cp gs://BUCKET_NAME/FILE.txt .
gsutil cp -r gs://BUCKET_NAME/DIR .  # Download directory

# Move/Rename object
gsutil mv gs://BUCKET_NAME/OLD_NAME gs://BUCKET_NAME/NEW_NAME

# Copy between buckets
gsutil cp gs://SOURCE_BUCKET/FILE gs://DEST_BUCKET/

# Delete object
gsutil rm gs://BUCKET_NAME/FILE.txt
gsutil rm -r gs://BUCKET_NAME/DIR/  # Delete directory

# Sync local directory with bucket
gsutil rsync -r LOCAL_DIR gs://BUCKET_NAME/
gsutil rsync -d -r gs://BUCKET_NAME/ LOCAL_DIR  # Delete extra files

# Get object metadata
gsutil stat gs://BUCKET_NAME/FILE.txt

# Set object metadata
gsutil setmeta -h "Content-Type:application/json" gs://BUCKET_NAME/FILE.json

# Make object public
gsutil acl ch -u AllUsers:R gs://BUCKET_NAME/FILE.txt

# Make bucket public
gsutil iam ch allUsers:objectViewer gs://BUCKET_NAME
```

### 13. Access Control
```bash
# Set bucket IAM policy
gsutil iam set policy.json gs://BUCKET_NAME

# Get bucket IAM policy
gsutil iam get gs://BUCKET_NAME

# Grant user read access
gsutil iam ch user:email@example.com:objectViewer gs://BUCKET_NAME

# Grant service account write access
gsutil iam ch serviceAccount:SA@PROJECT.iam.gserviceaccount.com:objectCreator gs://BUCKET_NAME

# Remove permission
gsutil iam ch -d user:email@example.com:objectViewer gs://BUCKET_NAME

# Set CORS configuration
gsutil cors set cors.json gs://BUCKET_NAME

# Get CORS configuration
gsutil cors get gs://BUCKET_NAME
```

---

## Google Kubernetes Engine (GKE)

### 14. Cluster Management
```bash
# List clusters
gcloud container clusters list

# Create cluster (standard)
gcloud container clusters create CLUSTER_NAME \
  --zone=us-central1-a \
  --num-nodes=3 \
  --machine-type=e2-medium \
  --disk-size=50GB

# Create cluster (autopilot mode)
gcloud container clusters create-auto CLUSTER_NAME \
  --region=us-central1

# Create cluster with advanced options
gcloud container clusters create CLUSTER_NAME \
  --zone=us-central1-a \
  --num-nodes=3 \
  --machine-type=e2-standard-4 \
  --enable-autoscaling \
  --min-nodes=2 \
  --max-nodes=10 \
  --enable-autorepair \
  --enable-autoupgrade \
  --network=custom-vpc \
  --subnetwork=custom-subnet \
  --enable-ip-alias \
  --enable-stackdriver-kubernetes

# Get cluster credentials
gcloud container clusters get-credentials CLUSTER_NAME --zone=us-central1-a

# Describe cluster
gcloud container clusters describe CLUSTER_NAME --zone=us-central1-a

# Upgrade cluster
gcloud container clusters upgrade CLUSTER_NAME --zone=us-central1-a

# Resize cluster
gcloud container clusters resize CLUSTER_NAME \
  --num-nodes=5 \
  --zone=us-central1-a

# Delete cluster
gcloud container clusters delete CLUSTER_NAME --zone=us-central1-a
```

### 15. Node Pools
```bash
# List node pools
gcloud container node-pools list --cluster=CLUSTER_NAME --zone=us-central1-a

# Create node pool
gcloud container node-pools create POOL_NAME \
  --cluster=CLUSTER_NAME \
  --zone=us-central1-a \
  --num-nodes=3 \
  --machine-type=n1-standard-2

# Create node pool with taints
gcloud container node-pools create POOL_NAME \
  --cluster=CLUSTER_NAME \
  --zone=us-central1-a \
  --num-nodes=2 \
  --machine-type=n1-highmem-4 \
  --node-taints=workload=memory-intensive:NoSchedule

# Enable autoscaling on node pool
gcloud container node-pools update POOL_NAME \
  --cluster=CLUSTER_NAME \
  --zone=us-central1-a \
  --enable-autoscaling \
  --min-nodes=1 \
  --max-nodes=10

# Delete node pool
gcloud container node-pools delete POOL_NAME \
  --cluster=CLUSTER_NAME \
  --zone=us-central1-a
```

---

## Cloud Functions

### 16. Function Management
```bash
# List functions
gcloud functions list

# Deploy function (Node.js)
gcloud functions deploy FUNCTION_NAME \
  --runtime=nodejs20 \
  --trigger-http \
  --entry-point=helloWorld \
  --source=. \
  --allow-unauthenticated

# Deploy function (Python)
gcloud functions deploy FUNCTION_NAME \
  --runtime=python311 \
  --trigger-http \
  --entry-point=main \
  --source=.

# Deploy with environment variables
gcloud functions deploy FUNCTION_NAME \
  --runtime=nodejs20 \
  --trigger-http \
  --set-env-vars=KEY1=VALUE1,KEY2=VALUE2

# Deploy with Pub/Sub trigger
gcloud functions deploy FUNCTION_NAME \
  --runtime=nodejs20 \
  --trigger-topic=TOPIC_NAME \
  --entry-point=processPubSub

# Deploy with Storage trigger
gcloud functions deploy FUNCTION_NAME \
  --runtime=python311 \
  --trigger-resource=BUCKET_NAME \
  --trigger-event=google.storage.object.finalize

# Deploy with specific memory/timeout
gcloud functions deploy FUNCTION_NAME \
  --runtime=nodejs20 \
  --trigger-http \
  --memory=512MB \
  --timeout=60s \
  --max-instances=100

# Describe function
gcloud functions describe FUNCTION_NAME

# View function logs
gcloud functions logs read FUNCTION_NAME

# Call function
gcloud functions call FUNCTION_NAME --data='{"key":"value"}'

# Delete function
gcloud functions delete FUNCTION_NAME
```

---

## Cloud Run

### 17. Cloud Run Services
```bash
# List services
gcloud run services list

# Deploy service from container image
gcloud run deploy SERVICE_NAME \
  --image=gcr.io/PROJECT_ID/IMAGE:TAG \
  --platform=managed \
  --region=us-central1 \
  --allow-unauthenticated

# Deploy from source (buildpacks)
gcloud run deploy SERVICE_NAME \
  --source=. \
  --region=us-central1 \
  --allow-unauthenticated

# Deploy with environment variables
gcloud run deploy SERVICE_NAME \
  --image=gcr.io/PROJECT_ID/IMAGE:TAG \
  --region=us-central1 \
  --set-env-vars=KEY1=VALUE1,KEY2=VALUE2

# Deploy with secrets
gcloud run deploy SERVICE_NAME \
  --image=gcr.io/PROJECT_ID/IMAGE:TAG \
  --region=us-central1 \
  --set-secrets=SECRET_NAME=SECRET_NAME:latest

# Deploy with resource limits
gcloud run deploy SERVICE_NAME \
  --image=gcr.io/PROJECT_ID/IMAGE:TAG \
  --region=us-central1 \
  --memory=1Gi \
  --cpu=2 \
  --min-instances=1 \
  --max-instances=10 \
  --concurrency=80

# Deploy with VPC connector
gcloud run deploy SERVICE_NAME \
  --image=gcr.io/PROJECT_ID/IMAGE:TAG \
  --region=us-central1 \
  --vpc-connector=CONNECTOR_NAME

# Update service
gcloud run services update SERVICE_NAME \
  --region=us-central1 \
  --set-env-vars=NEW_VAR=VALUE

# Describe service
gcloud run services describe SERVICE_NAME --region=us-central1

# Get service URL
gcloud run services describe SERVICE_NAME \
  --region=us-central1 \
  --format='value(status.url)'

# Set IAM policy (allow unauthenticated)
gcloud run services add-iam-policy-binding SERVICE_NAME \
  --region=us-central1 \
  --member="allUsers" \
  --role="roles/run.invoker"

# Delete service
gcloud run services delete SERVICE_NAME --region=us-central1

# View logs
gcloud logging read "resource.type=cloud_run_revision AND resource.labels.service_name=SERVICE_NAME" \
  --limit=50 \
  --format=json
```

### 18. Cloud Run Jobs
```bash
# Create job
gcloud run jobs create JOB_NAME \
  --image=gcr.io/PROJECT_ID/IMAGE:TAG \
  --region=us-central1

# Execute job
gcloud run jobs execute JOB_NAME --region=us-central1

# List jobs
gcloud run jobs list

# Describe job
gcloud run jobs describe JOB_NAME --region=us-central1

# Update job
gcloud run jobs update JOB_NAME \
  --image=gcr.io/PROJECT_ID/NEW_IMAGE:TAG \
  --region=us-central1

# Delete job
gcloud run jobs delete JOB_NAME --region=us-central1
```

---

## Cloud SQL

### 19. Instance Management
```bash
# List instances
gcloud sql instances list

# Create MySQL instance
gcloud sql instances create INSTANCE_NAME \
  --database-version=MYSQL_8_0 \
  --tier=db-n1-standard-1 \
  --region=us-central1

# Create PostgreSQL instance
gcloud sql instances create INSTANCE_NAME \
  --database-version=POSTGRES_15 \
  --tier=db-custom-2-7680 \
  --region=us-central1

# Create instance with high availability
gcloud sql instances create INSTANCE_NAME \
  --database-version=MYSQL_8_0 \
  --tier=db-n1-standard-2 \
  --region=us-central1 \
  --availability-type=REGIONAL

# Describe instance
gcloud sql instances describe INSTANCE_NAME

# Restart instance
gcloud sql instances restart INSTANCE_NAME

# Delete instance
gcloud sql instances delete INSTANCE_NAME

# Set root password
gcloud sql users set-password root \
  --host=% \
  --instance=INSTANCE_NAME \
  --password=PASSWORD
```

### 20. Database & User Management
```bash
# List databases
gcloud sql databases list --instance=INSTANCE_NAME

# Create database
gcloud sql databases create DATABASE_NAME --instance=INSTANCE_NAME

# Delete database
gcloud sql databases delete DATABASE_NAME --instance=INSTANCE_NAME

# List users
gcloud sql users list --instance=INSTANCE_NAME

# Create user
gcloud sql users create USER_NAME \
  --instance=INSTANCE_NAME \
  --password=PASSWORD

# Delete user
gcloud sql users delete USER_NAME --instance=INSTANCE_NAME
```

### 21. Backups & Exports
```bash
# List backups
gcloud sql backups list --instance=INSTANCE_NAME

# Create backup
gcloud sql backups create --instance=INSTANCE_NAME

# Restore from backup
gcloud sql backups restore BACKUP_ID --backup-instance=INSTANCE_NAME

# Export database
gcloud sql export sql INSTANCE_NAME gs://BUCKET_NAME/export.sql \
  --database=DATABASE_NAME

# Import database
gcloud sql import sql INSTANCE_NAME gs://BUCKET_NAME/import.sql \
  --database=DATABASE_NAME
```

---

## IAM & Security

### 22. Service Accounts
```bash
# List service accounts
gcloud iam service-accounts list

# Create service account
gcloud iam service-accounts create SA_NAME \
  --display-name="Service Account Display Name"

# Delete service account
gcloud iam service-accounts delete SA_EMAIL

# Create key for service account
gcloud iam service-accounts keys create key.json \
  --iam-account=SA_EMAIL

# List keys
gcloud iam service-accounts keys list \
  --iam-account=SA_EMAIL

# Delete key
gcloud iam service-accounts keys delete KEY_ID \
  --iam-account=SA_EMAIL

# Grant role to service account
gcloud projects add-iam-policy-binding PROJECT_ID \
  --member="serviceAccount:SA_EMAIL" \
  --role="roles/storage.admin"
```

### 23. IAM Roles & Permissions
```bash
# List IAM roles
gcloud iam roles list

# Describe role
gcloud iam roles describe roles/storage.admin

# List project IAM policy
gcloud projects get-iam-policy PROJECT_ID

# Add IAM policy binding
gcloud projects add-iam-policy-binding PROJECT_ID \
  --member="user:email@example.com" \
  --role="roles/editor"

# Remove IAM policy binding
gcloud projects remove-iam-policy-binding PROJECT_ID \
  --member="user:email@example.com" \
  --role="roles/editor"

# Create custom role
gcloud iam roles create ROLE_ID \
  --project=PROJECT_ID \
  --title="Custom Role" \
  --description="Custom role description" \
  --permissions=compute.instances.list,compute.instances.get

# Update custom role
gcloud iam roles update ROLE_ID \
  --project=PROJECT_ID \
  --add-permissions=compute.instances.start

# Delete custom role
gcloud iam roles delete ROLE_ID --project=PROJECT_ID

# Grant service account impersonation
gcloud iam service-accounts add-iam-policy-binding SA_EMAIL \
  --member="user:email@example.com" \
  --role="roles/iam.serviceAccountTokenCreator"
```

---

## Networking (VPC)

### 24. VPC Networks
```bash
# List networks
gcloud compute networks list

# Create auto-mode network
gcloud compute networks create NETWORK_NAME \
  --subnet-mode=auto

# Create custom network
gcloud compute networks create NETWORK_NAME \
  --subnet-mode=custom

# Delete network
gcloud compute networks delete NETWORK_NAME

# Describe network
gcloud compute networks describe NETWORK_NAME
```

### 25. Subnets
```bash
# List subnets
gcloud compute networks subnets list

# Create subnet
gcloud compute networks subnets create SUBNET_NAME \
  --network=NETWORK_NAME \
  --region=us-central1 \
  --range=10.0.1.0/24

# Create subnet with secondary ranges (for GKE)
gcloud compute networks subnets create SUBNET_NAME \
  --network=NETWORK_NAME \
  --region=us-central1 \
  --range=10.0.1.0/24 \
  --secondary-range=pods=10.4.0.0/14,services=10.0.32.0/20

# Expand subnet
gcloud compute networks subnets expand-ip-range SUBNET_NAME \
  --region=us-central1 \
  --prefix-length=20

# Delete subnet
gcloud compute networks subnets delete SUBNET_NAME --region=us-central1
```

### 26. Firewall Rules
```bash
# List firewall rules
gcloud compute firewall-rules list

# Create firewall rule (allow SSH)
gcloud compute firewall-rules create allow-ssh \
  --network=NETWORK_NAME \
  --allow=tcp:22 \
  --source-ranges=0.0.0.0/0

# Create firewall rule (allow HTTP/HTTPS)
gcloud compute firewall-rules create allow-web \
  --network=NETWORK_NAME \
  --allow=tcp:80,tcp:443 \
  --source-ranges=0.0.0.0/0 \
  --target-tags=web-server

# Create firewall rule (deny all)
gcloud compute firewall-rules create deny-all \
  --network=NETWORK_NAME \
  --action=DENY \
  --rules=all \
  --source-ranges=0.0.0.0/0 \
  --priority=1000

# Update firewall rule
gcloud compute firewall-rules update RULE_NAME \
  --allow=tcp:22,tcp:3389

# Delete firewall rule
gcloud compute firewall-rules delete RULE_NAME

# Describe firewall rule
gcloud compute firewall-rules describe RULE_NAME
```

### 27. VPC Peering & VPN
```bash
# Create VPC peering
gcloud compute networks peerings create PEERING_NAME \
  --network=NETWORK_NAME \
  --peer-network=PEER_NETWORK_URI

# List VPC peerings
gcloud compute networks peerings list

# Delete VPC peering
gcloud compute networks peerings delete PEERING_NAME \
  --network=NETWORK_NAME

# Create VPN gateway
gcloud compute target-vpn-gateways create VPN_GATEWAY_NAME \
  --network=NETWORK_NAME \
  --region=us-central1

# Reserve static IP for VPN
gcloud compute addresses create VPN_STATIC_IP \
  --region=us-central1
```

### 28. IP Addresses
```bash
# List IP addresses
gcloud compute addresses list

# Reserve static external IP
gcloud compute addresses create ADDRESS_NAME \
  --region=us-central1

# Reserve global static IP (for load balancer)
gcloud compute addresses create ADDRESS_NAME --global

# Describe address
gcloud compute addresses describe ADDRESS_NAME --region=us-central1

# Delete address
gcloud compute addresses delete ADDRESS_NAME --region=us-central1

# Assign static IP to instance
gcloud compute instances delete-access-config INSTANCE_NAME \
  --zone=us-central1-a \
  --access-config-name="External NAT"

gcloud compute instances add-access-config INSTANCE_NAME \
  --zone=us-central1-a \
  --access-config-name="External NAT" \
  --address=STATIC_IP
```

---

## Load Balancing

### 29. HTTP(S) Load Balancer
```bash
# Create health check
gcloud compute health-checks create http http-health-check \
  --port=80 \
  --request-path=/health

# Create backend service
gcloud compute backend-services create BACKEND_NAME \
  --protocol=HTTP \
  --health-checks=http-health-check \
  --global

# Add instance group to backend
gcloud compute backend-services add-backend BACKEND_NAME \
  --instance-group=GROUP_NAME \
  --instance-group-zone=us-central1-a \
  --global

# Create URL map
gcloud compute url-maps create URL_MAP_NAME \
  --default-service=BACKEND_NAME

# Create target HTTP proxy
gcloud compute target-http-proxies create HTTP_PROXY_NAME \
  --url-map=URL_MAP_NAME

# Create forwarding rule
gcloud compute forwarding-rules create HTTP_FORWARDING_RULE \
  --global \
  --target-http-proxy=HTTP_PROXY_NAME \
  --ports=80

# Create SSL certificate (managed)
gcloud compute ssl-certificates create CERT_NAME \
  --domains=example.com,www.example.com \
  --global

# Create target HTTPS proxy
gcloud compute target-https-proxies create HTTPS_PROXY_NAME \
  --url-map=URL_MAP_NAME \
  --ssl-certificates=CERT_NAME

# Create HTTPS forwarding rule
gcloud compute forwarding-rules create HTTPS_FORWARDING_RULE \
  --global \
  --target-https-proxy=HTTPS_PROXY_NAME \
  --ports=443
```

### 30. Network Load Balancer
```bash
# Create target pool
gcloud compute target-pools create TARGET_POOL_NAME \
  --region=us-central1

# Add instances to target pool
gcloud compute target-pools add-instances TARGET_POOL_NAME \
  --instances=INSTANCE_NAME \
  --zone=us-central1-a

# Create forwarding rule
gcloud compute forwarding-rules create FORWARDING_RULE_NAME \
  --region=us-central1 \
  --ports=80 \
  --target-pool=TARGET_POOL_NAME
```

---

## Container Registry & Artifact Registry

### 31. Container Registry (GCR)
```bash
# Configure Docker authentication
gcloud auth configure-docker

# Tag image for GCR
docker tag IMAGE_NAME gcr.io/PROJECT_ID/IMAGE_NAME:TAG

# Push image to GCR
docker push gcr.io/PROJECT_ID/IMAGE_NAME:TAG

# Pull image from GCR
docker pull gcr.io/PROJECT_ID/IMAGE_NAME:TAG

# List images
gcloud container images list --repository=gcr.io/PROJECT_ID

# List tags for image
gcloud container images list-tags gcr.io/PROJECT_ID/IMAGE_NAME

# Delete image
gcloud container images delete gcr.io/PROJECT_ID/IMAGE_NAME:TAG --quiet

# Describe image
gcloud container images describe gcr.io/PROJECT_ID/IMAGE_NAME:TAG
```

### 32. Artifact Registry
```bash
# Create repository
gcloud artifacts repositories create REPO_NAME \
  --repository-format=docker \
  --location=us-central1 \
  --description="Docker repository"

# List repositories
gcloud artifacts repositories list

# Configure Docker authentication
gcloud auth configure-docker us-central1-docker.pkg.dev

# Tag image for Artifact Registry
docker tag IMAGE_NAME us-central1-docker.pkg.dev/PROJECT_ID/REPO_NAME/IMAGE_NAME:TAG

# Push image
docker push us-central1-docker.pkg.dev/PROJECT_ID/REPO_NAME/IMAGE_NAME:TAG

# Pull image
docker pull us-central1-docker.pkg.dev/PROJECT_ID/REPO_NAME/IMAGE_NAME:TAG

# List images
gcloud artifacts docker images list us-central1-docker.pkg.dev/PROJECT_ID/REPO_NAME

# Delete repository
gcloud artifacts repositories delete REPO_NAME --location=us-central1
```

---

## Cloud Build

### 33. Build Management
```bash
# Submit build from source
gcloud builds submit --tag=gcr.io/PROJECT_ID/IMAGE_NAME

# Submit build with cloudbuild.yaml
gcloud builds submit --config=cloudbuild.yaml

# Submit build from GitHub
gcloud builds submit --no-source \
  --substitutions=_REPO_NAME=repo,_BRANCH_NAME=main

# List builds
gcloud builds list

# Describe build
gcloud builds describe BUILD_ID

# View build logs
gcloud builds log BUILD_ID

# Cancel build
gcloud builds cancel BUILD_ID
```

### 34. Build Triggers
```bash
# Create trigger from GitHub
gcloud builds triggers create github \
  --name=TRIGGER_NAME \
  --repo-name=REPO_NAME \
  --repo-owner=OWNER \
  --branch-pattern="^main$" \
  --build-config=cloudbuild.yaml

# List triggers
gcloud builds triggers list

# Run trigger manually
gcloud builds triggers run TRIGGER_NAME \
  --branch=main

# Delete trigger
gcloud builds triggers delete TRIGGER_NAME

# Describe trigger
gcloud builds triggers describe TRIGGER_NAME
```

### 35. Example cloudbuild.yaml
```yaml
# cloudbuild.yaml
steps:
  # Build Docker image
  - name: 'gcr.io/cloud-builders/docker'
    args: ['build', '-t', 'gcr.io/$PROJECT_ID/myapp:$SHORT_SHA', '.']
  
  # Push to Container Registry
  - name: 'gcr.io/cloud-builders/docker'
    args: ['push', 'gcr.io/$PROJECT_ID/myapp:$SHORT_SHA']
  
  # Deploy to Cloud Run
  - name: 'gcr.io/google.com/cloudsdktool/cloud-sdk'
    entrypoint: gcloud
    args:
      - 'run'
      - 'deploy'
      - 'myapp'
      - '--image=gcr.io/$PROJECT_ID/myapp:$SHORT_SHA'
      - '--region=us-central1'
      - '--platform=managed'

images:
  - 'gcr.io/$PROJECT_ID/myapp:$SHORT_SHA'

timeout: 1200s
```

---

## App Engine

### 36. Application Management
```bash
# Create App Engine application
gcloud app create --region=us-central

# Deploy application
gcloud app deploy

# Deploy with specific version
gcloud app deploy --version=v1

# Deploy specific service
gcloud app deploy service.yaml

# List services
gcloud app services list

# Describe service
gcloud app services describe SERVICE_NAME

# Delete service
gcloud app services delete SERVICE_NAME
```

### 37. Versions & Traffic
```bash
# List versions
gcloud app versions list

# Describe version
gcloud app versions describe VERSION_ID --service=SERVICE_NAME

# Split traffic between versions
gcloud app services set-traffic SERVICE_NAME \
  --splits=v1=0.8,v2=0.2

# Migrate all traffic to version
gcloud app services set-traffic SERVICE_NAME \
  --splits=v2=1

# Delete version
gcloud app versions delete VERSION_ID --service=SERVICE_NAME
```

### 38. App Engine Commands
```bash
# Browse application
gcloud app browse

# View logs
gcloud app logs tail -s SERVICE_NAME

# Open Cloud Console
gcloud app open-console

# SSH into instance
gcloud app instances ssh INSTANCE_ID \
  --service=SERVICE_NAME \
  --version=VERSION_ID
```

---

## BigQuery

### 39. Dataset Management
```bash
# List datasets
bq ls

# Create dataset
bq mk DATASET_NAME
bq mk --dataset PROJECT_ID:DATASET_NAME

# Describe dataset
bq show DATASET_NAME

# Update dataset (set expiration)
bq update --default_table_expiration 3600 DATASET_NAME

# Delete dataset
bq rm -r -f DATASET_NAME
```

### 40. Table Operations
```bash
# List tables in dataset
bq ls DATASET_NAME

# Create table from schema
bq mk --table DATASET_NAME.TABLE_NAME schema.json

# Create table from CSV
bq load --source_format=CSV DATASET_NAME.TABLE_NAME \
  gs://BUCKET/data.csv \
  schema.json

# Create table from query
bq query --destination_table=DATASET_NAME.TABLE_NAME \
  --use_legacy_sql=false \
  'SELECT * FROM `project.dataset.source_table` WHERE date > "2024-01-01"'

# Show table schema
bq show --schema DATASET_NAME.TABLE_NAME

# Describe table
bq show DATASET_NAME.TABLE_NAME

# Delete table
bq rm -t DATASET_NAME.TABLE_NAME

# Copy table
bq cp DATASET_NAME.SOURCE_TABLE DATASET_NAME.DEST_TABLE
```

### 41. Query Operations
```bash
# Run query
bq query --use_legacy_sql=false \
  'SELECT name, count FROM `project.dataset.table` LIMIT 10'

# Run query and save to table
bq query --use_legacy_sql=false \
  --destination_table=DATASET_NAME.RESULT_TABLE \
  'SELECT * FROM `project.dataset.table` WHERE status = "active"'

# Run query from file
bq query --use_legacy_sql=false < query.sql

# Dry run (estimate cost)
bq query --dry_run --use_legacy_sql=false \
  'SELECT * FROM `project.dataset.table`'

# Export query results to GCS
bq extract --destination_format=CSV \
  DATASET_NAME.TABLE_NAME \
  gs://BUCKET_NAME/export-*.csv
```

### 42. Jobs
```bash
# List jobs
bq ls -j

# Show job details
bq show -j JOB_ID

# Cancel job
bq cancel JOB_ID

# Wait for job completion
bq wait JOB_ID
```

---

## Pub/Sub

### 43. Topic Management
```bash
# List topics
gcloud pubsub topics list

# Create topic
gcloud pubsub topics create TOPIC_NAME

# Delete topic
gcloud pubsub topics delete TOPIC_NAME

# Describe topic
gcloud pubsub topics describe TOPIC_NAME

# Publish message
gcloud pubsub topics publish TOPIC_NAME --message="Hello World"

# Publish message with attributes
gcloud pubsub topics publish TOPIC_NAME \
  --message="Hello" \
  --attribute=key1=value1,key2=value2
```

### 44. Subscription Management
```bash
# List subscriptions
gcloud pubsub subscriptions list

# Create pull subscription
gcloud pubsub subscriptions create SUBSCRIPTION_NAME \
  --topic=TOPIC_NAME

# Create push subscription
gcloud pubsub subscriptions create SUBSCRIPTION_NAME \
  --topic=TOPIC_NAME \
  --push-endpoint=https://example.com/push

# Create subscription with filter
gcloud pubsub subscriptions create SUBSCRIPTION_NAME \
  --topic=TOPIC_NAME \
  --message-filter='attributes.type="important"'

# Pull messages
gcloud pubsub subscriptions pull SUBSCRIPTION_NAME \
  --limit=10 \
  --auto-ack

# Delete subscription
gcloud pubsub subscriptions delete SUBSCRIPTION_NAME

# Describe subscription
gcloud pubsub subscriptions describe SUBSCRIPTION_NAME
```

---

## Cloud Monitoring & Logging

### 45. Logging
```bash
# Read recent logs
gcloud logging read "timestamp>\"2024-01-01T00:00:00Z\"" \
  --limit=50 \
  --format=json

# Filter logs by resource
gcloud logging read "resource.type=gce_instance" --limit=20

# Filter logs by severity
gcloud logging read "severity>=ERROR" --limit=100

# Tail logs in real-time
gcloud logging tail "resource.type=cloud_run_revision"

# Write log entry
gcloud logging write LOG_NAME "Log message" \
  --severity=INFO

# List logs
gcloud logging logs list

# Delete logs
gcloud logging logs delete LOG_NAME
```

### 46. Monitoring Metrics
```bash
# List metric descriptors
gcloud monitoring metrics-descriptors list

# Create uptime check
gcloud monitoring uptime create UPTIME_CHECK_NAME \
  --resource-type=uptime-url \
  --host=example.com \
  --path=/health

# List uptime checks
gcloud monitoring uptime list

# Delete uptime check
gcloud monitoring uptime delete UPTIME_CHECK_NAME
```

---

## Secret Manager

### 47. Secret Management
```bash
# Create secret
gcloud secrets create SECRET_NAME \
  --replication-policy="automatic"

# Add secret version (from file)
gcloud secrets versions add SECRET_NAME --data-file=/path/to/secret.txt

# Add secret version (from stdin)
echo -n "my-secret-value" | gcloud secrets versions add SECRET_NAME --data-file=-

# List secrets
gcloud secrets list

# Describe secret
gcloud secrets describe SECRET_NAME

# Access secret value
gcloud secrets versions access latest --secret=SECRET_NAME

# List secret versions
gcloud secrets versions list SECRET_NAME

# Delete secret version
gcloud secrets versions destroy VERSION_ID --secret=SECRET_NAME

# Delete secret
gcloud secrets delete SECRET_NAME

# Grant access to secret
gcloud secrets add-iam-policy-binding SECRET_NAME \
  --member="serviceAccount:SA_EMAIL" \
  --role="roles/secretmanager.secretAccessor"
```

---

## Cloud DNS

### 48. Managed Zones
```bash
# List managed zones
gcloud dns managed-zones list

# Create managed zone
gcloud dns managed-zones create ZONE_NAME \
  --dns-name=example.com. \
  --description="Example domain zone"

# Delete managed zone
gcloud dns managed-zones delete ZONE_NAME

# Describe managed zone
gcloud dns managed-zones describe ZONE_NAME
```

### 49. DNS Records
```bash
# List DNS records
gcloud dns record-sets list --zone=ZONE_NAME

# Start transaction
gcloud dns record-sets transaction start --zone=ZONE_NAME

# Add A record
gcloud dns record-sets transaction add "1.2.3.4" \
  --name=example.com. \
  --ttl=300 \
  --type=A \
  --zone=ZONE_NAME

# Add CNAME record
gcloud dns record-sets transaction add "target.example.com." \
  --name=www.example.com. \
  --ttl=300 \
  --type=CNAME \
  --zone=ZONE_NAME

# Remove record
gcloud dns record-sets transaction remove "1.2.3.4" \
  --name=example.com. \
  --ttl=300 \
  --type=A \
  --zone=ZONE_NAME

# Execute transaction
gcloud dns record-sets transaction execute --zone=ZONE_NAME

# Abort transaction
gcloud dns record-sets transaction abort --zone=ZONE_NAME

# Import records from file
gcloud dns record-sets import records.yaml --zone=ZONE_NAME

# Export records to file
gcloud dns record-sets export records.yaml --zone=ZONE_NAME
```

---

## Resource Management

### 50. Billing & Costs
```bash
# List billing accounts
gcloud billing accounts list

# Link project to billing account
gcloud billing projects link PROJECT_ID \
  --billing-account=BILLING_ACCOUNT_ID

# Get project billing info
gcloud billing projects describe PROJECT_ID

# Export billing data to BigQuery
gcloud billing accounts get-iam-policy BILLING_ACCOUNT_ID
```

### 51. Resource Organization
```bash
# List organizations
gcloud organizations list

# List folders
gcloud resource-manager folders list --organization=ORG_ID

# Create folder
gcloud resource-manager folders create \
  --display-name=FOLDER_NAME \
  --organization=ORG_ID

# Move project to folder
gcloud projects move PROJECT_ID --folder=FOLDER_ID

# List labels on project
gcloud projects describe PROJECT_ID --format="value(labels)"

# Add label to project
gcloud projects update PROJECT_ID --update-labels=env=prod,team=backend
```

### 52. APIs & Services
```bash
# List enabled APIs
gcloud services list --enabled

# List available APIs
gcloud services list --available

# Enable API
gcloud services enable compute.googleapis.com
gcloud services enable container.googleapis.com

# Disable API
gcloud services disable compute.googleapis.com

# Get API operation status
gcloud services operations describe OPERATION_ID
```

### 53. Quotas & Limits
```bash
# List quotas
gcloud compute project-info describe --project=PROJECT_ID

# Request quota increase (through Cloud Console)
# https://console.cloud.google.com/iam-admin/quotas

# Check region quotas
gcloud compute regions describe REGION_NAME
```

### 54. Asset Inventory
```bash
# List all resources
gcloud asset search-all-resources --scope=projects/PROJECT_ID

# Search for specific resource type
gcloud asset search-all-resources \
  --scope=projects/PROJECT_ID \
  --asset-types=compute.googleapis.com/Instance

# Export asset inventory
gcloud asset export \
  --output-path=gs://BUCKET_NAME/assets.json \
  --content-type=resource \
  --project=PROJECT_ID
```

---

## Advanced Topics

### 55. Cloud Scheduler
```bash
# List jobs
gcloud scheduler jobs list

# Create job (HTTP target)
gcloud scheduler jobs create http JOB_NAME \
  --schedule="0 */6 * * *" \
  --uri="https://example.com/api/endpoint" \
  --http-method=POST \
  --headers="Content-Type=application/json" \
  --message-body='{"key":"value"}'

# Create job (Pub/Sub target)
gcloud scheduler jobs create pubsub JOB_NAME \
  --schedule="0 2 * * *" \
  --topic=TOPIC_NAME \
  --message-body="Scheduled message"

# Run job manually
gcloud scheduler jobs run JOB_NAME

# Pause job
gcloud scheduler jobs pause JOB_NAME

# Resume job
gcloud scheduler jobs resume JOB_NAME

# Delete job
gcloud scheduler jobs delete JOB_NAME
```

### 56. Cloud Tasks
```bash
# List queues
gcloud tasks queues list

# Create queue
gcloud tasks queues create QUEUE_NAME

# Create HTTP task
gcloud tasks create-http-task \
  --queue=QUEUE_NAME \
  --url=https://example.com/handler \
  --method=POST \
  --body-content='{"key":"value"}' \
  --schedule-time="2024-12-31T23:59:59Z"

# Pause queue
gcloud tasks queues pause QUEUE_NAME

# Resume queue
gcloud tasks queues resume QUEUE_NAME

# Purge queue
gcloud tasks queues purge QUEUE_NAME

# Delete queue
gcloud tasks queues delete QUEUE_NAME
```

### 57. Memorystore (Redis)
```bash
# List instances
gcloud redis instances list --region=us-central1

# Create Redis instance
gcloud redis instances create INSTANCE_NAME \
  --size=1 \
  --region=us-central1 \
  --redis-version=redis_6_x

# Describe instance
gcloud redis instances describe INSTANCE_NAME --region=us-central1

# Update instance
gcloud redis instances update INSTANCE_NAME \
  --size=2 \
  --region=us-central1

# Delete instance
gcloud redis instances delete INSTANCE_NAME --region=us-central1
```

### 58. Filestore (NFS)
```bash
# List instances
gcloud filestore instances list --region=us-central1

# Create instance
gcloud filestore instances create INSTANCE_NAME \
  --zone=us-central1-a \
  --tier=BASIC_HDD \
  --file-share=name=nfs,capacity=1TB \
  --network=name=default

# Delete instance
gcloud filestore instances delete INSTANCE_NAME --zone=us-central1-a
```

### 59. VPC Serverless Connector
```bash
# Create connector
gcloud compute networks vpc-access connectors create CONNECTOR_NAME \
  --region=us-central1 \
  --subnet=SUBNET_NAME \
  --subnet-project=PROJECT_ID

# List connectors
gcloud compute networks vpc-access connectors list --region=us-central1

# Describe connector
gcloud compute networks vpc-access connectors describe CONNECTOR_NAME \
  --region=us-central1

# Delete connector
gcloud compute networks vpc-access connectors delete CONNECTOR_NAME \
  --region=us-central1
```

### 60. Deployment Manager
```bash
# Create deployment
gcloud deployment-manager deployments create DEPLOYMENT_NAME \
  --config=config.yaml

# List deployments
gcloud deployment-manager deployments list

# Describe deployment
gcloud deployment-manager deployments describe DEPLOYMENT_NAME

# Update deployment
gcloud deployment-manager deployments update DEPLOYMENT_NAME \
  --config=config-updated.yaml

# Delete deployment
gcloud deployment-manager deployments delete DEPLOYMENT_NAME
```

---

## Useful Tips & Tricks

### 61. Formatting & Filtering
```bash
# JSON output
gcloud compute instances list --format=json

# YAML output
gcloud compute instances list --format=yaml

# CSV output
gcloud compute instances list --format=csv

# Custom table format
gcloud compute instances list --format="table(name,zone,status,networkInterfaces[0].accessConfigs[0].natIP:label=EXTERNAL_IP)"

# Get specific field value
gcloud compute instances describe INSTANCE_NAME \
  --zone=us-central1-a \
  --format="get(networkInterfaces[0].accessConfigs[0].natIP)"

# Filter with complex expressions
gcloud compute instances list \
  --filter="zone:us-central1-a AND status=RUNNING"

# Combine filters
gcloud compute instances list \
  --filter="machineType:e2-medium OR machineType:e2-small"

# Sort results
gcloud compute instances list --sort-by=creationTimestamp

# Reverse sort
gcloud compute instances list --sort-by=~creationTimestamp
```

### 62. Batch Operations
```bash
# Delete multiple instances
gcloud compute instances delete $(gcloud compute instances list \
  --filter="labels.env=test" --format="value(name)") \
  --zone=us-central1-a --quiet

# Stop all instances in zone
gcloud compute instances list --filter="zone:us-central1-a" \
  --format="value(name)" | \
  xargs -I {} gcloud compute instances stop {} --zone=us-central1-a

# Add label to all instances
gcloud compute instances list --format="value(name,zone)" | \
  while read name zone; do
    gcloud compute instances add-labels $name --zone=$zone --labels=managed=true
  done
```

### 63. Scripting & Automation
```bash
# Get project ID
PROJECT_ID=$(gcloud config get-value project)

# Get project number
PROJECT_NUMBER=$(gcloud projects describe $PROJECT_ID --format="value(projectNumber)")

# Get instance IP
INSTANCE_IP=$(gcloud compute instances describe INSTANCE_NAME \
  --zone=us-central1-a \
  --format="get(networkInterfaces[0].accessConfigs[0].natIP)")

# Loop through all projects
gcloud projects list --format="value(projectId)" | while read project; do
  echo "Processing project: $project"
  gcloud compute instances list --project=$project
done

# Create instance with generated name
TIMESTAMP=$(date +%Y%m%d-%H%M%S)
gcloud compute instances create "instance-${TIMESTAMP}" \
  --zone=us-central1-a \
  --machine-type=e2-micro
```

### 64. Configuration Shortcuts
```bash
# Use environment variable for project
export CLOUDSDK_CORE_PROJECT=my-project-id
export CLOUDSDK_COMPUTE_REGION=us-central1
export CLOUDSDK_COMPUTE_ZONE=us-central1-a

# Disable prompts (for scripts)
gcloud compute instances delete INSTANCE_NAME \
  --zone=us-central1-a \
  --quiet  # or -q

# Increase verbosity
gcloud compute instances create INSTANCE_NAME --verbosity=debug

# Use different configuration
gcloud --configuration=production compute instances list

# Set format globally
gcloud config set core/format json

# Disable color output
gcloud config set core/disable_color true
```

### 65. Metadata & Labels
```bash
# Set instance metadata
gcloud compute instances add-metadata INSTANCE_NAME \
  --zone=us-central1-a \
  --metadata=key1=value1,key2=value2

# Set project-wide metadata
gcloud compute project-info add-metadata \
  --metadata=ssh-keys="user:ssh-rsa AAAA..."

# Add labels
gcloud compute instances add-labels INSTANCE_NAME \
  --zone=us-central1-a \
  --labels=env=prod,team=backend

# Update labels
gcloud compute instances update INSTANCE_NAME \
  --zone=us-central1-a \
  --update-labels=version=v2

# Remove labels
gcloud compute instances remove-labels INSTANCE_NAME \
  --zone=us-central1-a \
  --labels=old-label
```

---

## Best Practices

### Security Best Practices
- Use service accounts with minimal permissions
- Enable VPC Service Controls for sensitive data
- Rotate service account keys regularly
- Use Secret Manager for sensitive data
- Enable audit logging
- Implement organization policies
- Use private Google Access for VMs without public IPs
- Enable OS Login for SSH access management

### Cost Optimization
- Use committed use discounts for predictable workloads
- Implement autoscaling for variable workloads
- Use preemptible VMs for fault-tolerant workloads
- Set up budget alerts
- Use Cloud Storage lifecycle policies
- Right-size your resources based on monitoring data
- Clean up unused resources (snapshots, IPs, disks)

### Operational Excellence
- Use labels consistently for resource organization
- Implement infrastructure as code (Terraform, Deployment Manager)
- Set up monitoring and alerting
- Use Cloud Build for CI/CD
- Implement proper backup and disaster recovery
- Use managed services when possible
- Document your architecture and runbooks

---

## Interview Scenarios

### Scenario 1: Multi-Tier Web Application on GCP
```bash
# 1. Create custom VPC network
gcloud compute networks create app-vpc --subnet-mode=custom

# 2. Create subnets for different tiers
gcloud compute networks subnets create web-subnet \
  --network=app-vpc \
  --region=us-central1 \
  --range=10.0.1.0/24

gcloud compute networks subnets create app-subnet \
  --network=app-vpc \
  --region=us-central1 \
  --range=10.0.2.0/24

gcloud compute networks subnets create db-subnet \
  --network=app-vpc \
  --region=us-central1 \
  --range=10.0.3.0/24

# 3. Create firewall rules
gcloud compute firewall-rules create allow-web \
  --network=app-vpc \
  --allow=tcp:80,tcp:443 \
  --source-ranges=0.0.0.0/0 \
  --target-tags=web-tier

gcloud compute firewall-rules create allow-app \
  --network=app-vpc \
  --allow=tcp:8080 \
  --source-tags=web-tier \
  --target-tags=app-tier

gcloud compute firewall-rules create allow-db \
  --network=app-vpc \
  --allow=tcp:5432 \
  --source-tags=app-tier \
  --target-tags=db-tier

# 4. Create instance template for web tier
gcloud compute instance-templates create web-template \
  --machine-type=e2-medium \
  --network=app-vpc \
  --subnet=web-subnet \
  --tags=web-tier \
  --metadata=startup-script='#!/bin/bash
    apt-get update
    apt-get install -y nginx
    systemctl start nginx'

# 5. Create managed instance group with autoscaling
gcloud compute instance-groups managed create web-group \
  --template=web-template \
  --size=2 \
  --zone=us-central1-a

gcloud compute instance-groups managed set-autoscaling web-group \
  --zone=us-central1-a \
  --min-num-replicas=2 \
  --max-num-replicas=10 \
  --target-cpu-utilization=0.75

# 6. Create Cloud SQL instance
gcloud sql instances create app-db \
  --database-version=POSTGRES_15 \
  --tier=db-custom-2-7680 \
  --region=us-central1 \
  --network=projects/PROJECT_ID/global/networks/app-vpc \
  --no-assign-ip

# 7. Create load balancer
gcloud compute health-checks create http web-health-check \
  --port=80 \
  --request-path=/health

gcloud compute backend-services create web-backend \
  --protocol=HTTP \
  --health-checks=web-health-check \
  --global

gcloud compute backend-services add-backend web-backend \
  --instance-group=web-group \
  --instance-group-zone=us-central1-a \
  --global

gcloud compute url-maps create web-url-map \
  --default-service=web-backend

gcloud compute target-http-proxies create web-http-proxy \
  --url-map=web-url-map

gcloud compute forwarding-rules create web-forwarding-rule \
  --global \
  --target-http-proxy=web-http-proxy \
  --ports=80
```

### Scenario 2: Serverless Microservices Architecture
```bash
# 1. Create Pub/Sub topics for event-driven architecture
gcloud pubsub topics create orders
gcloud pubsub topics create payments
gcloud pubsub topics create notifications

# 2. Deploy Cloud Run services
gcloud run deploy order-service \
  --image=gcr.io/PROJECT_ID/order-service:latest \
  --region=us-central1 \
  --set-env-vars=PUBSUB_TOPIC=orders \
  --allow-unauthenticated

gcloud run deploy payment-service \
  --image=gcr.io/PROJECT_ID/payment-service:latest \
  --region=us-central1 \
  --set-env-vars=PUBSUB_TOPIC=payments \
  --no-allow-unauthenticated

gcloud run deploy notification-service \
  --image=gcr.io/PROJECT_ID/notification-service:latest \
  --region=us-central1 \
  --set-env-vars=SMTP_SERVER=smtp.gmail.com \
  --no-allow-unauthenticated

# 3. Create Pub/Sub subscriptions with push to Cloud Run
gcloud pubsub subscriptions create payment-sub \
  --topic=orders \
  --push-endpoint=https://payment-service-xyz.run.app/process \
  --push-auth-service-account=SA_EMAIL

gcloud pubsub subscriptions create notification-sub \
  --topic=payments \
  --push-endpoint=https://notification-service-xyz.run.app/notify \
  --push-auth-service-account=SA_EMAIL

# 4. Create Cloud Scheduler for periodic tasks
gcloud scheduler jobs create http cleanup-job \
  --schedule="0 2 * * *" \
  --uri="https://order-service-xyz.run.app/cleanup" \
  --http-method=POST \
  --oidc-service-account-email=SA_EMAIL

# 5. Set up Cloud Storage for file uploads
gsutil mb -l us-central1 gs://PROJECT_ID-uploads
gsutil lifecycle set lifecycle.json gs://PROJECT_ID-uploads

# 6. Create Cloud Function for file processing
gcloud functions deploy process-upload \
  --runtime=python311 \
  --trigger-resource=PROJECT_ID-uploads \
  --trigger-event=google.storage.object.finalize \
  --entry-point=process_file \
  --set-env-vars=OUTPUT_BUCKET=PROJECT_ID-processed
```

### Scenario 3: GKE with CI/CD Pipeline
```bash
# 1. Create GKE cluster with advanced features
gcloud container clusters create prod-cluster \
  --zone=us-central1-a \
  --num-nodes=3 \
  --machine-type=n1-standard-4 \
  --enable-autoscaling \
  --min-nodes=3 \
  --max-nodes=10 \
  --enable-autorepair \
  --enable-autoupgrade \
  --enable-stackdriver-kubernetes \
  --addons=HorizontalPodAutoscaling,HttpLoadBalancing,GcePersistentDiskCsiDriver \
  --workload-pool=PROJECT_ID.svc.id.goog

# 2. Get cluster credentials
gcloud container clusters get-credentials prod-cluster --zone=us-central1-a

# 3. Create namespace
kubectl create namespace production

# 4. Create Cloud Build trigger for CI/CD
gcloud builds triggers create github \
  --name=deploy-to-gke \
  --repo-name=myapp \
  --repo-owner=myorg \
  --branch-pattern="^main$" \
  --build-config=cloudbuild.yaml \
  --substitutions=_CLUSTER=prod-cluster,_ZONE=us-central1-a,_NAMESPACE=production

# 5. Create service account for Cloud Build
gcloud iam service-accounts create cloud-build-gke \
  --display-name="Cloud Build GKE Deployer"

gcloud projects add-iam-policy-binding PROJECT_ID \
  --member="serviceAccount:cloud-build-gke@PROJECT_ID.iam.gserviceaccount.com" \
  --role="roles/container.developer"

# 6. Example cloudbuild.yaml for GKE deployment
cat <<EOF > cloudbuild.yaml
steps:
  # Build image
  - name: 'gcr.io/cloud-builders/docker'
    args: ['build', '-t', 'gcr.io/\$PROJECT_ID/myapp:\$SHORT_SHA', '.']
  
  # Push image
  - name: 'gcr.io/cloud-builders/docker'
    args: ['push', 'gcr.io/\$PROJECT_ID/myapp:\$SHORT_SHA']
  
  # Deploy to GKE
  - name: 'gcr.io/cloud-builders/gke-deploy'
    args:
      - run
      - --filename=k8s/
      - --image=gcr.io/\$PROJECT_ID/myapp:\$SHORT_SHA
      - --location=\${_ZONE}
      - --cluster=\${_CLUSTER}
      - --namespace=\${_NAMESPACE}

images:
  - 'gcr.io/\$PROJECT_ID/myapp:\$SHORT_SHA'
EOF
```

---

## Quick Reference

### Common Regions & Zones
- **us-east1** (South Carolina): us-east1-a, us-east1-b, us-east1-c, us-east1-d
- **us-central1** (Iowa): us-central1-a, us-central1-b, us-central1-c, us-central1-f
- **us-west1** (Oregon): us-west1-a, us-west1-b, us-west1-c
- **europe-west1** (Belgium): europe-west1-b, europe-west1-c, europe-west1-d
- **asia-east1** (Taiwan): asia-east1-a, asia-east1-b, asia-east1-c

### Machine Types
- **General Purpose**: e2-micro, e2-small, e2-medium, e2-standard-2/4/8/16
- **Compute Optimized**: c2-standard-4/8/16/30/60
- **Memory Optimized**: m1-megamem-96, m1-ultramem-40/80/160
- **Custom**: custom-CPUS-MEMORY (e.g., custom-4-16384)

### Storage Classes
- **Standard**: Hot data, frequent access
- **Nearline**: Data accessed < once/month
- **Coldline**: Data accessed < once/quarter
- **Archive**: Data accessed < once/year

### Database Options
- **Cloud SQL**: MySQL, PostgreSQL, SQL Server
- **Cloud Spanner**: Globally distributed relational
- **Firestore**: NoSQL document database
- **Bigtable**: Wide-column NoSQL database
- **Memorystore**: In-memory cache (Redis, Memcached)

---

**💡 Pro Tips:**
- Always use `--project` flag when working with multiple projects
- Use `gcloud config configurations` to manage multiple environments
- Enable billing alerts to avoid unexpected charges
- Use `--dry-run` flag to preview changes before execution
- Leverage labels for cost tracking and resource organization
- Use Cloud Shell for quick operations without local setup
- Set up budget alerts and quotas to control costs
- Use VPC Service Controls for enhanced security
- Implement least privilege access with IAM
- Enable audit logs for compliance and security

**Total Commands:** 300+ essential GCP and gcloud CLI operations
**Coverage:** Compute, Storage, Kubernetes, Serverless, Databases, Networking, Security, Monitoring, CI/CD
