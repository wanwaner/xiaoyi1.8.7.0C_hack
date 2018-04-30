# xiaoyi1.8.7.0C_hack


Support telnet,tftp,rtsp,no logo.

Clone this repository on a computer，

Then, format a micro SD card in fat32 format and copy the content of the folder at the root of your memory card.

If plugged, unplug the Yi camera
Insert the memory card in the Yi camera
Plug the Yi camera
The camera will start. The led will indicate the current status :

yellow : camera startup
blue blinking : network configuration in progress (connec to wifi, set up the IP address)
blue : network configuration is OK. Camera is ready to use.

telnet username/password :  root/1234qwer

RTSP server is on port 554.

You can access the video over RTSP on 3 urls :

High definition video and audio (h264) : http://ip:554/ch0_0.h264
Low definition video and audio (h264) : http://ip:554/ch0_1.h264
Audio (h264) : http://ip:554/ch0_3.h264
