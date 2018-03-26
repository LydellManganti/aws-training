# Local Machine requirements
- docker ce installed
- python 2.7 and pip installed

# How to setup local machine for development
1. Clone https://github.com/lydell.manganti/lydell-aws-training.git
2. Add aws access key and secret in ~/.aws/credentials
Add the "lydell-testing" profile because the application will look for this profile name.
Please replace the access key and secret access key related to your aws account.
```
[lydell-testing]
aws_access_key_id = ABDEFGHJIKLMN
aws_secret_access_key = AB1234Bdfd44rka99sdfjakfjwpfsfowDDD
``` 
3. Add region settings in ~/.aws/config
Add the "profile lydell-testing" profile because the application will look for this profile name.
Please replace the region related to your aws account.
```
[profile lydell-testing]
output=json
region = ap-southeast-2
```

# How to run application locally
1. Follow steps to setup local machine
2. Change directory to the root folder of the application
3. Run 
```
./setup.sh
```
4. Run 
```
source ./.venv/app/bin/activate
```
5. Run 
```
./run-app.sh
```
6. Navigate to url http://localhost:5000

# How to run Test suite locally
1. Follow steps to setup local machine
2. Change directory to the root folder of the application
3. Run 
```
./run-tests.sh
```

# How to build image locally
1. Follow steps to setup local machine
2. Change directory to the root folder of the application
3. Run
```
docker build --tag [image_name] .
```

# How to run container from the image built locally
1. Follow steps to build image locally and take note of the image id to be used below.
2. Run
```
docker run -i -p 80:80 -e AWS_ACCESS_KEY_ID=yourkey_aws_access_key -e AWS_SECRET_ACCESS_KEY=your_aws_secret_access_key [image_id]
```
3. Navigate to url http://localhost:80


Please note difference of port numbers when running locally and running docker container
========================================================================================
