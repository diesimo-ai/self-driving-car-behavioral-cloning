# Overview

![sim](https://user-images.githubusercontent.com/36713637/189908895-2d655b52-e59c-4930-80cf-e9d5cc410dde.png)


This is a full self-driving car simulator based on Computer Vision and [NVIDIA CNN model for Self-driving car](https://github.com/afondiel/full-self-driving-car-simulation/tree/main/doc)

I ran Udacity self-driving car simulator intended for NanoDegree program (for Self-driving Engineer) to collect training data

After training the NVIDIA machine learning model with the collected data I save the model (you can modify the model to increase its accuracy)

Finally I run the simulator in autonomy to clone the self-driving behavior based on the pretrained model but on real time test dataset  

# Requirements tools

- python3
- [Udacity self-driving car simulator download repo](https://github.com/udacity/self-driving-car-sim)
- keras
- opencv
# Libraries

Install the required libaries by running the script below 
- on linux
```bash
./run_setup.sh
```
- on windows
```batch
.\run_setup.bat
```
# Usage 

To run the app :
- on linux 

```bash
./run_app.sh
```
- on windows 
```batch
.\run_app.bat
```

# Contribution 
Be free to reach me and pull request. Ideas worth spreading ;) 
# Output files

*.log :log files

> "As soon as it works, no one calls it AI anymore." 
>
> — John McCarthy (AI effect)
