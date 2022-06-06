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


# Class for all actions
class EasyKube:
    def __init__(self):
        # Loading K8s config
        config.load_kube_config()

        # Setting client
        self.v1 = client.CoreV1Api()

    ## Services
    ### GET services from namespace
    def list_services(self):
        v1 = self.v1

        print("Listing services")
        request = v1.list_namespaced_service(NAMESPACE)
        for i in request.items:
            print("%s\t %s\t %s\t %s\t %s" % (i.metadata.name, i.spec.type, i.spec.cluster_ip, i.spec.external_i_ps, i.spec.ports))

    ## Pods
    ### GET all pods from namespace
    def list_pods(self):
        v1 = self.v1

        print("Listing pods with their IPs:")
        request = v1.list_namespaced_pod(NAMESPACE)
        for i in request.items:
            print("%s\t %s\t %s" % (i.metadata.name, i.status.phase, i.status.pod_ip))

# Main function
def main():
    mykube = EasyKube()
    
    mykube.list_services()

if __name__ == "__main__":
    main()
