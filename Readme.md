# Protected Planet Esri

Protected Planet Esri Services

## Requirements
This is a Python 2.7 project that is testes to run on Windows Server 2008 and ArcGIS Server 10.1.
It gets a WDPA file geodatabase from S3 and replaces the existing one. Then it recreates the tile cache.

## Installation
This is a python 2.7 project. You should have python and pip installed.
We have a requirements.txt file with all the requirements.
Please run the following command to install:

```
pip install -r requirements.txt
```

#S3 secret file
There should be a s3.yaml file in the config directory.
Change the s3_example.yaml file to access your own S3 bucket.



##Run


#First time

You should run:

```
python create_service.py
```

This will generate a .sd file with the service definition and starts a service for this ArcGIS server.

#Monthly Updates

You should run the monthly_update file in the src directory

```
python monthly_update.py
```

This task should do every month. We can set it to run automatically doing the following steps:

Open control panel, click Administrative and Schedule Tasks.
Click Task Scheduler > Create Task and set Trigger (when top run) and Action (set path to monthly_update.py).