from ev3dev2.motor import MoveTank, OUTPUT_A, OUTPUT_D, SpeedPercent
from ev3dev2._platform.ev3 import INPUT_1, INPUT_2, INPUT_3
from ev3dev2.sensor.lego import ColorSensor
import keyboard as kbd
import subprocess
import os
import time

path = os.path.join(r'C:\ProgramData', 'Anaconda3', 'envs', 'robot', 'Scripts', 'ev3dev2simulator.exe')
subprocess.Popen([path, '-t', 'config_large'])
time.sleep(10)
print('World started!')

SPEED_FORWARD = SpeedPercent(50)
SPEED_BACKWARD = SpeedPercent(-50)
TURN_TIME = 0.1

tank_drive = MoveTank(OUTPUT_A, OUTPUT_D)
csl = ColorSensor(INPUT_1)
csc = ColorSensor(INPUT_2)
csr = ColorSensor(INPUT_3)
color = False

while True:
    if csc.color != 1:
        print(f"Center sensor: {csc.color_name} / RGB: {csc.raw}")
        color = True
    if csl.color != 1:
        print(f"Left sensor: {csl.color_name} / RGB: {csl.raw}")
        color = True
    if csr.color != 1:
        print(f"Right sensor: {csr.color_name} / RGB: {csr.raw}")
        color = True
    if color:
        print('=============================================')
        color = False

    b = kbd.read_key()
    if b == 'up':
        tank_drive.on_for_seconds(SPEED_FORWARD, SPEED_FORWARD, 1)
        tank_drive.stop()
    elif b == 'down':
        tank_drive.on_for_seconds(SPEED_BACKWARD, SPEED_BACKWARD, 1)
        tank_drive.stop()
    elif b == 'right':
        tank_drive.on_for_seconds(SPEED_FORWARD, SPEED_BACKWARD, TURN_TIME)
    elif b == 'left':
        tank_drive.on_for_seconds(SPEED_BACKWARD, SPEED_FORWARD, TURN_TIME)
    elif b == 'space':
        tank_drive.stop()

