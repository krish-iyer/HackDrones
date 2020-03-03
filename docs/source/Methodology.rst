Methodology
===========

Drone Control firmware
``````````````````````
Drone will be flashed with a cleanflight firmware with added support for barometer(BMP280) and Magnetometer
(QMC5883L). The firmware can be flashed using cleanflight flight configrator chrome extention. The 
installation process for everythng related to the project will be discussed in detail in a seperate post 

Sensors
```````
As drone(SPRACINGEVOF3EVO brushed) doesn't have on board barometer and magnetometer support by default, some 
addition support for barometer(BMP280) and magnetometer(QMC5883L) has to be added to get assisted control 
over altitude and position control.

Network 
```````
The idea is to control multiple drones over a wireless network(WiFi). So for providing wireless network
support to the drones and to be able to communicate to GCS(Ground control station), we will be connecting
ESP8285 WiFi module with a custom firmware to the drone. Each of this module will be receiving the command
or request which then will be communicated to the drone over MSP(MultiWii Serial Protocol) although the
the packets recieved will be encoded according to the MSP Protocol so all WiFi module has to do is read
and write the following packets serially to the drone.

Formation control
`````````````````
To control position and altitude for every drone, first we need to make each drone distinctive and track
the object and it's IP address inorder to give right control commands to the right drone. 

We will make each drone distinctive with a different color and for object tracking we will be using OpenCV
where each color will be mapped to the corresponding IP address of the drone.


