#!/bin/bash

# Install Docker and Add Jenkins to group
curl https://get.docker.com | sudo bash
sudo usermod -aG docker jenkins

sudo -su jenkins
docker login 