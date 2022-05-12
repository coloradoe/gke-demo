#!/bin/sh

set -x

# Create a new Cloud NAT gateway so that our private nodes can
# communicate out to the internet
gcloud compute routers nats create gke-demo-gateway \
              --router=gke-demo-router \
              --auto-allocate-nat-external-ips \
              --nat-all-subnet-ip-ranges \
              --enable-logging