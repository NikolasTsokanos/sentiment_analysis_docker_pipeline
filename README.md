# Sentiment Analysis Docker Pipeline
Dockerized Pipeline of tweets using Twitter's API, MongoDB, PostgreSQL and Sentiment Analysis

## Project Description
In this project we created an ETL pipeline between two databases. First, we experimented with Twitter's API, where our text data (tweets) are being extracted from and stored directly in a NoSQL database (in our case MongoDB). The next step is a simple Extract-Transform-Load task (ETL job), whereby our data are being extracted from MongoDB, cleaned, transformed and analyzed based on positive or negative sentiment in order to be loaded into an SQL database (PostreSQL). In the last step, the most positive as well as the most negative score of each tweet (within a specific time interval) are being posted on the Slack-channel of our choice using a webhook-url from the built-in slackbot.

## How to Run
* Clone the whole repo locally on your machine
* Navigate from your (Bash) Terminal inside the project's main folder
* Locate and run the _compose.yml_-file with the following commands:
  * __docker-compose build__ _#Builds all containers_
  * __docker-compose up -d__ _#Runs everything in the background_
  * __docker stop $(docker ps - aq)__ _#Stops all containers_
  * __docker-compose down__ _#Deletes all containers_
 
 ## System Requirements
 Be aware of the following system requirements before deploying the pipeline:
 * latest version of Docker and Docker Compose
 * all the packages and toolkits listed in _requirements.txt_
  
