from pynput import mouse
from pynput.mouse import Button, Controller
import pyautogui
import time
import keyboard

mymouse = Controller()
def solve_hanoi(peg, current, helper, goal):
    if peg>0:
        solve_hanoi(peg-1, current, goal, helper)
        print("Move disk "+ str(peg) + " from peg " + str(current) + " to peg " + str(goal))
        move(current)
        move(goal)
        solve_hanoi(peg-1, helper, current, goal) 
def move(thingy):
    if keyboard.is_pressed('space'):
        print("exiting")
        exit()
    if thingy == 1:
        pyautogui.moveTo(1152,419)
    elif thingy==2:
        pyautogui.moveTo(1439,420)
    elif thingy == 3:
        pyautogui.moveTo(1720,423)
    mymouse.press(Button.left)
    mymouse.release(Button.left)

solve_hanoi(9,1,2,3)
exit()
