#!/bin/sh

#get chrome driver

wget https://chromedriver.storage.googleapis.com/2.35/chromedriver_linux64.zip

mkdir -p ${PWD}/drivers && \
unzip chromedriver_linux64.zip && \
mv chromedriver ${PWD}/drivers

