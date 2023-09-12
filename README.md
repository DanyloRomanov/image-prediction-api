# image-prediction-api

# Local run commands:
## dockerize
docker build -t image-detection-app . 
docker run  -p 80:80 image-detection-app

# Run in heroku
 ### logs
 heroku logs --tail

 ### set remote
 heroku git:remote picture-detection-app

 ### set contailer
 heroku stack:set container

 ### start
 git push heroku main

