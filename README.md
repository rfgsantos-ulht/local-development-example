# Local Development Example

## Introduction

In this repository you will find a working example of local development with aid of Nginx Reverse Proxy along with some instructions and recommendations for you application development and deployment in DEISI Projects Server.

The structure presents as it follows:

```
├── README.md
├── docker-compose.yml
├── templates
├── gateway
│   ├── Dockerfile
│   ├── multimedia
│   ├── nginx.conf
│   └── prod.conf
└── sample-django
    ├── Dockerfile
    ├── manage.py
    ├── mysite
    ├── mywebsite
    └── requirements.txt
```

**gateway** - Nginx Reverse Proxy configurations for a dummy local development.

**sample-django** - Sample Django application with the necessary configurations for future deployments.

**templates** - In here you will find some of the resources that you can use for your local development.

## Templates

The folder templates provides you with some files you can use to create your own configurations for future deployment.
Before using any of these files, you must evaluate if any of these use cases match your own:

* You want to deploy a Full Stack application (Frontend + Backend)
    * React JS + Spring Boot
    * Next JS + Spring Boot

* You want to deploy a Backend application 
    * PHP 
    * Django

* You have a Mobile Application with a Backend server (In here you only deploy the backend server)
    * Flutter + Spring Boot
    * iOS + Spring Boot
    * Android + Spring

* You have a Progressive WebApp
    * Ionic
    * Flutter

### Considerations

After successfully identifying any of the use cases matching your own, there are a few steps you need to take into account and starting to define, such as:

* You must know you TFC/Application identifier - Usually this has the format of:
    * DEISI50
    * G120
    * TFC30

* Your application must be capable to be adaptative to the environment it runs, where it is in your machine, a server or Docker. This requires to pay attention to some details:
    * If your application uses any kind of database, this should be modifiable.
    * If it uses any kind of secrets, make sure to keep them hidden.
    * If it has any kind of automated mechanisms of security, like CSRF, CORS, make sure you have compatibility with the domain:
        * https://projects.deisi.ulusofona.pt/
    * If your application has any kind of dependencies, make sure they are easily downloadable.

* Make sure it is possible to be ran behind a Reverse Proxy.

## Automations

The server is currently placing automations of deployment based in your Github repository. 
For this to be configured for your project, you must have all previous considerations tackled in your application development.

The CI/CD pipeline is configured with the following steps:

- Instalation of a Github App developed by Lusofona
- You configure the repository branch you wish to be listened to through a small app developed by Lusofona
- Configure the namespace that is going into the path , for instance: https://projects.deisi.ulusofona.pt/mynamespace
- After the deployment is triggered, it will search for a ```docker-compose.yml``` in the project root
- Deploy will happen in the server soon! You will be able to view the logs of the containers for better debugging

To access all of the resources above, you must send me an email with all information, but only after you verify that it is working locally. 


## Final 

Any questions related with the documentation or if you need any help with Docker, I'm very happy to help. 
Send me an email with your question: rui.filipe.santos@ulusofona.pt

