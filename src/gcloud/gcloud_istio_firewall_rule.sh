#!/bin/sh

# For private GKE clusters
# An automatically created firewall rule does not open port 15017.
# This is needed by the Pilot discovery validation webhook.
gcloud compute firewall-rules list --filter="name~gke-gke-cluster-703226a-[0-9a-z]*-master"
gcloud compute firewall-rules update gke-gke-cluster-703226a-f54cb7cc-master --allow tcp:10250,tcp:443,tcp:15017