# TLDR:

1. wget https://github.com/samuk10/leetmouse-gui/
2. pip install virtualenv
3. python3 -m venv venv
4. source ./venv/bin/activate
5. sudo pip install PySimpleGUIQt PySide6 
6. sudo python3 main.py

# leetmouse-gui
Simple GUI for my fork of leetmouse ([https://github.com/samuk10/leetmouse](https://github.com/samuk10/leetmouse/)). This program assumes you've already installed the leetmouse driver.
Please note it lacks form validation. All fields should be formatted as floats with an 'f' appended to the end, as in the example photo below.

![image](https://i.imgur.com/RFpL59Z.png)

## Requirements
- PySimpleGUIQt

``` sudo pip install pysimpleguiqt ```

## Use

Since this program must change module parameters it needs root access:
``` sudo python3 main.py ```


## Todo
- Form validation
- Error catching and handling for file I/O
- Graph to display acceleration curve (output vs input)
- Restructure so that fields are ordered in a way that makes sense, IE mode & mode specific options together, general options together
