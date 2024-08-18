# k8s-Telaverge-Project

```markdown
# Kubernetes-Based Client-Server System with Auto-Recovery

## Project Overview

This project demonstrates a distributed system using Kubernetes, featuring a client and two servers. The system showcases inter-service communication, logging, and Kubernetes' auto-recovery capabilities.

Key features:
- Client sends alternating requests to two servers
- Servers log incoming requests and responses
- Kubernetes manages deployment and ensures high availability
- Auto-recovery demonstration when a server goes down

## Prerequisites

- Ubuntu 24.04 LTS
- Docker
- Kubernetes (kubeadm, kubelet, kubectl)
- Python 3.9+

## Setup Instructions

1. Install necessary tools:
   ```bash
   sudo apt update
   sudo apt install -y docker.io kubectl
   ```

2. Install Kubernetes components:
   ```bash
   sudo apt install -y kubeadm kubelet kubernetes-cni
   ```

3. Initialize the Kubernetes cluster:
   ```bash
   sudo kubeadm init --pod-network-cidr=10.244.0.0/16
   ```

4. Set up kubectl for your user:
   ```bash
   mkdir -p $HOME/.kube
   sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
   sudo chown $(id -u):$(id -g) $HOME/.kube/config
   ```

5. Install a network plugin (Flannel):
   ```bash
   kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml
   ```

## Project Structure

```
project/
│
├── client.py
├── server1.py
├── server2.py
├── Dockerfile.client
├── Dockerfile.server1
├── Dockerfile.server2
├── client-deployment.yaml
├── server1-deployment.yaml
└── server2-deployment.yaml
```

## Deployment Steps

1. Build Docker images:
   ```bash
   docker build -t client:v1 -f Dockerfile.client .
   docker build -t server1:v1 -f Dockerfile.server1 .
   docker build -t server2:v1 -f Dockerfile.server2 .
   ```

2. Apply Kubernetes configurations:
   ```bash
   kubectl apply -f client-deployment.yaml
   kubectl apply -f server1-deployment.yaml
   kubectl apply -f server2-deployment.yaml
   ```

3. Verify deployments:
   ```bash
   kubectl get deployments
   kubectl get pods
   kubectl get services
   ```

## Testing the System

1. Check pod logs to see client requests and server responses:
   ```bash
   kubectl logs <client-pod-name>
   kubectl logs <server1-pod-name>
   kubectl logs <server2-pod-name>
   ```

2. Verify server logs:
   ```bash
   kubectl exec <server1-pod-name> -- cat /app/server1.log
   kubectl exec <server2-pod-name> -- cat /app/server2.log
   ```

## Auto-Recovery Demonstration

1. Simulate a server failure:
   ```bash
   kubectl delete pod <server2-pod-name>
   ```

2. Observe Kubernetes recreating the pod:
   ```bash
   kubectl get pods
   ```

3. Check logs to confirm system recovery and continued operation.

## How It Works

1. The client sends "hello" requests to Server 1 (port 8080) and Server 2 (port 8081) alternately, with a 1-second delay between requests.
2. Each server responds with "hi" and logs the interaction with a timestamp.
3. Kubernetes manages the deployment and ensures each component is running.
4. If a server pod fails, Kubernetes automatically creates a new one to maintain the desired state.

## Troubleshooting

- If pods are stuck in "Pending" state, ensure the network plugin is correctly installed.
- For "ImagePullBackOff" errors, check if the Docker images are correctly built and accessible to the cluster.
- Use `kubectl describe pod <pod-name>` for detailed information on pod issues.
