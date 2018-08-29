# trafflickr

Project for HackGSU Fall 2017
https://devpost.com/software/trafflickr-uhpk51

## Inspiration
Most of us have our lives thick in the hubbub of Atlanta city life. But with such a lively city comes even livelier traffic. How to alleviate this problem? Well the first step to solving any problem is to first watch and analyze.

## How it Works
User can input a date and time and then the street camera and real-time video footage will pull up from the SmartCity API and allow you to see the current traffic on certain streets and times of the day. With Google's object detection API, we are somewhat able to track what different objects are and classify them, such as cars.

## How it's built
We used GE CityIQ API to retrieve the video data. We used Google TensorFlow Object Detection API to analyze the footage and classify the objects in it.
