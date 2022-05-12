import pulumi_gcp as gcp
from pulumi import Config, export, get_project, get_stack, Output, ResourceOptions
from google.cloud import datastore

# Implicit auth to gcloud
client = datastore.Client()

# Read in some configurable settings for our cluster:
config = Config(None)

# max nodeCount is the max number of cluster nodes to autoscale out
MAX_NODE_COUNT = config.get_int('max_node_count')
# min nodeCount is the max number of cluster nodes to autoscale out
MIN_NODE_COUNT = config.get_int('min_node_count')
# nodeMachineType is the machine type to use for cluster nodes. Defaults to n1-standard-1 if unspecified.
# See https://cloud.google.com/compute/docs/machine-types for more details on available machine types.
NODE_MACHINE_TYPE = config.get('node_machine_type')
# username is the admin username for the cluster.
USERNAME = config.get('username') or 'admin'
# password is the password for the admin user in the cluster.
PASSWORD = config.get_secret('password')
# master version of GKE engine
MASTER_VERSION = config.get('master_version')
# make cluster private
PRIVATE_ENDPOINT = config.get('private_endpoint')
# make cluster private
PRIVATE_NODES = config.get('private_nodes')
# remove default node pool
REMOVE_DEFAULT_NODEPOOL_ENABLED = config.get('remove_default_nodepool') or True
# enable shielded nodes
SHIELDED_NODES_ENABLED = config.get('enable_shielded_nodes') or True

# Now, actually create the GKE cluster.
k8s_cluster = gcp.container.Cluster('gke-cluster',
    remove_default_node_pool=REMOVE_DEFAULT_NODEPOOL_ENABLED,
    enable_shielded_nodes=SHIELDED_NODES_ENABLED,
    initial_node_count=MIN_NODE_COUNT,
    min_master_version=MASTER_VERSION,
    private_cluster_config=gcp.container.ClusterPrivateClusterConfigArgs(
        enable_private_endpoint=PRIVATE_ENDPOINT,
        enable_private_nodes=PRIVATE_NODES,
        master_ipv4_cidr_block="172.18.0.0/28"
    ),
    master_authorized_networks_config=gcp.container.ClusterMasterAuthorizedNetworksConfigArgs(
        cidr_blocks=[
            {'cidr_block': "<your-IP>/32"}
        ]
    )
)

k8s_nodes = gcp.container.NodePool("primary-nodes",
    cluster=k8s_cluster.id,
    name="gke-demo-nodegroup",
    autoscaling=gcp.container.NodePoolAutoscalingArgs(
        max_node_count=MAX_NODE_COUNT,
        min_node_count=MIN_NODE_COUNT
    )
)
