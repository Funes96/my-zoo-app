#!/bin/bash

if [ ! -d "zoo-amit" ]; then
  echo "Cloning application from GitHub..."
  git clone https://github.com/Funes96/my-zoo-app.git
else
  echo "Pulling latest changes from GitHub..."
  cd zoo-amit
  git pull
fi

cd zoo-amit

echo "Starting application with Docker Compose..."
docker-compose up -d

echo "Application is running at http://localhost:8000"