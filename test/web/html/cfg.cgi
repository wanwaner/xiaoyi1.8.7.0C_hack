#!/bin/bash

########################################
# Переменные
########################################

# Подсчет TZ
carrentTZ=$(cat /etc/TZ | sed 's/GMT//')
_tz=$((8-carrentTZ))

# Services
[ "$(pidof tcpsvd)" ] && _ftpon="checked" || _ftpoff="checked"
[ "$(pidof telnetd)" ] && _telneton="checked" || _telnetoff="checked"

# Backup
_dfhd1=$(df -h | grep hd1 | awk '{print $4}')
_date=$(date +%Y%m%d)
[ "$_dfhd1" ] && _disableHD1="" || _disableHD1="disabled"


########################################
# HTML страница
########################################
cat header
cat << EOF
    <form action="/cmd.cgi/">
      <p><h3>Часовой пояс</h3></p>
      <p>Текущее время: $(date)</p>
      <p>Часовой пояс:</p>
      <p><input type=number size=2 maxlength=1 name="tz" value="${_tz}" /></p>
      <p><button type="submit" name="cmd" value="settz">Изменить</button></p>
    </form>
    
    <hr />
    
    <table border="1" cellpadding="0" cellspacing="2" align="center" width="500" >
      <tbody>
	<tr>
	  <td>      
		<form action="/cmd.cgi/">
      			<p><h3>FTP</h3></p>
      			<p><input type="radio"  $_ftpon name="ftp" value="on" />Включен</p>
      			<p><input type="radio"  $_ftpoff name="ftp" value="off" />Выключен</p>
      			<p><button type="submit" name="cmd" value="setftp">Изменить</button></p>
    		</form>
          </td>
	  <td>    
		<form action="/cmd.cgi/">
      			<p><h3>Telnet</h3></p>
      
      			<p><input type="radio"  ${_telneton} name="telnet" value="on" />Включен</p>
      			<p><input type="radio"  ${_telnetoff} name="telnet" value="off" />Выключен</p>
      			<p><button type="submit" name="cmd" value="settelnet">Изменить</button></p>
    		</form>

	  </td>
	</tr>
      </tbody>
    </table>
    
    <hr />
    <form action="/cmd.cgi/" >
      <p><h3>Бэкап разделов камеры.</h3></p>
      <p>Сохранение на карту памяти в папку "backup/${_date}"</p>
      <p>Свободно на карте: ${_dfhd1}${_disableHD1}</p>
      <p><input type="checkbox"  name="mtd3" ${_disableHD1}/>mtd3 (os)</p>
      <p><input type="checkbox"  name="mtd4" ${_disableHD1}/>mtd4 (rootfs)</p>
      <p><input type="checkbox"  name="mtd5" ${_disableHD1}/>mtd5 (home)</p>
      <p><input type="checkbox"  name="mtd6" ${_disableHD1}/>mtd6 (vd)</p>
      <p><button type="submit" name="cmd" value="backup" ${_disableHD1}>Сохранить</button></p>
    </form>

    <br>
EOF
cat footer

exit 0
