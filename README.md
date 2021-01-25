# Random Character Generator Project - SFIA2
## Contents
* [Brief](#brief)
    * [Requirements](#requirements)
    * [My Approach](#my-approach)
* [Project Tracking](#project-tracking)
* [Architecture](#architecture)
    * [Entity Diagram](#entity-diagram)
    * [CI Pipeline](#ci-pipeline)
* [Usage of Version Control System](#usage-of-version-control-system)
* [Evolution of Design and Process](#evolution-of-design-and-process)
    * [Usage of APIs in Service 1, 2, 3 and 4](#usage-of-apis-in-service-1-2-3-and-4)
    * [Testing](#testing)
        * [Unit Mock Test](#unit-mock-test)
    * [Build and Push](#build-and-push)
    * [Ansible](#ansible)
    * [Deploy](#deploy)
* [Risk Assessment](#risk-assessment)
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
* Deploy a rolling update with Docker Stack
* Set up a reverse proxy to the application

### My Approach

For this project I created an application where the user clicks a button that refreshes the page and generates a random character build for the user. This then creates a random character for the user to see and this satisfies the ‘create’ functionality criteria. The character has the following features: 
* *Name* 
* *Class* 
* *Item* 
* *Bonus Stats* 

 Also, the web page displays the five previous characters that were generated through an SQL table where the data is stored on an SQL VM instance. This feature satisfies the ‘read’ function of the criteria. 

## Project Tracking
The project tracking of this project was done by using Asana. You can find the link to the board used here: https://app.asana.com/0/1199599860779001/board
>![asana][asana]
>
> *Figure 4: Asana Board for Character Generator Project*

The Asana board has been designed such that tasks are moved from left to right. The boards displayed are listed as follows: 
* Product Backlog: These cards are a list of items that are needed to be completed for the project. 
* User Story: This card is the  user story that shows the functionality of the application. 
* Planning: These cards are a list of features that could have been included into the project and are in the ‘planning’ phase. 
* In progress: These cards are lists of items currently being worked on. 
* Testing: These cards are a list of items that are being tested.
* Finished: These cards are lists of processes that have been completed.

## Architecture

### Entity Diagram
Displayed below is the Entity Diagram showing the table used and implemented into the code.

>![ED][ed]
>
> *Figure 1: Entity Diagram*

The Entity Diagram in Figure 1 shows the data that is going to be stored from the application into an SQL table.

### CI Pipeline

Initial Pipeline
>![initpip][in-pip]
>
> *Figure 2: Initial CI Pipeline Diagram*
The initial pipeline shows NGINX was not initiated through Ansible and was created manually on a VM.

Updated Pipeline
>![cipipeline][ci-pip]
>
> *Figure 3: Updated CI Pipeline Diagram*

Figure 3 shows the continuous integration pipeline that is connected with the associated tools and services used within the structure. This structure shows the continuous deployment and continuous delivery of the whole system. The general structure is that I would be able to change my source code by pushing it in to a version control system, such as GitHub. Once this occurs the webhook connected between the Jenkins server and the GitHub repository will trigger everything that is scripted inside of the Jenkinsfile. 

The script starts off with a testing phase and this testing phase applies the plugins JUnit and Cobertura on the test unit code and produces test coverage reports. The next phase builds the images and pushes the new image to a DockerHub repository. Then the Ansible script file is ran and this initiates docker swarm onto the provided IP addresses. It also creates worker nodes which are then attached to the docker swarm. Ansible also installs NGINX on a virtual machine and links the NGINX to the swarm. 

Finally, the Jenkins pipeline initiates docker stack to deploy with docker compose, which takes the images from the DockerHub repository and installs the web application on the docker swarm. NGINX is the load balancer and users can connect to its IP address and view the application from there. 

In conclusion, the benefits of using this pipeline are that if there is an update for the web application it will then immediately be rolled into from the GitHub Repository into the Docker Swarm via all of the tools explained previously. This allows a continuous delivery as well as a continuous deployment, so that users can use the web application while it is being updated. Also, the rolling update is a quick way to update the application. 

## Usage of Version Control System
The version control system used in this project is GitHub in this project I used a development branch where I would push any changes of my code into that branch. I also branched out and made several feature branches used for the different components of this project. This allowed me to compare previous code to newly updated code.  

>![vcs][vcs]
>
> *Figure 5: Git Log Graph*

Figure 5 shows a section of commits made during the creation of the project and the branches used along with these commits. 

>![branchsection][branchsection]
>
> *Figure 6: GitHub Branches*

Figure 6 shows the different branches and active branches in the Version Control System.

The benefit of branches is that it allows you to see previous versions of your code just in case you would like to revert back and this is helpful as you may overwrite your previous code with an error or with a feature that is no longer wanted. 

## Evolution of Design and Process

### Usage of APIs in Service 1, 2, 3 & 4
The services in the application send information to each other through the use of APIs. They send a ‘request’ signal when they require the information from the particular service which then sends back to the requester through a ‘response’. APIs are useful as they store information and can be accessed by multiple languages. The APIs used in this application are JSON APIs. 

In this application, Service 2 and 3 contain an array list of information each and Service 4 uses the information from 2 and 3 via 1 to create a product which is then sent back to 1 for use.

>![bsv][bsv]
>
> *Figure 7: Pipeline Display showing all components of the Jenkinsfile*

From left to right the stages are:
* Declarative: Checkout SCM - Declares the Environment Variables
* Testing - Uses the test files provided with ```pytest```
* Build & Push - Builds Docker images and pushes to repository
* Config Management (Ansible)
* Deploy - Uses Docker Stack
* Declarative: Post Actions - Post Coverage Graphs

### Testing
To do my tests I used the following test files:
```python
service_1/tests/test_unit.py
service_2/tests/test_unit.py
service_3/tests/test_unit.py
service_4/tests/test_unit.py
```

I did the following to run my tests on Jenkins and to get the coverage reports:

* For Service 1:
```python
 cd service_1
 python3 -m pytest --cov=application --cov-report xml --cov-report term-missing --junitxml junit.xml
```

* For Service 2:
```python
 cd service_2
 python3 -m pytest --cov=application --cov-report xml --cov-report term-missing --junitxml junit.xml
```
* For Service 3:
```python
 cd service_3
 python3 -m pytest --cov=application --cov-report xml --cov-report term-missing --junitxml junit.xml
```
* For Service 4:
```python
 cd service_4
 python3 -m pytest --cov=application --cov-report xml --cov-report term-missing --junitxml junit.xml
```

This was all input into the ```test_script.sh``` file, which is ran through the Jenkinsfile.
####  Unit Mock Test
The unit mock test was done by using a Python library called ‘unittest.mock’. This library allows you to mock responses from components such as APIs. This is useful as it allows you to test services individually. 

The ‘pytest’ coverage mechanism shows us that all of the source code is being tested effectively. In Figure 7, you can see that the unit mock test for the source code has achieved 100% coverage. The picture below also shows a Cobertura graph of the coverage report and the common trend of the coverage for all of the lines of code tested beign 100%.
>![coverage][cov]
>
> *Figure 8: Cobertura Graph*

Figure 9 shows the test coverage of the previous builds.
>![testgraph][testgraph]
>
> *Figure 9: JUnit Graph*

Figure 10, 11, 12 and 13 show the coverage of each service individually.
>![s1test][s1test]
>
> *Figure 10: Service 1 Coverage Report*

>![s2test][s2test]
>
> *Figure 11: Service 2 Coverage Report*

>![s3test][s3test]
>
> *Figure 12: Service 3 Coverage Report*

>![s4test][s4test]
>
> *Figure 13: Service 4 Coverage Report*

The tests for Services 1, 2, 3 and 4 were done thorougly and checks if all information displays from each array.

### Build and Push
The Build & Push section shown in Figure 6 is where the ```Dockerfile``` for each section were initialised using the ```docker-compose.yaml``` file. This file built each image and pushed them into my DockerHub repository. The images are then going to be used at a later stage of the process. This stage also installed Docker on the Jenkins system and allowed Jenkins to perform the required stages with Docker.

Docker is the containerisation tool and is useful as it can be used on any operating system. 

### Ansible
Ansible was used to initialise the docker swarm onto a few virtual machines. This was done by installing ansible onto the Jenkins server and initialising the different roles such as installing docker onto each virtual machine, initialising the docker swarm see create a swarm manager and finally to initialise the swarm worker node attached with a join token to swarm manager. 

After the first creation of the application, I decided to refactor my code. Initially I had to create an NGINX instance manually, but then I added another role to my ansible configure file to install NGINX on a separate virtual machine each time a new build is created on Jenkins. This allowed me to automate the NGINX installation on other virtual machines, just in case the previous virtual machine containing NGINX is deleted or has an error. 

### Deploy
The deploy section of the pipeline initialised the docker compose onto the swarm. This utilised the ```docker stack deploy``` function allowing the developer to make a rolling update across multiple services. Docker Stack is used to make several containers that are all based on the same image to provide high availability. The rolling update is beneficial as it means the users will experience hardly any downtime while the application is being updated, so both the old and the new version will be accessible until the new version has been fully rolled out across the whole docker swarm.

## Risk Assessment
The Risk Assessment for this project is displayed below. The view this in full click this link: https://docs.google.com/spreadsheets/d/1K0oOe0WRTf1r99D3WdDTF6l_0dBxpTVbylfzUqmbzY0/edit?usp=sharing
>![rsa1][rsa1]
>
> *Figure 14: Risk Assessment for Character Generator Project*

## Front-End Design
The Front-End design displays what the user will see upon visiting the site. This is built with very simple HTML but is functional and works within reason.
>![cgp][design]
>
> *Figure 15: The Front-End Design of the Project*

## Known Issues
* Random 'Max Retries' error which can be caused when the refresh button is clicked multiple times quickly.

## Future Improvements
There are a number of improvements I would like to add to this application if there was more time:
* Add a 'Stats' table which links to the 'Characters' table and shows all the stats of the randomly generated character.
* Add images for the seperately generated characters.
* Add a potential scoreboard which shows who has had the best randomly generated characters in terms of stats.

## Author
Naserul Islam

## Aknowledgements

* Harry Volker

[ed]: https://i.imgur.com/VJ7yjuv.png
[ci-pip]: https://i.imgur.com/QymS1EC.png
[asana]: https://i.imgur.com/a5PHVQw.png
[vcs]: https://i.imgur.com/rW4CccT.png
[branchsection]: https://i.imgur.com/MNUXuBV.png
[cov]: https://i.imgur.com/veEnCjV.png
[testgraph]: https://i.imgur.com/lCAPJug.png
[s1test]: https://i.imgur.com/UGiyYqB.png
[s2test]: https://i.imgur.com/RzYOo0v.png
[s3test]: https://i.imgur.com/OS43jGl.png
[s4test]: https://i.imgur.com/RbkA64U.png
[bsv]: https://i.imgur.com/SmwkTo5.png
[rsa1]: https://i.imgur.com/DU8URDY.png
[design]: https://i.imgur.com/tQzlpkj.png
[in-pip]: https://i.imgur.com/uMtDS3Q.png
