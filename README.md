# RPI\_GPIO\_HID\_Keyboard
**使用树莓派 GPIO 控制的模拟键盘！**

**该项目的开发已完成，如无 bug，这将是最终版本。**

**一些记录信息请看 [ZeroW 模拟键盘的开发记录](https://moe-new.github.io/2019/01/ZeroW-%E6%A8%A1%E6%8B%9F%E9%94%AE%E7%9B%98%E7%9A%84%E5%BC%80%E5%8F%91%E8%AE%B0%E5%BD%95/)。**

## 项目介绍：

在使用本项目前，请先**检查代码**，并根据需求**修改关键内容**。

**在本项目里，你将会看到：语法错误、混乱的变量名、以及由于复制粘贴造成的语法/变量名错误。**

这是一个简单的键盘模拟脚本。

从 Raspberry Pi 的 GPIO 读取按键状态，然后发送定义的 KeyCode 到 /dev/hidg0 触发 HID 键盘的输入。

使用的是机械键盘的任意轴体，两脚分别连接到 0v 和任意 PIN 口。

启动脚本时会将目标 PIN 调为 HIGH 模式，然后循环检测该 PIN 口状态。

轴体被按下时两脚闭合，PIN 口会变成 LOW 模式，写入对应 KeyCode 后发送。

关于 Raspberry Pi HID Keyboard 具体原理与操作请参考：[Using RPi Zero as a Keyboard](https://www.rmedgar.com/blog/using-rpi-zero-as-keyboard-setup-and-device-definition)


## 依赖项目：

+ 初始化 HID 设备：
  - [Using RPi Zero as a Keyboard Part 1: Setup and device definition](https://www.rmedgar.com/blog/using-rpi-zero-as-keyboard-setup-and-device-definition)（已参考该文章制作[初始化脚本](https://github.com/Moe-New/RPI_GPIO_HID_Keyboard/blob/master/Setup/USB_Setup.sh)）
  - [Moe-New/P4wnP1](https://github.com/Moe-New/P4wnP1)（推荐使用，可以利用该项目中的其他功能进行调试）

+ Python 2.7+

+ GPIO 控制：[RPi.GPIO](https://pypi.org/project/RPi.GPIO/)（必须，Python 控制 GPIO 的库）


## 适用设备：

+ Raspberry Pi Zero （未测试）

+ Raspberry Pi Zero W （当前主要测试环境）

## 使用方法：
请查看 [wiki](https://github.com/Moe-New/RPI_GPIO_HID_Keyboard/wiki)

## 一些附加资料：
+ 开发记录：[ZeroW 模拟键盘的开发记录](https://moe-new.github.io/2019/01/ZeroW-%E6%A8%A1%E6%8B%9F%E9%94%AE%E7%9B%98%E7%9A%84%E5%BC%80%E5%8F%91%E8%AE%B0%E5%BD%95/)

+ 初始化与发送数据：[Using RPi Zero as a Keyboard Part 3: Sending and receiving reports](https://www.rmedgar.com/blog/using-rpi-zero-as-keyboard-send-reports)

+ 操作例子：[使用树莓派 Zero 实现带回显的新型 Bad USB](http://shumeipai.nxez.com/2018/06/26/using-raspberry-pi-zero-to-implement-new-bad-usb-with-echo.html)

+ 键值定义表：[10 keyboard keypad page (0x07)](http://d1.amobbs.com/bbs_upload782111/files_47/ourdev_692986N5FAHU.pdf)

+ 键值在线查询：[USB HID Keyboard Scan Codes](https://serverhelfer.de/usb-hid-keyboard-scan-codes/)

