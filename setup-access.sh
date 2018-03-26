#!/bin/bash
cat <<EOF > ~/.aws/credentials
[lydell-testing]
aws_access_key_id = $AWS_ACCESS_KEY_ID
aws_secret_access_key = $AWS_SECRET_ACCESS_KEY
EOF
cat <<EOF > ~/.aws/config
[profile lydell-testing]
output=json
region = ap-southeast-2
EOF
/entrypoint.sh
