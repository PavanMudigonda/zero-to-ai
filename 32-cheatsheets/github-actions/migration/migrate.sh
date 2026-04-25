#!/bin/bash


gh actions-importer audit jenkins \
    --jenkins-instance-url https://localhost:8080 \
    --jenkins-username admin \
    --jenkins-access-token ${JENKINS_ACCESS_TOKEN} \
    --github-access-token ${GITHUB_ACCESS_TOKEN} \
    --output-dir audit-dir