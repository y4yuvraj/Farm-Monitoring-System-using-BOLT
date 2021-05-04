# Farm Monitoring System
A device that would help farmers to improve crop productivity.

<img src="https://drive.google.com/thumbnail?id=1KzEUAr7NRCK630tdVMUedJPSOMz5_0et">
---
goal: DESIGN A SYSYTEM FOR AGRICULTURE TO IMPROVE THE CROP PRODUCTIVITY.

## Introduction
A device that would help farmers to improve crop productivity by safeguarding the crops from intruder or fire by sending an alert to the farmer if someone tries to destroy the crops, also this will give real time feedbacks about the moisture in the soil along with temperature and amount of light which are essential for healthy crops.

## Working
Project has two functionality i.e. to give real time information to a farmer about moisture in soil, the amount of light and temperature also this project can alert farmer against a fire or a intruder trying to destroy crops. It is not easy for a farmer to manage farm all by himself also the factors like temperature and moisture cannot be measured easily and many others factors like animals, fire can destroy the crops this project will solve all these problems, we can detect sudden change in temperature and light(z-score analysis) and notify the farmer using message or e-mail, also in case of fire or an unwanted intruder we can send an alert to farmer if anomaly detected in temperature or an intruder tries to destroy crop.

## Demonstartion

### Alerts:
<img src="https://drive.google.com/thumbnail?id=1AhapbqPby41NydEyFsuST89Z2leUetJI">
<img src="https://drive.google.com/thumbnail?id=1_bmP3KrNKMwRIV59TUr5DVUN6ccpwAPi">

### Final Look:
<img src="https://drive.google.com/thumbnail?id=1W0xSeU9AteXJKOL5_mpJleAi81a0Cm83">
<img src="https://drive.google.com/thumbnail?id=17tczAXqNBw20EU7l-Z1FGl9prCa0TWG8">

## Process
1. Connect your Arduino to your computer and upload the plantproject.ino program to the Arduino using Arduino IDE(this is done because the cables for communication between bolt WIFI module and Arduino should not be connected before uploading this code ,cable used for communication can be identified easily it is labeled as Rx and Tx in both Arduino and BOLT WI-FI module)
2. Code for Sensors on Arduino IDE(plantproject.ino): There is a simple code in the folder where are calling Serial to run on 9600 baud rate. And then taking the input using analogRead() for pin A0 of Arduino.
3. now unplug the Arduino and make the connection.

## CONNECTIONS:

#NOTE: we can connect 5V and ground pin of Arduino to 5V and ground of BOLT WI-FI module to power BOLT WI-FI module using Arduino in this way we need only one power supply to power both Arduino and BOLT WI-FI module now we don't have to give supply to both, only one supply given to Arduino is enough through which our WI-FI module will be powered.



## Challenges!!
Thinking of a way to play these sounds and connecting the keyboard presses to these button.

## Accomplishments
Since this my first implementaion after the learning process i consider this as an achievement since learnig and application also tells about the progress we have made as a devoloper.

## Learning Process
Along with the practical implementation of HTML, CSS-BootStrap and JavaScript on a website, I learned to deploy a website using Github Pages and many event in javacript.


## Built With
* HTML
* CSS-BootStrap
* JavaScript

# What's next?
With this packed up my next goal is ReactJs and NodeJs.

