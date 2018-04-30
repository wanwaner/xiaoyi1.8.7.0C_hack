#!/bin/bash

#source ./template/func

########################################
# Переменные
########################################

# Общая
_uptime=$(uptime)
#_kernel=$(uname -a)
#_firmware=$(cat /home/version | grep version -m1)
_firmware=$(sed -n 's/version=\(........\).*/\1/p' /home/version)


# сервисы
_srvlighttpd=$([ "$(pidof lighttpd)" ] && echo UP || echo DOWN)
_srvrtsp=$([ "$(pidof rtspsvr)" ] && echo UP || echo DOWN)
_srvtelnet=$([ "$(pidof telnetd)" ] && echo UP || echo DOWN)
_srvftp=$([ "$(pidof tcpsvd)" ] && echo UP || echo DOWN)

#pgrep lighttpd
#ps aux | grep lighttpd | grep -v "grep"

# Ресурсы
_df=$(df -h | grep -v 'tmpfs')
_free=$(free)
#_cpu=$(ps | awk '{s += $3} END {print s "%"}')


# Сеть
_wifi=$(cat /etc/wpa_supplicant.conf | grep ssid -m1 | sed 's/ssid=//')
_ip=$(ipaddr | grep ra0 | tail -n 1 | awk '{print $2}' | sed 's/\/24//')
_port=$(netstat -tualnp)


########################################
# HTML страница
########################################
cat header
cat << EOF
    <h2>Общая информация</h2>
    <ul>
      <li><strong>Uptime:</strong> ${_uptime}</li>
      <!-- <li><strong>Kernel: ${_kernel}</strong></li> -->
      <li><strong>Firmware:</strong> ${_firmware}</li>
    </ul>

    <h2>Сервисы</h2>
    <ul>
      <li><strong>lighttpd:</strong> ${_srvlighttpd}</li>
      <li><strong>RTSP:</strong> ${_srvrtsp}</li>
      <li><strong>telnet:</strong> ${_srvtelnet}</li>
      <li><strong>FTP:</strong> ${_srvftp}</li>
    </ul>
      
    <h2>Ресурсы</h2>
    <table>
      <thead>
        <tr>
          <th scope="col">Диск</th>
          <th scope="col">ОЗУ</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><pre>${_df}</pre></td>
          <td><pre>${_free}</pre></td>
        </tr>
      </tbody>
    </table>

    <h2>Сеть</h2>
    <ul>
      <li><strong>Wi-Fi:</strong> ${_wifi}</li>
      <li><strong>IP:</strong> ${_ip}</li>

      <li>
	<div class="spoil"> 
	  <div class="smallfont"><input type="button" value="Открытые порты" class="input-button" onclick="if (this.parentNode.parentNode.getElementsByTagName('div')[1].getElementsByTagName('div')[0].style.display != '') { this.parentNode.parentNode.getElementsByTagName('div')[1].getElementsByTagName('div')[0].style.display = ''; this.innerText = ''; this.value = 'Свернуть'; } else { this.parentNode.parentNode.getElementsByTagName('div')[1].getElementsByTagName('div')[0].style.display = 'none'; this.innerText = ''; this.value = 'Открытые порты'; }"/> 
	  </div> 
	  <div class="alt2"> 
	    <div style="display: none; text-align:left;"> 
	      <pre>${_port}</pre>
	    </div> 
	  </div> 
	</div> 
      </li>
    </ul>
EOF
cat footer

exit 0
