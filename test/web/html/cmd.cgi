#!/bin/sh

########################################
# Функции
########################################


setTZ(){
  TZ=`echo "$QUERY_STRING" | grep -oE "(^|[?&])tz=[^&]+" | sed "s/%20/ /g" | cut -f 2 -d "=" | sed -e 's/  *$//'`
  
  echo "Зона UTC $TZ<br>"

  TZtoSet=$((8-TZ))

  if [ $TZtoSet -gt 0 ]; then
      TZValue="GMT+$TZtoSet"
      #echo "TZValue=$TZValue"
  else
      TZValue="GMT$TZtoSet"
      #echo "TZValue=$TZValue"
  fi

  echo $TZValue > /etc/TZ && echo "Временная зона изменена успешно.<br>" || echo "ОШИБКА записи временной зоны.<br>";htmlfooter

}


setFTP(){

  _ftp=`echo "$QUERY_STRING" | grep -oE "(^|[?&])ftp=[^&]+" | sed "s/%20/ /g" | cut -f 2 -d "=" | sed -e 's/  *$//'`
  
  case "$_ftp" in
    on )
      echo "Включаем FTP.<br>"
      echo "Добавляем в автозагрузку<br>"
      echo "#!/bin/sh" > /etc/init.d/S89ftp && echo "/etc/init.d/S89ftp создан успешно.<br>" || echo "ОШИБКА создания /etc/init.d/S89ftp.<br>"
      echo "tcpsvd -vE 0.0.0.0 21 ftpd -w / &" >> /etc/init.d/S89ftp
      echo "Изменяем права файла<br>"
      chmod 755 /etc/init.d/S89ftp && echo "Права изменены.<br>" || echo "ОШИБКА изменения прав /etc/init.d/S89ftp.<br>"
      echo "Запускаем FTP.<br>"
      tcpsvd -vE 0.0.0.0 21 ftpd -w / &
      echo "FTP включен успешно.<br>"
      #echo "Для завершения перезагрузите камеру.<br>"
    ;;
    
    off)
      echo "Выключаем FTP.<br>"
      echo "Убиваем процесс.<br>"
      #ps | grep /home/watch_process | grep -v "grep" | awk '{print $1}' | xargs kill -9
      #killall -9 tcpsvd
      pidof tcpsvd | xargs kill -9
      echo "Убираем из автозагрузки.<br>"
      rm /etc/init.d/S89ftp && echo "FTP выключен успешно.<br>" || echo "ОШИБКА удаления /etc/init.d/S89ftp.<br>"
    ;;
    
    * )
      echo "<h3>ERROR! Неверный параметр для FTP.</h3>"
    ;;
  
  esac


}

setTELNET(){

  _telnet=`echo "$QUERY_STRING" | grep -oE "(^|[?&])telnet=[^&]+" | sed "s/%20/ /g" | cut -f 2 -d "=" | sed -e 's/  *$//'`

  case "$_telnet" in
    on )
      echo "Включаем telnet.<br>"
      echo "Добавляем в автозагрузку<br>"
      echo "#!/bin/sh" > /etc/init.d/S88telnet && echo "/etc/init.d/S88telnet создан успешно.<br>" || echo "ОШИБКА создания /etc/init.d/S88telnet.<br>"
      echo "telnetd &" >> /etc/init.d/S88telnet
      echo "Изменяем права файла<br>"
      chmod 755 /etc/init.d/S88telnet && echo "Права изменены.<br>" || echo "ОШИБКА изменения прав /etc/init.d/S88telnet.<br>"
      echo "Запускаем telnet.<br>"
      telnetd &
      echo "telnet включен успешно.<br>"
      #echo "Для завершения перезагрузите камеру.<br>"
    ;;
    
    off)
      echo "Выключаем telnet.<br>"
      echo "Убиваем процесс.<br>"
      #ps | grep /home/watch_process | grep -v "grep" | awk '{print $1}' | xargs kill -9
      pidof telnetd | xargs kill -9
      echo "Убираем из автозагрузки.<br>"
      rm /etc/init.d/S88telnet && echo "telnet выключен успешно.<br>" || echo "ОШИБКА удаления /etc/init.d/S88telnet.<br>"
    ;;
    
    * )
      echo "<h3>ERROR! Неверный параметр для telnet.</h3>"
    ;;
  
  esac
}

setRTSP(){
  echo "$QUERY_STRING"
  #sed -i "s/portRtsp=554/portRtsp=5541/" /etc/ui.conf
  
  #rm /home/rtspsvr
  #mv /home/recv_X.726 /home/recv.726

}

setWIFI(){
  echo "$QUERY_STRING"
  #################################################
  #wifi_name="name"
  #wifi_password="password"
  #################################################
  #sed -i 's/valid1=0/valid1=1/g' /etc/ui.conf
  #sed -i 's/doreset=1/doreset=0/g' /etc/ui.conf
  ##rm /etc/wpa_supplicant.conf
  ##rm /home/wpa_supplicant.conf
  #echo "ctrl_interface=/var/run/wpa_supplicant
  #ap_scan=1
  #network={
  #ssid=\""$wifi_name"\"
  #scan_ssid=1
  #proto=WPA RSN
  #key_mgmt=WPA-PSK
  #pairwise=CCMP TKIP
  #group=CCMP TKIP
  #psk=\""$wifi_password"\"
  #}" > /etc/wpa_supplicant.conf
  #cp /etc/wpa_supplicant.conf /home/wpa_supplicant.conf
  #sleep 5
  ##mv "/home/hd1/test/equip_test.sh" "/home/hd1/test/equip_test.sh.old"
  #rm "/home/hd1/test/equip_test.sh"
  #reboot

}

setPASS(){
  _newpass=`echo "$QUERY_STRING" | grep -oE "(^|[?&])pass=[^&]+" | sed "s/%20/ /g" | cut -f 2 -d "=" | sed -e 's/  *$//'`
  echo "$_newpass" | passwd root --stdin
}


chainaOFF(){
  echo "$QUERY_STRING"
  #ps | grep /home/watch_process | grep -v "grep" | awk '{print $1}' | xargs kill -9
  #ps | grep /home/cloud | grep -v "grep" | awk '{print $1}' | xargs kill -9
  #sed -i 's|api.xiaoyi.com/v4/ipc/check_did|api.xiaoyi.cox/v4/ipc/check_did|g' /home/cloud
}

rebootCAM(){
  #echo "$QUERY_STRING"
  reboot
}

offCAM(){
  #echo "$QUERY_STRING"
  poweroff
}

backupCAM(){
	_date=$(date +%Y%m%d)

	mtd3=`echo "$QUERY_STRING" | grep -oE "(^|[?&])mtd3=[^&]+" | sed "s/%20/ /g" | cut -f 2 -d "=" | sed -e 's/  *$//'`
	mtd4=`echo "$QUERY_STRING" | grep -oE "(^|[?&])mtd4=[^&]+" | sed "s/%20/ /g" | cut -f 2 -d "=" | sed -e 's/  *$//'`
	mtd5=`echo "$QUERY_STRING" | grep -oE "(^|[?&])mtd5=[^&]+" | sed "s/%20/ /g" | cut -f 2 -d "=" | sed -e 's/  *$//'`
	mtd6=`echo "$QUERY_STRING" | grep -oE "(^|[?&])mtd6=[^&]+" | sed "s/%20/ /g" | cut -f 2 -d "=" | sed -e 's/  *$//'`

	mkdir -p "/home/hd1/backup/${_date}"

	if [[ "$mtd3" = "on" ]]; then
		#echo "mtd3=$mtd3"
		echo "Backup mtd3 <br>"
		cat "/dev/mtdblock3" > "/home/hd1/backup/${_date}/mtdblock3"
	fi 

	if [[ "$mtd4" = "on" ]]; then
		#echo "mtd4=$mtd4"
		echo "Backup mtd4 <br>"
		cat "/dev/mtdblock4" > "/home/hd1/backup/${_date}/mtdblock4"
	fi 

	if [[ "$mtd5" = "on" ]]; then
		#echo "mtd5=$mtd5"
		echo "Backup mtd5 <br>"
		cat "/dev/mtdblock5" > "/home/hd1/backup/${_date}/mtdblock5"
	fi 

	if [[ "$mtd6" = "on" ]]; then
		#echo "mtd6=$mtd6"
		echo "Backup mtd6 <br>"
		cat "/dev/mtdblock6" > "/home/hd1/backup/${_date}/mtdblock6"
	fi 

	echo "Резервное копирование завершено."	
}



htmlfooter(){
  ########################################
  # HTML конец страницы
  # вынесен отдельно с завершением, чтобы не использовать go to при ошибках
  ########################################
  cat << EOF2
      <hr />
      <!-- <form action="/cfg.cgi">
	<button type="submit">Вернуться</button>
      </form> -->
      <input type="button" onclick="history.back();" value="Вернуться"/>
      <hr />
      <p style="text-align: center;">&copy; SnakeSel для <a href="http://4pda.ru/forum/index.php?showtopic=638230" target="_blank">4pda</a>.</p>
    </body>
  </html>
EOF2

  exit 0

}

########################################
# Скрипт
########################################

# HTML заголовок
cat << EOF
<!DOCTYPE html>

<html>
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <link type="image/x-icon" rel="shortcut icon" href="/favicon.ico" />
    <title>${_title}</title>
  </head>
  <body>
EOF


#zapros=$(echo "$QUERY_STRING"; echo "$REQUEST_METHOD"; echo "$CONTENT_LENGTH";read -n $CONTENT_LENGTH POST_DATA <&0)

#  IFS='=&'
#  set -- $QUERY_STRING
#  (echo $1 is $2)

cmd=`echo "$QUERY_STRING" | grep -oE "(^|[?&])cmd=[^&]+" | sed "s/%20/ /g" | cut -f 2 -d "=" | sed -e 's/  *$//'`
#echo "${cmd}<br>"

case "$cmd" in

	settz )
		echo "<h3>Установка временной зоны.</h3>"
		setTZ
		;;
		
	setftp )
		echo "<h3>Изменение работы FTP</h3>"
		setFTP
		;;
		
	settelnet )
		echo "<h3>Изменение работы Telnet</h3>"
		setTELNET
		;;
		
	setpasswd )
		echo "<h3>Изменение пароля root</h3>"
		setPASS
		;;
		
	reboot )
		echo "<h3>Перезагрузка камеры.</h3>"
		rebootCAM
		;;
		
	off )
		echo "<h3>Выключение камеры.</h3>"
		offCAM
		;;

	backup )
		echo "<h3>Резервное копирование разделов.</h3>"
		backupCAM
		;;

	* )
		echo "<h3>ERROR! Command unrecognized.</h3>"
		;;

esac



#конец страницы
htmlfooter


exit 0
