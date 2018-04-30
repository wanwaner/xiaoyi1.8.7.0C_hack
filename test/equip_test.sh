#!/bin/sh

rm -f /etc/init.d/S50nochina

dr=`dirname $0`

# Enable telnet
echo "#!/bin/sh" > /etc/init.d/S88telnet
echo "telnetd &" >> /etc/init.d/S88telnet
chmod 755 /etc/init.d/S88telnet
#/home/init.sh

# Enable FTP
echo "#!/bin/sh" > /etc/init.d/S89ftp
echo "tcpsvd -vE 0.0.0.0 21 ftpd -w / &" >> /etc/init.d/S89ftp
chmod 755 /etc/init.d/S89ftp
tcpsvd -vE 0.0.0.0 21 ftpd -w / &

# Enable RTSP
cp -f /tmp/hd1/test/rtspsvr /home/rtspsvr


# Disable logo
echo -e "Disable logo YI"
#mv -f /home/hight_1555.bmp /home/hight_1555.bmp_
#mv -f /home/low_1555.bmp /home/low_1555.bmp_
cp -f $dr/logo/*.bmp /home/

# disconnected from china
#cp -f $dr/cloud /home/cloud
# /home/killapp.sh
#cp /home/cloudAPI /tmp/hd1/cloudAPI.bak
mv /home/cloudAPI /home/cloudAPI_real
cp /tmp/hd1/test/cloudAPI /home/cloudAPI
sync


# fix bootcycle
echo -e "Remove hd1/test/"

mv $dr/equip_test.sh $dr/equip_test-moved.sh
rm -rf $dr

reboot
