# RPI GPIO HID Keyboard
这是一个树莓派模拟 HID 键盘设备以及 Python 发送键码的简单脚本示例。  
**该项目的开发已完成，这是最终版本。**  
这个 Python 脚本的执行效率不高，如果需要制作游戏用键盘，可以考虑其他方式。  
同样原理的 Android 新项目：[Android HID Keyboard](https://github.com/Sucareto/Android_HID_Keyboard)

## 适用设备：
- Raspberry Pi Zero （未测试）
- Raspberry Pi Zero W （当前主要测试环境）

## 使用方法：
首先进行基础配置：
- 启动到 raspbian（推荐使用 raspbian lite）
- 安装 Python 以及 RPi.GPIO 库
- 进行必要的设置后，下载本项目
- 启用 USB HID 设备：
```
cd RPI_GPIO_HID_Keyboard/Setup
sudo bash USB_Setup.sh
```
 - 如无错误，重启即可使用

直接运行：
```
python sdvx_controller.py
```
或者，配置开机自动运行：
```
cd RPI_GPIO_HID_Keyboard
sudo cp sdvx_headless.service /etc/systemd/system/sdvx_headless.service
sudo systemctl enable sdvx_headless.service
sudo cp sdvx_controller.py /opt/
sudo chmod +x /opt/sdvx_controller.py
```
默认启用了 headless 模式，可以按下 GPIO 40 触发关机，如需禁用，可修改 sdvx_headless.service 文件。

## 一些附加资料：
- 原理与操作：[Using RPi Zero as a Keyboard Part 1: Setup and device definition](https://www.rmedgar.com/blog/using-rpi-zero-as-keyboard-setup-and-device-definition/)
- 操作例子：[使用树莓派 Zero 实现带回显的新型 Bad USB](http://shumeipai.nxez.com/2018/06/26/using-raspberry-pi-zero-to-implement-new-bad-usb-with-echo.html)
- 键值定义表：[10 keyboard keypad page (0x07)](http://d1.amobbs.com/bbs_upload782111/files_47/ourdev_692986N5FAHU.pdf)
- 键值在线查询：[USB HID Keyboard Scan Codes](https://serverhelfer.de/usb-hid-keyboard-scan-codes/)
