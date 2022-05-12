#!/bin/sh

set -x

# nice to have, this is assuming you're on debian/ubuntu
sudo apt install kubectx

# assuming istioctl is installed
istioctl install

# NOTE: At this point we need to run src/gcloud/gcloud_istio_firewall_rule.sh

# switch to istio-system namespace to deploy gateway resource
kubens istio-system

# deploy gateway resource
kubectl apply -f httpbin-gateway.yaml

# create a new namespace for our sample app
kubectl create ns gke-demo

# switch to newly created namespace
kubens gke-demo

# label namespace to enable istio sidecar
kubectl label namespace default istio-injection=enabled

# deploy sample application
kubectl apply -f httpbin.yaml
