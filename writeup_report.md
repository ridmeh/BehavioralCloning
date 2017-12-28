#Introduction
Driving car autonomously is a great learning oppurtunity to see how CNN can learn from images and certain parameters predict the behavior for next. I hre
Initial time was spent on 
#Data Collection
I began as suggested by collecting data using keyboard. When I looked at distribution of data, it was concentrated on 0 angle on steering. After reading on forum I reverted to data provided by udacity.
#Data Augumentation
 most of the suggestions ( except increasing contrast) ugument the data.  After reading lot in forums about the issue in collecting data using keyboard I switched to 
Finally, I 
#Model Architecture and Training Strategy
My first archictecture was simple one as described in class sessions. I


When steering angle is high I modified throttle in drive.py to slow down the car. I got this suggestion in some earlier forum and found to be very helpful.

Final model runs great with speed of 9. Car stays in the middle most of time and able to jump back when come close to sides.  

#Observations
1. Project which initially looked simple went very challanging when car would either move in circles or drive into woods. After following forum ( which is of immense help) I fixed most of the issues. After all trials, car would still not drive straight. I later learnt keras was using Theano backend and not TensorFlow. Once I switched to TensorFlow, car completed the entire track with no issues in one go. Amazing experience.
2. When, I switched on recoding I found car is not behaving good. It may be due to limited hardware. Thus, for recording I have reduced speed to 7.
#Future
I would like to explore more on what happens when Throttle , Speed and Steering all need to be predicted.
