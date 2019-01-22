#!/bin/bash
cd /sys/kernel/config/usb_gadget/
mkdir -p HID-Keyboard
cd HID-Keyboard

echo 0x0100 > bcdDevice		# 设备版本号，由制造商分配
echo 0x0200 > bcdUSB		# USB 规范号，该设备实现
#echo 0x00 > bDeviceClass	# USB 类代码，通过 USB 组织分配
#echo 0x00 > bDeviceProtocol	# USB 协议代码，由 USB 组织分配
#echo 0x00 > bDeviceSubClass	# USB 子类代码，通过 USB 组织分配
echo 0x08 > bMaxPacketSize0	# 最大数据包大小，仅可能的值是 8，16，32，和 64
echo 0x0104 > idProduct		# 产品 ID，由制造商分配
echo 0x1d6b > idVendor		# 供应商 ID，通过 USB 组织分配

mkdir -p strings/0x409

echo "RaspberryPi" > strings/0x409/manufacturer	# 制造商
echo "ZeroW" > strings/0x409/product		# 产品名
echo "233333333" > strings/0x409/serialnumber	# 序列号

mkdir -p functions/hid.usb0
echo 1 > functions/hid.usb0/protocol		# 设备的协议
echo 8 > functions/hid.usb0/report_length	# 键盘发送的报告长度
echo 1 > functions/hid.usb0/subclass		# HID 的类型

# 设备描述符
echo -ne \\x05\\x01\\x09\\x06\\xa1\\x01\\x05\\x07\\x19\\xe0\\x29\\xe7\\x15\\x00\\x25\\x01\\x75\\x01\\x95\\x08\\x81\\x02\\x95\\x01\\x75\\x08\\x81\\x03\\x95\\x05\\x75\\x01\\x05\\x08\\x19\\x01\\x29\\x05\\x91\\x02\\x95\\x01\\x75\\x03\\x91\\x03\\x95\\x06\\x75\\x08\\x15\\x00\\x25\\x65\\x05\\x07\\x19\\x00\\x29\\x65\\x81\\x00\\xc0 > functions/hid.usb0/report_desc

mkdir -p configs/c.1/strings/0x409

#echo 0x80 > configs/c.$C/bmAttributes
#echo 100 > configs/c.1/MaxPower	# 设备的最大功率(mA)
#echo "nyanyanya~" > configs/c.$C/strings/0x409/configuration

ln -s functions/hid.usb0 configs/c.1/
ls /sys/class/udc > UDC
