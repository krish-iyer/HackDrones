Introduction
============

This documentation will help you in building a good foundation of a drone network with which you can implement
various swarm control algorithms(specific to drones). This will be an easy guide to wireless control of drones 
and bit of manupulation of low level network bindings. 

For testing and demonstration I will be using a FC(flight controller) which will be supported by cleanflight
configurator so that we needn't worry about atleast control part. The idea here is to first setup the usual
drone in the flight state and then tear bit by bit and include more custom code. For example there's a very
good tutorial on to `fly a drone a drone using an android app <https://www.instructables.com/id/Build-a-WiFi-Enabled-Micro-quadrotor/>`_.

If you somehow missed to follow the above mentioned link, I can help you with the few of the details here. The
controller being used is SPRACINGF3EVO and please make sure that you opt controllers for brushed motor rather
than brusless motor. In case of brushless motors you required to have ESCs(Electronic Speed Controllers) and
bigger batteries so just to make it more safe and stable let's opt for brushed controller. Anyway all the 
methodologydicussed in the documentation will work on both brushed and brushless controllers.

Once you get the FC board in your hand, you need to fash it will some kind of progrm which can take care of 
control signals to drive the motor and also the various sensors value like accelerometer and gyro. In case if 
you don't have prior knowledge in flight control algorithms and ARM M series MCUs, cleanflight is a good 
solution for getting your flight ready with few clicks.

Details regarding WiFi module would be discussed in detail in upcoming posts, once we are done with setting up 
the WiFi, we can very well control drone with anything that can send signal over WiFi be it an android phone or
a PC. 

**Hardware Specification**

- FC(flight controller) - **SPRACINGF3EVO**
- WiFi module - **ESP8285** or **ESP8266**
- Barometer - **BMP280**
- Magnetometer - **QMC5883L**