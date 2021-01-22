#!/bin/bash
scp -i ~/.ssh/id_rsa docker-compose.yaml jenkins@swarm-manager:/home/jenkins/docker-compose.yaml
ssh -i ~/.ssh/id_rsa jenkins@swarm-manager << EOF
    export DATABASE_URI=${DATABASE_URI}
    export AUTHOR=${AUTHOR}
    export app_version = 'v2'
    export rollback = 'false'
    export replicas = 10
    docker stack deploy --compose-file /home/jenkins/docker-compose.yaml character-generator
EOF