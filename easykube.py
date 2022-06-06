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

# Main function
def main():
    mykube = EasyKube()


if __name__ == "__main__":
    main()
