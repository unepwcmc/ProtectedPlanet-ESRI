# Protected Planet Esri

Protected Planet Esri Services

## Setup
This application is built to be run on a EC2 ESRI instance. It uses ArcPy library.


## Installation
This is a python 2.7 project. You should have python and pip installed.
We have a requirements.txt file with all the requirements.
Please run the following command to install:

...
pip install -r requirements.txt
...

##S3 secret file
There should be a s3.yaml file in the config directory.
Change the s3_example.yaml file to access your own S3 bucket.

## Create service
We have setup a mxd base file and a draft service definition. You can create your service running src\stup_esri\create_service.py