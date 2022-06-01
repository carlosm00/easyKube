"""

EasyKube

CLI python application for Kubernetes (K8s) easy deployment
and management with debug-level logs.
YAML templates are stored on the templates folder.

Library importation
"""

from __future__ import print_function
import sys
import logging
import os
import json
import yaml
import time
from os import listdir
from kubernetes import client, config
from kubernetes.client.rest import ApiException

# Default namespace will be easykube
NAMESPACE = "easykube"


# Action Function list
## List Pods from namespace
def list_pods():
    print("Listing pods with their IPs:")
    request = v1.list_namespaced_pod(NAMESPACE)
    for i in request.items:
        print("%s\t%s\t%s\t%s\t%s" % (i.metadata.name, i.status.pod_ip,
                              i.metadata.namespace, i.metadata.name, i.status.phase))

## List Deployments
def list_deployments():
    print("Listing deployments:")
    request = v1.list_namespaced_deployment(NAMESPACE, pretty=True, timeout_seconds=3, watch=False)
    print(request)

## 

# Main function
def main():
    # Loading K8s config
    config.load_kube_config()

    # Setting client
    v1 = client.CoreV1Api()


if __name__ == "__main__":
    main()
