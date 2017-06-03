# XJTU automatic Internet connection(windows only)

## Requirements
1. Python should be installed(for now, Python 2.7 is tested only)
2. requests module(a Python module) should be installed(pip install is quite simple)
3. "python" should be found by your system(type 'python' in cmd should act normal)

## Usage
1. clone this repo to where/you/save

2. open wideBand.py

3. fill in adsl_account information

	a) "name" field is your connection name(English name only, if your name is Chinese, remove it and build a new one in English)

	b) "username" and "password": your XJTU Internet username and password

4. open autostart.bat
change where/you/save to where you actually save wideBand.py(absolute path). For example, my setting is `C:/Users/jszhu/software/scripts/wideBand.py`.

5. copy autostart.bat to C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup
This step is for automatic connection when starting your Windows.

## Tips
1. For Python installation, install anoconda is recommended, since requests module is included(https://www.continuum.io/downloads/).
2. autostart.bat actually runs a python script. So, if "python" can not be found by your system, just replace it by your python.exe absolute path.