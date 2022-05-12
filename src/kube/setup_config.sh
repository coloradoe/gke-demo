#!/bin/sh

set -x

# nice to have, this is assuming you're on debian/ubuntu
sudo apt install kubectx

# assuming istioctl is installed
istioctl install

# For private GKE clusters
# An automatically created firewall rule does not open port 15017.
# This is needed by the Pilot discovery validation webhook.
gcloud compute firewall-rules list --filter="name~gke-gke-cluster-703226a-[0-9a-z]*-master"
gcloud compute firewall-rules update gke-gke-cluster-703226a-f54cb7cc-master --allow tcp:10250,tcp:443,tcp:15017

# switch to istio-system namespace to deploy gateway resource
kubens istio-system

# deploy sample gateway resource
kubectl apply -f httpbin-gateway.yaml

# create a new namespace for our sample app
kubectl create ns gke-demo

# switch to newly created namespace
kubens gke-demo

# label namespace to enable istio sidecar
kubectl label namespace gke-demo istio-injection=enabled

# deploy sample application
kubectl apply -f httpbin.yaml
