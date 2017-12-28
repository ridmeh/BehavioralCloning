#Introduction

Driving car autonomously is a great learning oppurtunity to see how CNN can learn from images with certain parameters and predict the behavior for next move.

#Data Collection
I began as suggested by collecting data using keyboard. When I looked at distribution of data, it was concentrated on 0 angle on steering. It did not make sense to move further with such a skewed data. After reading on forums I realized it is very hard to collect good data using keyboard. I reverted to use data provided by udacity.

#Data Augumentation
Data provided by udacity was good but need augumentation. I attempted below augumentation with which model worked really well.
-Flipping Images & Sterring measurements
-Cropping
-Removed ALL zeros


#Model Architecture and Training Strategy
My first archictecture was simple one as described in class sessions. I chose AWS to train the system. I tried Nvidia architecture to run smoother then couple of models that I trained earlier with. Final model runs great with speed of 9. Car stays in the middle most of time and able to jump back when come close to sides.  

#Automation testing
When steering angle is high I modified throttle in drive.py to slow down the car. I got this suggestion in some earlier forum and found to be very helpful.

#Observations
1. Project which initially looked simple went very challanging when car would either move in circles or drive into woods. After following forum ( which is of immense help) I fixed most of the issues. After all trials, car would still not drive straight. I later learnt keras was using Theano backend and not TensorFlow. Once I switched to TensorFlow, car completed the entire track with no issues in one go. Amazing experience.
2. When, I switched on recoding I found car is not behaving good. It may be due to limited hardware. Thus, for recording I have reduced speed to 7.
#Future
I would like to explore more on what happens when Throttle , Speed and Steering all need to be predicted.
