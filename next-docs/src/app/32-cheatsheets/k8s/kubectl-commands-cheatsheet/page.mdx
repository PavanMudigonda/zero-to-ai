# kubectl Commands - Complete Cheatsheet

Practice these commands with your GKE cluster: **nginx-1 deployment with 3 replicas**

---

## 1. Cluster Information Commands

**Command 1:** Check cluster info
```bash
kubectl cluster-info
```

**Command 2:** Check versions
```bash
kubectl version
```

**Command 3:** View config
```bash
kubectl config view
```

**Command 4:** List API resources
```bash
kubectl api-resources
```

**Command 5:** List API versions
```bash
kubectl api-versions
```

**Command 6:** List everything
```bash
kubectl get all --all-namespaces
```

---

## 2. Pod Commands

**Command 7:** List pods
```bash
kubectl get pod
```

**Command 8:** List pods with details
```bash
kubectl get pod -o wide
```

**Command 9:** Describe a pod (use your actual pod name)
```bash
kubectl describe pod nginx-1-xxxxx
```

**Command 10:** Get pod logs
```bash
kubectl logs nginx-1-xxxxx
```

**Command 11:** Follow pod logs (stream)
```bash
kubectl logs -f nginx-1-xxxxx
```

**Command 12:** Last 20 lines of logs
```bash
kubectl logs --tail=20 nginx-1-xxxxx
```

**Command 13:** Logs from last hour
```bash
kubectl logs --since=1h nginx-1-xxxxx
```

**Command 14:** Get shell in pod
```bash
kubectl exec -it nginx-1-xxxxx -- /bin/bash
```

**Command 15:** Run command in pod
```bash
kubectl exec nginx-1-xxxxx -- ls /usr/share/nginx/html
```

**Command 16:** Top pods (resource usage)
```bash
kubectl top pod
```

**Command 17:** Delete a pod
```bash
kubectl delete pod nginx-1-xxxxx
```

---

## 3. Deployment Commands

**Command 18:** List deployments
```bash
kubectl get deployment
```

**Command 19:** Describe deployment
```bash
kubectl describe deployment nginx-1
```

**Command 20:** Get deployment YAML
```bash
kubectl get deployment nginx-1 -o yaml
```

**Command 21:** Edit deployment (opens editor)
```bash
kubectl edit deployment nginx-1
```

**Command 22:** Scale deployment
```bash
kubectl scale deployment nginx-1 --replicas=5
```

**Command 23:** Check rollout status
```bash
kubectl rollout status deployment nginx-1
```

**Command 24:** Rollout history
```bash
kubectl rollout history deployment nginx-1
```

**Command 25:** Create deployment
```bash
kubectl create deployment test-app --image=nginx:latest
```

**Command 26:** Delete deployment
```bash
kubectl delete deployment test-app
```

---

## 4. Service Commands

**Command 27:** List services
```bash
kubectl get services
```

**Command 28:** Describe service
```bash
kubectl describe services nginx-1
```

**Command 29:** Expose deployment as LoadBalancer
```bash
kubectl expose deployment nginx-1 --port=80 --type=LoadBalancer
```

**Command 30:** Expose deployment as ClusterIP
```bash
kubectl expose deployment nginx-1 --port=80 --type=ClusterIP --name=nginx-internal
```

**Command 31:** Edit service
```bash
kubectl edit services nginx-1
```

**Command 32:** Delete service
```bash
kubectl delete service nginx-1
```

---

## 5. Events Commands

**Command 33:** Get all events
```bash
kubectl get events
```

**Command 34:** Get events sorted by time
```bash
kubectl get events --sort-by='.lastTimestamp'
```

**Command 35:** Get only warnings
```bash
kubectl get events --field-selector type=Warning
```

**Command 36:** Exclude pod events
```bash
kubectl get events --field-selector involvedObject.kind!=Pod
```

---

## 6. Namespace Commands

**Command 37:** List namespaces
```bash
kubectl get namespace
```

**Command 38:** Create namespace
```bash
kubectl create namespace dev
```

**Command 39:** Describe namespace
```bash
kubectl describe namespace default
```

**Command 40:** Delete namespace
```bash
kubectl delete namespace dev
```

**Command 41:** Get pods in specific namespace
```bash
kubectl get pods -n kube-system
```

**Command 42:** Get all resources in namespace
```bash
kubectl get all -n default
```

---

## 7. Node Commands

**Command 43:** List nodes
```bash
kubectl get node
```

**Command 44:** Describe node
```bash
kubectl describe node
```

**Command 45:** Top nodes (resource usage)
```bash
kubectl top node
```

**Command 46:** See pods on specific node
```bash
kubectl get pods -o wide --all-namespaces
```

**Command 47:** Mark node unschedulable
```bash
kubectl cordon <node_name>
```

**Command 48:** Mark node schedulable
```bash
kubectl uncordon <node_name>
```

---

## 8. YAML/Manifest Commands

**Command 49:** Apply YAML file
```bash
kubectl apply -f manifest.yaml
```

**Command 50:** Create from YAML
```bash
kubectl create -f manifest.yaml
```

**Command 51:** Delete using YAML
```bash
kubectl delete -f manifest.yaml
```

**Command 52:** Apply all YAML in directory
```bash
kubectl apply -f ./k8s/
```

---

## 9. ConfigMap & Secret Commands

**Command 53:** Create configmap from literal
```bash
kubectl create configmap my-config --from-literal=key1=value1 --from-literal=key2=value2
```

**Command 54:** List configmaps
```bash
kubectl get configmap
```

**Command 55:** Describe configmap
```bash
kubectl describe configmap my-config
```

**Command 56:** Create secret
```bash
kubectl create secret generic my-secret --from-literal=password=mysecretpass
```

**Command 57:** List secrets
```bash
kubectl get secrets
```

**Command 58:** Describe secret
```bash
kubectl describe secrets my-secret
```

---

## 10. Advanced Commands

**Command 59:** Port forward to pod
```bash
kubectl port-forward nginx-1-xxxxx 8080:80
```

**Command 60:** Port forward to service
```bash
kubectl port-forward service/nginx-1 8080:80
```

**Command 61:** Run temporary debug pod
```bash
kubectl run debug --image=busybox:latest --rm -it -- sh
```

**Command 62:** Create pod imperatively
```bash
kubectl run test-pod --image=nginx:latest --port=80
```

**Command 63:** Watch resources (live updates)
```bash
kubectl get pods -w
```

**Command 64:** Get resource as JSON
```bash
kubectl get pod nginx-1-xxxxx -o json
```

**Command 65:** Get specific field using JSONPath
```bash
kubectl get pods -o jsonpath='{.items[*].metadata.name}'
```

---

## 11. Daemonsets

**Command 66:** List daemonsets
```bash
kubectl get daemonset
```

**Command 67:** Describe daemonset
```bash
kubectl describe daemonset <daemonset_name>
```

**Command 68:** Edit daemonset
```bash
kubectl edit daemonset <daemonset_name>
```

**Command 69:** Delete daemonset
```bash
kubectl delete daemonset <daemonset_name>
```

---

## 12. ReplicaSets

**Command 70:** List replicasets
```bash
kubectl get replicasets
```

**Command 71:** Describe replicaset
```bash
kubectl describe replicasets <replicaset_name>
```

**Command 72:** Scale replicaset
```bash
kubectl scale --replicas=3 replicaset/<replicaset_name>
```

---

## 13. StatefulSets

**Command 73:** List statefulsets
```bash
kubectl get statefulset
```

**Command 74:** Describe statefulset
```bash
kubectl describe statefulset <statefulset_name>
```

**Command 75:** Delete statefulset (keep pods)
```bash
kubectl delete statefulset/<statefulset_name> --cascade=false
```

---

## 14. Service Accounts

**Command 76:** List service accounts
```bash
kubectl get serviceaccounts
```

**Command 77:** Describe service account
```bash
kubectl describe serviceaccounts <sa_name>
```

**Command 78:** Delete service account
```bash
kubectl delete serviceaccount <sa_name>
```

---

## 15. Labels & Annotations

**Command 79:** Add label to pod
```bash
kubectl label pod <pod_name> environment=production
```

**Command 80:** Add label to node
```bash
kubectl label node <node_name> disktype=ssd
```

**Command 81:** Remove label from pod
```bash
kubectl label pod <pod_name> environment-
```

**Command 82:** Add annotation to pod
```bash
kubectl annotate pod <pod_name> description="My web app"
```

**Command 83:** Get pods by label
```bash
kubectl get pods -l environment=production
```

**Command 84:** Get pods with multiple label selectors
```bash
kubectl get pods -l 'environment in (production,staging)'
```

---

## 16. Resource Management

**Command 85:** Set resource requests/limits
```bash
kubectl set resources deployment nginx-1 --limits=cpu=200m,memory=512Mi --requests=cpu=100m,memory=256Mi
```

**Command 86:** Get pod resource usage
```bash
kubectl top pod --containers
```

**Command 87:** Get node resource allocation
```bash
kubectl describe nodes | grep Allocated -A 5
```

---

## 17. Rollout Management

**Command 88:** Pause rollout
```bash
kubectl rollout pause deployment nginx-1
```

**Command 89:** Resume rollout
```bash
kubectl rollout resume deployment nginx-1
```

**Command 90:** Undo rollout (rollback)
```bash
kubectl rollout undo deployment nginx-1
```

**Command 91:** Rollback to specific revision
```bash
kubectl rollout undo deployment nginx-1 --to-revision=2
```

**Command 92:** Restart deployment (rolling restart)
```bash
kubectl rollout restart deployment nginx-1
```

---

## 18. Context & Configuration

**Command 93:** Get current context
```bash
kubectl config current-context
```

**Command 94:** List all contexts
```bash
kubectl config get-contexts
```

**Command 95:** Switch context
```bash
kubectl config use-context <context_name>
```

**Command 96:** Set namespace for current context
```bash
kubectl config set-context --current --namespace=dev
```

**Command 97:** View kubeconfig
```bash
kubectl config view
```

---

## 19. Copying Files

**Command 98:** Copy file from pod to local
```bash
kubectl cp <pod_name>:/path/to/file /local/path
```

**Command 99:** Copy file from local to pod
```bash
kubectl cp /local/path <pod_name>:/path/to/file
```

---

## 20. Drain & Maintenance

**Command 100:** Drain node (evict all pods)
```bash
kubectl drain <node_name> --ignore-daemonsets --delete-emptydir-data
```

**Command 101:** Drain node with force
```bash
kubectl drain <node_name> --ignore-daemonsets --delete-emptydir-data --force
```

**Command 102:** Taint a node
```bash
kubectl taint nodes <node_name> key=value:NoSchedule
```

**Command 103:** Remove taint from node
```bash
kubectl taint nodes <node_name> key=value:NoSchedule-
```

**Command 104:** Update node labels
```bash
kubectl label nodes <node_name> disktype=ssd
```

---

## 21. RBAC (Role-Based Access Control)

**Command 105:** List roles
```bash
kubectl get roles
```

**Command 106:** List cluster roles
```bash
kubectl get clusterroles
```

**Command 107:** Describe role
```bash
kubectl describe role <role_name>
```

**Command 108:** List role bindings
```bash
kubectl get rolebindings
```

**Command 109:** List cluster role bindings
```bash
kubectl get clusterrolebindings
```

**Command 110:** Create role
```bash
kubectl create role pod-reader --verb=get,list,watch --resource=pods
```

**Command 111:** Create cluster role
```bash
kubectl create clusterrole pod-reader --verb=get,list,watch --resource=pods
```

**Command 112:** Create role binding
```bash
kubectl create rolebinding read-pods --role=pod-reader --user=jane
```

**Command 113:** Create cluster role binding
```bash
kubectl create clusterrolebinding read-pods --clusterrole=pod-reader --user=jane
```

**Command 114:** Check if user can perform action (auth check)
```bash
kubectl auth can-i create pods
```

**Command 115:** Check permissions for specific user
```bash
kubectl auth can-i create pods --as=jane
```

**Command 116:** Check permissions in namespace
```bash
kubectl auth can-i create pods --as=jane -n dev
```

**Command 117:** List all permissions for current user
```bash
kubectl auth can-i --list
```

---

## 22. PersistentVolumes & Claims

**Command 118:** List persistent volumes
```bash
kubectl get pv
```

**Command 119:** List persistent volume claims
```bash
kubectl get pvc
```

**Command 120:** Describe PV
```bash
kubectl describe pv <pv_name>
```

**Command 121:** Describe PVC
```bash
kubectl describe pvc <pvc_name>
```

**Command 122:** Create PVC from YAML
```bash
kubectl apply -f pvc.yaml
```

**Command 123:** Delete PVC
```bash
kubectl delete pvc <pvc_name>
```

**Command 124:** Get PVC with capacity info
```bash
kubectl get pvc -o custom-columns=NAME:.metadata.name,CAPACITY:.spec.resources.requests.storage,STATUS:.status.phase
```

---

## 23. Jobs & CronJobs

**Command 125:** List jobs
```bash
kubectl get jobs
```

**Command 126:** List cronjobs
```bash
kubectl get cronjobs
```

**Command 127:** Create job from image
```bash
kubectl create job test-job --image=busybox -- echo "Hello"
```

**Command 128:** Create cronjob
```bash
kubectl create cronjob test-cron --image=busybox --schedule="*/5 * * * *" -- echo "Hello"
```

**Command 129:** Describe job
```bash
kubectl describe job <job_name>
```

**Command 130:** Get job logs
```bash
kubectl logs job/<job_name>
```

**Command 131:** Delete completed jobs
```bash
kubectl delete jobs --field-selector status.successful=1
```

**Command 132:** Suspend cronjob
```bash
kubectl patch cronjob <cronjob_name> -p '{"spec":{"suspend":true}}'
```

**Command 133:** Resume cronjob
```bash
kubectl patch cronjob <cronjob_name> -p '{"spec":{"suspend":false}}'
```

**Command 134:** Trigger cronjob manually
```bash
kubectl create job --from=cronjob/<cronjob_name> <job_name>
```

---

## 24. Ingress Resources

**Command 135:** List ingress resources
```bash
kubectl get ingress
```

**Command 136:** Describe ingress
```bash
kubectl describe ingress <ingress_name>
```

**Command 137:** Get ingress with endpoints
```bash
kubectl get ingress -o wide
```

**Command 138:** Edit ingress
```bash
kubectl edit ingress <ingress_name>
```

**Command 139:** Create ingress
```bash
kubectl create ingress simple --rule="foo.com/bar=svc:8080"
```

**Command 140:** Get ingress class
```bash
kubectl get ingressclass
```

---

## 25. NetworkPolicy

**Command 141:** List network policies
```bash
kubectl get networkpolicy
```

**Command 142:** Describe network policy
```bash
kubectl describe networkpolicy <policy_name>
```

**Command 143:** Delete network policy
```bash
kubectl delete networkpolicy <policy_name>
```

---

## 26. HorizontalPodAutoscaler (HPA)

**Command 144:** List HPAs
```bash
kubectl get hpa
```

**Command 145:** Create HPA
```bash
kubectl autoscale deployment nginx-1 --cpu-percent=50 --min=1 --max=10
```

**Command 146:** Describe HPA
```bash
kubectl describe hpa <hpa_name>
```

**Command 147:** Delete HPA
```bash
kubectl delete hpa <hpa_name>
```

**Command 148:** Get HPA with targets
```bash
kubectl get hpa -w
```

---

## 27. ResourceQuota & LimitRange

**Command 149:** List resource quotas
```bash
kubectl get resourcequota
```

**Command 150:** Describe resource quota
```bash
kubectl describe resourcequota <quota_name>
```

**Command 151:** Create resource quota
```bash
kubectl create quota my-quota --hard=cpu=1,memory=1G,pods=2
```

**Command 152:** List limit ranges
```bash
kubectl get limitrange
```

**Command 153:** Describe limit range
```bash
kubectl describe limitrange <limitrange_name>
```

---

## 28. PodDisruptionBudget

**Command 154:** List pod disruption budgets
```bash
kubectl get pdb
```

**Command 155:** Describe PDB
```bash
kubectl describe pdb <pdb_name>
```

**Command 156:** Create PDB
```bash
kubectl create pdb my-pdb --selector=app=nginx --min-available=2
```

---

## 29. Advanced Debugging (kubectl debug)

**Command 157:** Debug pod with ephemeral container
```bash
kubectl debug <pod_name> -it --image=busybox
```

**Command 158:** Debug by creating copy of pod
```bash
kubectl debug <pod_name> -it --copy-to=debug-pod --container=myapp
```

**Command 159:** Debug node with privileged container
```bash
kubectl debug node/<node_name> -it --image=ubuntu
```

**Command 160:** Debug with different image
```bash
kubectl debug <pod_name> -it --image=busybox --target=<container_name>
```

**Command 161:** Debug CrashLoopBackOff pod
```bash
kubectl debug <pod_name> -it --copy-to=debug-pod -- sh
```

---

## 30. Advanced Output & Formatting

**Command 162:** Custom columns output
```bash
kubectl get pods -o custom-columns=NAME:.metadata.name,STATUS:.status.phase,NODE:.spec.nodeName
```

**Command 163:** JSONPath with sorting
```bash
kubectl get pods --sort-by=.metadata.creationTimestamp
```

**Command 164:** JSONPath for specific field
```bash
kubectl get pods -o jsonpath='{.items[0].spec.containers[0].image}'
```

**Command 165:** Get pod IPs
```bash
kubectl get pods -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.status.podIP}{"\n"}{end}'
```

**Command 166:** Show resource limits
```bash
kubectl get pods -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.spec.containers[*].resources.limits.memory}{"\n"}{end}'
```

**Command 167:** Get all container images
```bash
kubectl get pods -A -o jsonpath='{range .items[*]}{.spec.containers[*].image}{"\n"}{end}' | sort -u
```

---

## 31. Patch & Update Commands

**Command 168:** Patch resource with strategic merge
```bash
kubectl patch deployment nginx-1 -p '{"spec":{"replicas":5}}'
```

**Command 169:** Patch with JSON patch
```bash
kubectl patch pod <pod_name> --type='json' -p='[{"op":"replace","path":"/spec/containers/0/image","value":"nginx:1.21"}]'
```

**Command 170:** Update image
```bash
kubectl set image deployment/nginx-1 nginx=nginx:1.21
```

**Command 171:** Set environment variable
```bash
kubectl set env deployment/nginx-1 ENV=production
```

**Command 172:** Set service account
```bash
kubectl set serviceaccount deployment nginx-1 myserviceaccount
```

---

## 32. Diff & Apply

**Command 173:** Diff before applying
```bash
kubectl diff -f manifest.yaml
```

**Command 174:** Apply with server-side apply
```bash
kubectl apply --server-side -f manifest.yaml
```

**Command 175:** Apply and record change
```bash
kubectl apply -f manifest.yaml --record
```

**Command 176:** Prune resources
```bash
kubectl apply -f manifest.yaml --prune -l app=myapp
```

---

## 33. Kustomize Integration

**Command 177:** Apply kustomization
```bash
kubectl apply -k ./kustomize/overlays/production
```

**Command 178:** View kustomize output
```bash
kubectl kustomize ./kustomize/overlays/production
```

**Command 179:** Diff kustomize changes
```bash
kubectl diff -k ./kustomize/overlays/production
```

---

## 34. Wait & Conditions

**Command 180:** Wait for deployment rollout
```bash
kubectl wait --for=condition=available --timeout=300s deployment/nginx-1
```

**Command 181:** Wait for pod ready
```bash
kubectl wait --for=condition=ready pod -l app=nginx
```

**Command 182:** Wait for job completion
```bash
kubectl wait --for=condition=complete --timeout=600s job/my-job
```

**Command 183:** Wait for pod deletion
```bash
kubectl wait --for=delete pod/<pod_name> --timeout=60s
```

---

## 35. Explain & Documentation

**Command 184:** Explain resource
```bash
kubectl explain pod
```

**Command 185:** Explain nested field
```bash
kubectl explain pod.spec.containers
```

**Command 186:** Explain with examples
```bash
kubectl explain deployment --recursive
```

---

## 36. API Resources & Discovery

**Command 187:** Get API resources in specific group
```bash
kubectl api-resources --api-group=apps
```

**Command 188:** Get namespaced resources only
```bash
kubectl api-resources --namespaced=true
```

**Command 189:** Get cluster-scoped resources
```bash
kubectl api-resources --namespaced=false
```

**Command 190:** Get resources by verb
```bash
kubectl api-resources --verbs=list,get
```

---

## 37. Certificate Management

**Command 191:** Get certificate signing requests
```bash
kubectl get csr
```

**Command 192:** Approve CSR
```bash
kubectl certificate approve <csr_name>
```

**Command 193:** Deny CSR
```bash
kubectl certificate deny <csr_name>
```

---

## 38. Plugin & Extensions

**Command 194:** List kubectl plugins
```bash
kubectl plugin list
```

**Command 195:** Get kubectl version with client/server details
```bash
kubectl version --short
```

---

## 39. Performance & Benchmarking

**Command 196:** Top pods sorted by CPU
```bash
kubectl top pods --sort-by=cpu
```

**Command 197:** Top pods sorted by memory
```bash
kubectl top pods --sort-by=memory
```

**Command 198:** Top nodes with details
```bash
kubectl top nodes --sort-by=memory
```

**Command 199:** Get all pods resource usage across namespaces
```bash
kubectl top pods -A --sort-by=memory
```

**Command 200:** Check container resource usage
```bash
kubectl top pod <pod_name> --containers
```

---

## Common Flags & Options

**Output formats:**
- `-o wide` - Additional columns
- `-o yaml` - YAML format
- `-o json` - JSON format
- `-o jsonpath` - Custom output using JSONPath
- `-o name` - Only resource names

**Common flags:**
- `-n <namespace>` - Specify namespace
- `--all-namespaces` or `-A` - All namespaces
- `-l key=value` - Filter by label
- `-w` or `--watch` - Watch for changes
- `--dry-run=client -o yaml` - Generate YAML without creating
- `-f <file>` - Specify file
- `--force` - Force operation
- `--grace-period=0` - Immediate deletion

---

## Quick Reference

### Get Information
```bash
kubectl get <resource>                    # List resources
kubectl get <resource> <name>             # Get specific resource
kubectl get <resource> -o wide            # More details
kubectl describe <resource> <name>        # Detailed info
kubectl logs <pod>                        # Container logs
kubectl top <resource>                    # Resource usage
```

### Create/Update/Delete
```bash
kubectl create <resource>                 # Create resource
kubectl apply -f <file>                   # Create/update from file
kubectl edit <resource> <name>            # Edit resource
kubectl delete <resource> <name>          # Delete resource
kubectl replace -f <file>                 # Replace resource
```

### Run & Execute
```bash
kubectl run <name> --image=<image>        # Create pod
kubectl exec <pod> -- <command>           # Execute command
kubectl exec -it <pod> -- /bin/bash       # Interactive shell
kubectl port-forward <pod> <local>:<pod>  # Forward port
```

### Scale & Rollout
```bash
kubectl scale <resource> --replicas=<n>   # Scale resource
kubectl rollout status <resource>         # Check rollout
kubectl rollout history <resource>        # Rollout history
kubectl rollout undo <resource>           # Rollback
```

---

## Practice Tips

1. **Start with basic get/describe commands** to understand your cluster
2. **Practice on your GKE nginx-1 deployment** - it's safe to experiment
3. **Use `--dry-run=client -o yaml`** to see what commands would create without actually creating
4. **Always check with `kubectl get` before deleting** to avoid mistakes
5. **Use `kubectl explain <resource>`** to learn about resource fields
6. **Combine with grep/awk** for powerful filtering: `kubectl get pods | grep Running`
7. **Master JSONPath** - incredibly powerful for scripting and automation
8. **Use kubectl diff** before applying changes to production
9. **Practice debugging** with ephemeral containers using `kubectl debug`
10. **Learn RBAC inside out** - critical for security interviews
11. **Understand the difference** between imperative and declarative approaches
12. **Practice writing complete manifests** from scratch, not just using generators
13. **Set up aliases** to speed up your workflow
14. **Use contexts effectively** to manage multiple clusters
15. **Learn to read events and logs** - essential for troubleshooting

---

## Resource Shortcuts

### Standard Shortcuts
- `po` = pods
- `deploy` = deployments
- `svc` = services
- `ns` = namespaces
- `no` = nodes
- `cm` = configmaps
- `sa` = serviceaccounts
- `rs` = replicasets
- `ds` = daemonsets
- `sts` = statefulsets
- `ing` = ingress
- `pv` = persistentvolumes
- `pvc` = persistentvolumeclaims
- `hpa` = horizontalpodautoscaler
- `netpol` = networkpolicies
- `pdb` = poddisruptionbudgets
- `cj` = cronjobs

Example: `kubectl get po` = `kubectl get pods`

### Additional Shortcuts
- `csr` = certificatesigningrequests
- `quota` = resourcequotas
- `limits` = limitranges
- `ep` = endpoints
- `ev` = events

### Using Multiple Shortcuts
```bash
kubectl get po,svc,ing,cm -n production
```

---

## Interview Q&A Scenarios

### Scenario 1: Pod stuck in Pending state
```bash
# Check pod events
kubectl describe pod <pod_name>

# Check node resources
kubectl top nodes

# Check if nodes are schedulable
kubectl get nodes

# Check if there are taints on nodes
kubectl describe node <node_name> | grep Taints

# Check resource quotas
kubectl get resourcequota -n <namespace>

# Check PVC status if using volumes
kubectl get pvc
```

### Scenario 2: Pod in CrashLoopBackOff
```bash
# Check logs
kubectl logs <pod_name>
kubectl logs <pod_name> --previous  # Logs from crashed container

# Describe pod for events
kubectl describe pod <pod_name>

# Debug with ephemeral container
kubectl debug <pod_name> -it --image=busybox

# Check liveness/readiness probes
kubectl get pod <pod_name> -o yaml | grep -A 10 livenessProbe

# Copy pod and change command to debug
kubectl debug <pod_name> --copy-to=debug-pod -it -- sh
```

### Scenario 3: Service not reachable
```bash
# Check service endpoints
kubectl get endpoints <service_name>
kubectl describe svc <service_name>

# Check if pods match service selector
kubectl get pods -l app=myapp
kubectl get svc <service_name> -o yaml | grep selector

# Test from within cluster
kubectl run test --rm -it --image=busybox -- wget -O- <service_name>:<port>

# Check network policies
kubectl get networkpolicy

# Check DNS resolution
kubectl run test --rm -it --image=busybox -- nslookup <service_name>
```

### Scenario 4: Node running out of resources
```bash
# Check node resources
kubectl top nodes
kubectl describe node <node_name> | grep -A 5 Allocated

# Find resource-heavy pods
kubectl top pods -A --sort-by=memory

# Check for evicted pods
kubectl get pods -A | grep Evicted

# Drain and cordon node
kubectl cordon <node_name>
kubectl drain <node_name> --ignore-daemonsets --delete-emptydir-data

# Scale down deployments if needed
kubectl scale deployment <name> --replicas=2
```

### Scenario 5: Deployment not rolling out
```bash
# Check rollout status
kubectl rollout status deployment <name>

# Check rollout history
kubectl rollout history deployment <name>

# Check replica sets
kubectl get rs

# Describe deployment
kubectl describe deployment <name>

# Check pod template hash mismatch
kubectl get pods --show-labels

# Pause and resume rollout
kubectl rollout pause deployment <name>
kubectl rollout resume deployment <name>
```

### Scenario 6: High cluster costs - need to optimize
```bash
# Find pods without resource limits
kubectl get pods -A -o json | jq '.items[] | select(.spec.containers[].resources.limits == null) | .metadata.name'

# Check resource usage vs requests
kubectl top pods -A
kubectl get pods -A -o custom-columns=NAME:.metadata.name,CPU_REQ:.spec.containers[*].resources.requests.cpu,MEM_REQ:.spec.containers[*].resources.requests.memory

# Find unused PVCs
kubectl get pvc -A --no-headers | while read ns name rest; do 
  kubectl get pods -n $ns -o json | jq -e ".items[].spec.volumes[]?.persistentVolumeClaim.claimName == \"$name\"" > /dev/null || echo "$ns/$name"
done

# Check for over-provisioned resources
kubectl top pods -A --sort-by=memory | head -20
```

---

## Kubernetes Best Practices

### Pod Design Best Practices

1. **Always set resource requests and limits**
```yaml
resources:
  requests:
    memory: "64Mi"
    cpu: "250m"
  limits:
    memory: "128Mi"
    cpu: "500m"
```

2. **Use liveness and readiness probes**
```yaml
livenessProbe:
  httpGet:
    path: /healthz
    port: 8080
  initialDelaySeconds: 30
  periodSeconds: 10

readinessProbe:
  httpGet:
    path: /ready
    port: 8080
  initialDelaySeconds: 5
  periodSeconds: 5
```

3. **Use meaningful labels and selectors**
```yaml
metadata:
  labels:
    app: myapp
    tier: frontend
    environment: production
    version: v1.2.3
```

4. **Don't use latest tag for images**
```yaml
# Bad
image: nginx:latest

# Good
image: nginx:1.21.6
```

5. **Use namespaces for isolation**
```bash
kubectl create namespace production
kubectl create namespace staging
kubectl create namespace development
```

### Security Best Practices

1. **Never run as root**
```yaml
securityContext:
  runAsNonRoot: true
  runAsUser: 1000
  fsGroup: 2000
```

2. **Use read-only root filesystem**
```yaml
securityContext:
  readOnlyRootFilesystem: true
```

3. **Drop unnecessary capabilities**
```yaml
securityContext:
  capabilities:
    drop:
      - ALL
    add:
      - NET_BIND_SERVICE
```

4. **Use network policies**
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: deny-all
spec:
  podSelector: {}
  policyTypes:
  - Ingress
  - Egress
```

5. **Use RBAC with least privilege**
```bash
# Create role with minimal permissions
kubectl create role pod-reader --verb=get,list --resource=pods

# Bind to specific user
kubectl create rolebinding read-pods --role=pod-reader --user=jane
```

6. **Scan images for vulnerabilities**
```bash
# Use tools like trivy, aqua, snyk
trivy image nginx:1.21
```

7. **Use secrets for sensitive data**
```bash
# Don't use ConfigMaps for sensitive data
kubectl create secret generic db-secret --from-literal=password=supersecret

# Mount as environment variable or volume
```

8. **Enable Pod Security Standards**
```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: production
  labels:
    pod-security.kubernetes.io/enforce: restricted
    pod-security.kubernetes.io/audit: restricted
    pod-security.kubernetes.io/warn: restricted
```

### Deployment Best Practices

1. **Use Deployments, not bare Pods**
```bash
# Good - self-healing, rolling updates
kubectl create deployment myapp --image=nginx:1.21

# Bad - no self-healing
kubectl run myapp --image=nginx:1.21
```

2. **Configure proper rollout strategy**
```yaml
spec:
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
```

3. **Use Pod Disruption Budgets**
```yaml
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: myapp-pdb
spec:
  minAvailable: 2
  selector:
    matchLabels:
      app: myapp
```

4. **Set up HPA for auto-scaling**
```bash
kubectl autoscale deployment myapp --cpu-percent=70 --min=2 --max=10
```

5. **Use anti-affinity for HA**
```yaml
affinity:
  podAntiAffinity:
    requiredDuringSchedulingIgnoredDuringExecution:
    - labelSelector:
        matchExpressions:
        - key: app
          operator: In
          values:
          - myapp
      topologyKey: "kubernetes.io/hostname"
```

### Resource Management Best Practices

1. **Set ResourceQuotas per namespace**
```yaml
apiVersion: v1
kind: ResourceQuota
metadata:
  name: compute-quota
spec:
  hard:
    requests.cpu: "10"
    requests.memory: 20Gi
    limits.cpu: "20"
    limits.memory: 40Gi
```

2. **Use LimitRanges for defaults**
```yaml
apiVersion: v1
kind: LimitRange
metadata:
  name: mem-limit-range
spec:
  limits:
  - default:
      memory: 512Mi
      cpu: 500m
    defaultRequest:
      memory: 256Mi
      cpu: 250m
    type: Container
```

3. **Monitor resource usage**
```bash
kubectl top nodes
kubectl top pods -A --sort-by=memory
```

### Operations Best Practices

1. **Always use labels for organization**
2. **Use health checks** - liveness and readiness probes
3. **Implement proper logging** - centralized logging solution
4. **Use GitOps** - Argo CD, Flux
5. **Regular backups** - etcd snapshots, velero
6. **Monitor everything** - Prometheus, Grafana
7. **Use admission controllers** - OPA, Kyverno
8. **Document resources** - annotations, README
9. **Version everything** - Git commit hashes in labels
10. **Test in staging first** - never test in production

---

## Common Pitfalls & Solutions

### Pitfall 1: Not setting resource requests/limits
**Problem:** Pod scheduling issues, resource starvation, node crashes  
**Solution:** Always set requests and limits
```yaml
resources:
  requests:
    cpu: "100m"
    memory: "128Mi"
  limits:
    cpu: "500m"
    memory: "512Mi"
```

### Pitfall 2: Using latest tag
**Problem:** Unpredictable deployments, version conflicts  
**Solution:** Use specific version tags
```yaml
# Bad
image: nginx:latest

# Good
image: nginx:1.21.6-alpine
```

### Pitfall 3: No health checks
**Problem:** Traffic sent to unhealthy pods  
**Solution:** Always configure probes
```yaml
livenessProbe:
  httpGet:
    path: /healthz
    port: 8080
readinessProbe:
  httpGet:
    path: /ready
    port: 8080
```

### Pitfall 4: Running as root
**Problem:** Security vulnerability  
**Solution:** Run as non-root user
```yaml
securityContext:
  runAsNonRoot: true
  runAsUser: 1000
```

### Pitfall 5: No resource quotas
**Problem:** One namespace consumes all cluster resources  
**Solution:** Set ResourceQuotas per namespace

### Pitfall 6: Forgetting to set DNS policy
**Problem:** Pod cannot resolve DNS  
**Solution:** Check dnsPolicy and dnsConfig

### Pitfall 7: Not using namespaces
**Problem:** All resources in default namespace, no isolation  
**Solution:** Use namespaces for environments and teams

### Pitfall 8: Imperative vs Declarative confusion
**Problem:** Configuration drift, hard to track changes  
**Solution:** Use declarative YAML files in Git
```bash
# Bad - imperative, no history
kubectl create deployment myapp --image=nginx

# Good - declarative, version controlled
kubectl apply -f deployment.yaml
```

### Pitfall 9: No Pod Disruption Budget
**Problem:** Maintenance takes down too many pods  
**Solution:** Create PDB
```yaml
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: myapp-pdb
spec:
  minAvailable: 1
  selector:
    matchLabels:
      app: myapp
```

### Pitfall 10: Not understanding networking
**Problem:** Service discovery failures  
**Solution:** Understand ClusterIP, NodePort, LoadBalancer, and DNS

---

## Key Differences (Interview Questions)

### Deployment vs StatefulSet vs DaemonSet

| Feature | Deployment | StatefulSet | DaemonSet |
|---------|-----------|-------------|-----------|
| Pod Identity | Random | Stable, ordered | Per node |
| Replicas | User defined | User defined | One per node |
| Storage | Ephemeral or shared PV | Stable PVC per pod | Typically host paths |
| Use Case | Stateless apps | Databases, queues | Monitoring, logging |
| Pod Names | Random suffix | Ordered (0, 1, 2) | Node-based |
| Scaling | Up/down freely | Ordered scale | Auto (node count) |
| Updates | Rolling | Ordered rolling | Rolling per node |

### Service Types

| Type | Purpose | When to Use |
|------|---------|-------------|
| ClusterIP | Internal only | Microservices communication |
| NodePort | External via node IP | Development, testing |
| LoadBalancer | External via cloud LB | Production external access |
| ExternalName | DNS alias | External service proxy |

### ConfigMap vs Secret

| Feature | ConfigMap | Secret |
|---------|-----------|--------|
| Purpose | Configuration | Sensitive data |
| Encoding | Plain text | Base64 |
| Encryption | No | Yes (with encryption at rest) |
| Size Limit | 1MB | 1MB |
| Use Case | App config | Passwords, tokens, keys |

### Probe Types

| Probe | Purpose | When Checked |
|-------|---------|--------------|
| livenessProbe | Is container alive? | Running |
| readinessProbe | Can container serve traffic? | Always |
| startupProbe | Has container started? | Startup only |

**Key Difference:** 
- Liveness failure → Container restarted
- Readiness failure → Removed from service endpoints
- Startup failure → After threshold, triggers liveness

### kubectl apply vs create vs replace

| Command | Behavior | Use Case |
|---------|----------|----------|
| create | Creates new resource, fails if exists | One-time creation |
| apply | Creates or updates (declarative) | GitOps, updates |
| replace | Deletes and recreates | Force update |

```bash
# create - fails if exists
kubectl create -f deployment.yaml

# apply - creates or updates (preferred)
kubectl apply -f deployment.yaml

# replace - deletes then creates
kubectl replace -f deployment.yaml --force
```

### Requests vs Limits

| Resource | Requests | Limits |
|----------|----------|--------|
| CPU | Guaranteed | Throttled if exceeded |
| Memory | Guaranteed | Killed (OOMKilled) if exceeded |
| Scheduling | Used for node selection | Not used |

**Best Practice:**
- **Requests:** What container needs minimum
- **Limits:** Maximum container can use

### Taint vs Toleration

- **Taint:** Applied to nodes to repel pods
- **Toleration:** Applied to pods to allow scheduling on tainted nodes

```bash
# Taint node
kubectl taint nodes node1 key=value:NoSchedule

# Pod must have toleration to schedule on node1
tolerations:
- key: "key"
  operator: "Equal"
  value: "value"
  effect: "NoSchedule"
```

### Affinity vs Anti-Affinity

- **Affinity:** Schedule pods together
- **Anti-Affinity:** Keep pods apart (HA)

### ClusterRole vs Role

| Feature | Role | ClusterRole |
|---------|------|-------------|
| Scope | Namespace | Cluster-wide |
| Resources | Namespaced | All resources |
| Use Case | Namespace access | Cluster admins |

---

## Production-Ready Deployment Example

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp
  namespace: production
  labels:
    app: myapp
    version: v1.2.3
    tier: frontend
  annotations:
    description: "My production application"
    git-commit: "abc123def456"
spec:
  replicas: 3
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  selector:
    matchLabels:
      app: myapp
  template:
    metadata:
      labels:
        app: myapp
        version: v1.2.3
        tier: frontend
      annotations:
        prometheus.io/scrape: "true"
        prometheus.io/port: "9090"
    spec:
      # Security
      securityContext:
        runAsNonRoot: true
        runAsUser: 1000
        fsGroup: 2000
        seccompProfile:
          type: RuntimeDefault
      
      # Service Account
      serviceAccountName: myapp-sa
      
      # Anti-affinity for HA
      affinity:
        podAntiAffinity:
          preferredDuringSchedulingIgnoredDuringExecution:
          - weight: 100
            podAffinityTerm:
              labelSelector:
                matchExpressions:
                - key: app
                  operator: In
                  values:
                  - myapp
              topologyKey: kubernetes.io/hostname
      
      # Containers
      containers:
      - name: myapp
        image: myregistry.io/myapp:1.2.3
        imagePullPolicy: IfNotPresent
        
        # Ports
        ports:
        - name: http
          containerPort: 8080
          protocol: TCP
        - name: metrics
          containerPort: 9090
          protocol: TCP
        
        # Environment
        env:
        - name: ENV
          value: "production"
        - name: DB_HOST
          valueFrom:
            configMapKeyRef:
              name: myapp-config
              key: db_host
        - name: DB_PASSWORD
          valueFrom:
            secretKeyRef:
              name: myapp-secret
              key: db_password
        
        # Resources
        resources:
          requests:
            cpu: "250m"
            memory: "256Mi"
          limits:
            cpu: "1000m"
            memory: "512Mi"
        
        # Health Checks
        livenessProbe:
          httpGet:
            path: /healthz
            port: 8080
          initialDelaySeconds: 30
          periodSeconds: 10
          timeoutSeconds: 5
          failureThreshold: 3
        
        readinessProbe:
          httpGet:
            path: /ready
            port: 8080
          initialDelaySeconds: 5
          periodSeconds: 5
          timeoutSeconds: 3
          failureThreshold: 3
        
        startupProbe:
          httpGet:
            path: /startup
            port: 8080
          initialDelaySeconds: 0
          periodSeconds: 10
          timeoutSeconds: 3
          failureThreshold: 30
        
        # Volume Mounts
        volumeMounts:
        - name: config
          mountPath: /config
          readOnly: true
        - name: cache
          mountPath: /cache
        
        # Security
        securityContext:
          allowPrivilegeEscalation: false
          readOnlyRootFilesystem: true
          capabilities:
            drop:
            - ALL
      
      # Volumes
      volumes:
      - name: config
        configMap:
          name: myapp-config
      - name: cache
        emptyDir:
          sizeLimit: 500Mi
      
      # Image Pull Secrets
      imagePullSecrets:
      - name: registry-secret
---
apiVersion: v1
kind: Service
metadata:
  name: myapp
  namespace: production
  labels:
    app: myapp
spec:
  type: ClusterIP
  selector:
    app: myapp
  ports:
  - name: http
    port: 80
    targetPort: 8080
    protocol: TCP
  sessionAffinity: None
---
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: myapp
  namespace: production
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: myapp
  minReplicas: 3
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
  - type: Resource
    resource:
      name: memory
      target:
        type: Utilization
        averageUtilization: 80
  behavior:
    scaleDown:
      stabilizationWindowSeconds: 300
      policies:
      - type: Percent
        value: 50
        periodSeconds: 15
    scaleUp:
      stabilizationWindowSeconds: 0
      policies:
      - type: Percent
        value: 100
        periodSeconds: 15
      - type: Pods
        value: 4
        periodSeconds: 15
      selectPolicy: Max
---
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: myapp-pdb
  namespace: production
spec:
  minAvailable: 2
  selector:
    matchLabels:
      app: myapp
---
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: myapp-netpol
  namespace: production
spec:
  podSelector:
    matchLabels:
      app: myapp
  policyTypes:
  - Ingress
  - Egress
  ingress:
  - from:
    - namespaceSelector:
        matchLabels:
          name: production
    - podSelector:
        matchLabels:
          tier: frontend
    ports:
    - protocol: TCP
      port: 8080
  egress:
  - to:
    - podSelector:
        matchLabels:
          app: database
    ports:
    - protocol: TCP
      port: 5432
  - to:
    - namespaceSelector: {}
    ports:
    - protocol: TCP
      port: 53
    - protocol: UDP
      port: 53
```

---

## Quick Command Combinations

### Get all resources in namespace
```bash
kubectl get all,cm,secret,ing,pvc -n production
```

### Delete all resources with label
```bash
kubectl delete all -l app=myapp
```

### Get all images in use
```bash
kubectl get pods -A -o jsonpath='{range .items[*]}{.spec.containers[*].image}{"\n"}{end}' | sort -u
```

### Get pods not running
```bash
kubectl get pods -A --field-selector=status.phase!=Running
```

### Restart all pods in deployment
```bash
kubectl rollout restart deployment myapp
```

### Export all resources to YAML
```bash
kubectl get all -o yaml > all-resources.yaml
```

### Find which pods are using most memory
```bash
kubectl top pods -A --sort-by=memory | head -20
```

### Get pod distribution across nodes
```bash
kubectl get pods -o wide --all-namespaces | awk '{print $8}' | sort | uniq -c
```

### Check all failed pods
```bash
kubectl get pods -A --field-selector=status.phase=Failed
```

### Force delete stuck pod
```bash
kubectl delete pod <pod_name> --grace-period=0 --force
```

### Get all pods with their QoS class
```bash
kubectl get pods -o custom-columns=NAME:.metadata.name,QOS:.status.qosClass
```

---

## Useful kubectl Aliases

Add these to your `~/.bashrc` or `~/.zshrc`:

```bash
alias k='kubectl'
alias kgp='kubectl get pods'
alias kgs='kubectl get svc'
alias kgd='kubectl get deployment'
alias kgn='kubectl get nodes'
alias kdp='kubectl describe pod'
alias kds='kubectl describe svc'
alias kdd='kubectl describe deployment'
alias kl='kubectl logs'
alias klf='kubectl logs -f'
alias kex='kubectl exec -it'
alias kctx='kubectl config current-context'
alias kns='kubectl config set-context --current --namespace'
alias kga='kubectl get all'
alias kgaa='kubectl get all --all-namespaces'
alias kdel='kubectl delete'
alias kapp='kubectl apply -f'
alias keti='kubectl exec -ti'
alias kcuc='kubectl config use-context'
alias kcgc='kubectl config get-contexts'
```

---

**Generated for:** Lead DevOps Architect Interview Prep  
**Cluster:** GKE Autopilot (qwiklabs-gcp-02-f6e122ad7a24)  
**Current Deployment:** nginx-1 (3 replicas)

**Interview Topics Covered:**
✅ 200 kubectl commands across 39 categories  
✅ RBAC (Roles, RoleBindings, ClusterRoles)  
✅ PersistentVolumes & PersistentVolumeClaims  
✅ Jobs & CronJobs management  
✅ Ingress resources  
✅ NetworkPolicy for security  
✅ HorizontalPodAutoscaler (HPA)  
✅ ResourceQuotas & LimitRanges  
✅ PodDisruptionBudgets for HA  
✅ **kubectl debug** (modern debugging)  
✅ Advanced JSONPath & custom columns  
✅ Patch & update strategies  
✅ **kubectl diff** for change preview  
✅ **Kustomize integration**  
✅ Wait conditions & timeouts  
✅ Certificate management  
✅ Performance benchmarking  
✅ **Interview Q&A scenarios** (6 real-world problems)  
✅ **Kubernetes best practices** (pod design, security, deployment, operations)  
✅ **Common pitfalls & solutions** (10 critical mistakes)  
✅ **Key differences** (Deployment vs StatefulSet, Service types, probes, etc.)  
✅ **Production-ready complete example** (Deployment + Service + HPA + PDB + NetworkPolicy)  
✅ **Useful kubectl aliases**  

**Modern Kubernetes Features (1.25-1.29):**
- kubectl debug with ephemeral containers
- Server-side apply
- Pod Security Standards
- HPA v2 with custom metrics
- PodDisruptionBudget v1
- NetworkPolicy improvements
- Advanced scheduling (affinity, topology spread)
- Resource management & QoS classes
