#!/bin/bash
if [[ $UID -eq 0 ]];then
	sed -n -i -e '/^dtoverlay=/!p' -e '$adtoverlay=dwc2' /boot/config.txt
	if [ ! -f /etc/modules ]; then touch /etc/modules; fi
	sed -n -i -e '/^dwc2/!p' -e '$adwc2' /etc/modules
	sed -n -i -e '/^libcomposite/!p' -e '$alibcomposite' /etc/modules
	cp ./HID_config /opt/ && chmod 744 /opt/HID_config
	cat << EOF | tee /etc/systemd/system/hid-setup.service > /dev/null
[Unit]
Description=hid setup
[Service]
ExecStart=/opt/HID_config
[Install]
WantedBy=multi-user.target
EOF
	systemctl enable hid-setup.service
	echo "执行完成，如无错误提示即为成功，请重启后使用"
else
	echo "请使用 root 执行。"
fi
