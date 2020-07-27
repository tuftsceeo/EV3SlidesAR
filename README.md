# EV3SlidesAR

**Integration of EV3 Augmented Reality System with Google Slides Coding**  
Contributors: Lily Zhang, Andre Cleaver, Alina Shah, Olga Sans Cope  
Summer 2020  

Repo for EV3 augmented reality system: https://github.com/tuftsceeo/EV3Thoughts/tree/LegoEd/

Instructions for coding EV3 through Google Slides: https://drive.google.com/file/d/1yqYrCx2bQ6hMxkl2ObVRbWDFxM4uoFOU/view?usp=sharing

Google slides template: https://docs.google.com/presentation/d/1F9wScvcMDqt-sQjwLVM1ncjIpHjNE0NCfedytdSozZY/edit?usp=sharing

*To edit Google slides code, go to the top menu. Click on Tools, then Script Editor.*

## Requirements to view on Zoom application:
[UnityCam](https://github.com/mrayy/UnityCam)
1. Before using, access folder "RunMe First", access the target platform folder (x32,x64) which depends on the application you will use to view the virtual camera in. Right click on "Register.bat" and choose "Run as Administrator" to register UnityCam plugin in Windows. A window will appear to confirm that the plugin was successfully registered.

2. Inside unity, attach to the main camera the following component: UnityCam\Scripts\UnityCam.cs

3. Hit Play, now unity will stream whatever being rendered as a webcamera. You can use it in browser or any video capture program via the new camera UnityCam.

4. You might need to copy the contents within the UnitySample/Assets/ folder within your own Unity Assets folder. 

Check the included sample scene for a fully working example.

[Webcamoid](https://webcamoid.github.io/)
1. Download and install Webcamoid, this serves as a virtual webcam that you can select when using Zoom. By assigning UnityCam to the virtual webcam, users will see Unity's game window.

