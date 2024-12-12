# Maplestory auto
This is a automation attack for msu [For education purpose only]

# Requirements
- Installed Python 2.7+ (https://www.python.org/downloads/)

# How to run
1. Install Python if you don't already installed.
2. Clone the repository to a folder on your PC.
3. Open Powershell/Terminal and go to the folder that you extracted from step 2
4. Run this command to install required libraries
```bash
pip install -r requirements.txt
```
5. Copy config.txt.sample to config.txt file
```bash
cp config.txt.sample config.txt
```

วิธีคือ ให้ไปหา python.exe ที่ลงไว้ครับ แล้วสร้าง shortcut มา
คลิกขวา properties shortcut นั้น แล้วเพิ่ม path ของ script bot ต่อท้ายไป ประมาณนี้

`D:\Python\Python310\python.exe D:\Develop\maplestory-auto\start.py`

แล้วมาติ๊ก run this program as admin

# Configuration
There are default configurations that suit my screen, but you can adjust to suit your screen.
Adjust values inside config.txt file to suit your screen and run bot smoothly.

# Config is in development, right now you have to modify the player.py code to match your need

| Name | Description | Type | Default |
| --- | --- | --- | --- |
| WALK_MAX_DURATION | max duration to walk around  | Second | 2 |

# Changelog
## v 0.0.1
+ Inital project
