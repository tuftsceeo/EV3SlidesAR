# EV3SlidesAR

**Integration of EV3 Augmented Reality System with Google Slides Coding**  
Contributors: Lily Zhang, Andre Cleaver, Alina Shah, Olga Sans Cope  
Summer 2020  

Repo for EV3 augmented reality system: https://github.com/tuftsceeo/EV3Thoughts/tree/LegoEd/

Instructions for coding EV3 through Google Slides: https://drive.google.com/file/d/1yqYrCx2bQ6hMxkl2ObVRbWDFxM4uoFOU/view?usp=sharing

Google slides template: https://docs.google.com/presentation/d/1F9wScvcMDqt-sQjwLVM1ncjIpHjNE0NCfedytdSozZY/edit?usp=sharing

*To edit Google slides code, go to the top menu. Click on Tools, then Script Editor.*

## Install
Sending and Receiving Messages with MQTT requied installing paho-mqtt on the EV3. More information can be found here with example code: https://www.ev3dev.org/docs/tutorials/sending-and-receiving-messages-with-mqtt/

`$ sudo pip3 install paho-mqtt`


## Requirements to view on Zoom application:
[UnityCam](https://github.com/mrayy/UnityCam)
1. Before using, access folder "RunMe First", access the target platform folder (x32,x64) which depends on the application you will use to view the virtual camera in. Right click on "Register.bat" and choose "Run as Administrator" to register UnityCam plugin in Windows. A window will appear to confirm that the plugin was successfully registered.

2. Inside unity, attach to the main camera the following component: UnityCam\Scripts\UnityCam.cs

3. Hit Play, now unity will stream whatever being rendered as a webcamera. You can use it in browser or any video capture program via the new camera UnityCam.

4. You might need to copy the contents within the UnitySample/Assets/ folder within your own Unity Assets folder. 

Check the included sample scene for a fully working example.

[Webcamoid](https://webcamoid.github.io/)
1. Download and install Webcamoid, this serves as a virtual webcam that you can select when using Zoom. By assigning UnityCam to the virtual webcam, users will see Unity's game window.
2. Within the "Configure Sources" tab at the bottom, select "UnityCam" as the active camera. Then go into Settings>Output and check off the Virtual camera box. Add a device to create the virtural camera that is linked to the UnityCam and give a name like "Unity_Cam_Feed".
3. Now hit the "Play" button which should now stream Unity's camera whenever you enter game mode. 
4. In Zoom, you should be able to see a new camera option, "Unity_Cam_Feed".

## Running Application
To run application, navigate to the CORPEV3 directory:
`$ cd CORPEV3/`

Run server.py:
`$ python3 server.py`
