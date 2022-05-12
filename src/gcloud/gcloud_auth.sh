#!/bin/sh
set -e

# Set our project as current project
gcloud config set project gke-demo-2092afn3wfn49sn20

# auth to gcp
gcloud auth application-default login

gcloud components update
