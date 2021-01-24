# Random Character Generator Project - SFIA2
## Contents
* [Brief](#brief)
    * [Requirements](#requirements)
    * [My Approach](#my-approach)
* [Architecture](#architecture)
    * [Entity Diagram (Database Model)](#entity-diagram)
    * [CI Pipeline](#ci-pipeline)
* [Project Tracking](#project-tracking)
* [Usage of Version Control System](#version-control-system)
* [Evolution of Design & Process](#evolution)
* [Risk Assessment](#risk-assessment)
* [Testing](#testing)
    * [Unit Mock Test](#unit-test)
* [Front-End Design](#front-end-design)
* [Known Issues](#known-issues)
* [Future Improvements](#future-improvements)
* [Authors](#authors)
* [Aknowledgements](#aknowledgements)

## Brief

The main objective of this project is to make a web-based application that utilises create and read functions and does this through linking to three different APIs and uses those APIs to create a final product. This was all done through tools and methodologies we have learned in the previous weeks. 

### Requirements

To achieve the objective of the project, I aim to include the following:
* A project tracking board (Asana)
* Version Control System (GitHub) - with branches used effectively
* Jenkins Pipeline - Connected with a Jenkinsfile through GitHub
* A python-based web-application which utilises APIs and optimises practics and design principles
* Unit mock testing of the services of the application
* A basic front-end website, created using Flask
* Code integrated into a Version Control System which will be built through a Jenkins Pipeline and deployed to cloud-based virtual machines
* Jenkins Pipeline connected to Docker and Ansible to deploy web-application on an Nginx Load Balancer
* Ansible - To initiate a docker swarm

### My Approach

For this project I created an application where the user clicks a button that refreshes the page and generates a random character build for the user. This then creates a random character for the user to see and this satisfies the ‘create’ functionality criteria. The character has the following features: 
* *Name* 
* *Class* 
* *Item* 
* *Bonus Stats* 

 Also, the web page displays the five previous characters that were generated through an SQL table where the data is stored on an SQL VM instance. This feature satisfies the ‘read’ function of the criteria. 

## Architecture

### Entity Diagram (Database Model)
Displayed below is the Entity Diagram showing the table used and implemented into the code.

>![ED][ed]
>
> *Figure 1: Entity Diagram*

The entity diagram shows the data that is going to be stored from the application and to be read by the application.