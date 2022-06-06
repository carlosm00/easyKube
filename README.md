# easyKube

CLI python application for Kubernetes (K8s) easy deployment and management.
This repository uses the functionalities of [Python Kubernetes-client](https://github.com/kubernetes-client/python/tree/master/kubernetes) to interact with Kubernetes' API.

# Features
- Open Source
- Python-based full CLI application
- Automatic deployment
- Legacy Kubernetes (k8s)

# Services to deploy
- Web servers
	- Ngix
	- Apache
- Database servers
	- MySQL
	- Redis

# Repository content
## Templates
This is the templates directory, listed in sub-folders for each service listed above. 
The full list of files is described on the table below:

| File		                     | Decription                      |
| :----------------------------  | :------------------------------ |
| apache_deployment              | Deployment template file        |
| apache_service                 | Service template file           |
| nginx_deployment               | Deployment template file        |
| nginx_service                  | Service template file           |
| mysql_deployment               | Deployment template file        |
| mysql_service                  | Service template file           |
| mysql_persistentvolume         | Persisten Volume template       |
| mysql_persistentvolumeclaim    | Persisten Volume claim template |
| mysql_secret_creation          | Service secrets template        |
| redis_deployment               | Deployment template file        |
| redis_service                  | Service template file           |