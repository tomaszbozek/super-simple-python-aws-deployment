# Super simple python deployment to aws cloud using aws beanstalk

## Requirements
- python 3.12
- aws account
  
## Problems
- AWS beanstalk changed to templates deployment usage: https://repost.aws/questions/QUcX9TipxqSGeM5G7RORmqoQ/new-account-recently-created-unable-to-create-environments-on-elastic-beanstalk-launch-configuration-error
normal creation of environment along with application in AWS beanstalk does not work (at least for me)

- in .ebextensions I added proper configuration which has to be deployed as whole library '.zip' with python, requirements during the creation of environment

- another problem is that deployment was using python 3.9 and environment was using 3.12, it will be solved after transition to docker
  now it was fixed by adding appropriate libraries in requirements.txt

 ## TODO
 - support production and gunicorn
 - add production environment variable for flask
