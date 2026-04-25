#!/bin/bash

for file in $(find . -name *Jenkinsfile*); do
    echo "migrating $file to github actions"
    gh actions-importer dry-run jenkins \
    --source-file-path "$file" \
    --output-dir "./migration-output-$(basename $file)"
done;