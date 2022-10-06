import time

import os

import sys

import webbrowser

from global_hotkeys import *

from bot import click_if_exists

from bot import hold_key

from bot import found

from time import sleep

from pyperclip import copy

from pyautogui import hotkey

from pyautogui import doubleClick

from pyautogui import click

from pyautogui import alert

from pyautogui import confirm

from pyautogui import moveTo

is_alive = True

awake = True

Keyboard_Command = True

os.chdir(r"C:\Users\rcherveny\Documents\Code\MagicART-Hotkeys")



# Lists

template_list = [
    "10K Template",
    "14K Template",
    "Logos Template",]

zoom_list = [
    r'images\Silver Template.png',
    r'images\10K Template.png',
    r'images\14K Template.png',]

sleeplist = [
    "Don't fall asleep...",
    "Stay awake...",
    "Can't sleep yet...",
    "So tired..."]



# Startup Notification

alert("Joe's Hotkeys are ready to go!")

# Commands

def commands_on_off(input_function):
    def wrapper():
        global Keyboard_Command
        if not Keyboard_Command:
            alert("Keyboard Commands OFF")
        if Keyboard_Command:
            input_function()
    return wrapper

@commands_on_off
def open_MagicArt():
    print("Opening MagicArt")

    moveTo(500,0)
    os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\MagicArt 5\MagicART 5.lnk")
    time.sleep(2)

    found = click_if_exists(r'images\object property pin.png')
    if not found:
        found = click_if_exists(r'images\open magicart.png')
        if not found:
            click_if_exists(r'images\highlighted open magicart.png')
        found = click_if_exists(r'images\object property pin.png')
        click_if_exists(r'images\fullscreen.png')
        if not found:
            print("oops, couldn't finish command")                
            return None

    click_if_exists(r'images\fullscreen.png')
        
    hotkey("ctrl", "o")
    time.sleep(1)
    click_if_exists(r'images\drop down menu.png')
    time.sleep(1)
    found = click_if_exists(r'images\desktop.png')
    if not found:
        found = click_if_exists(r'images\desktop 2.png')
        if not found:
            print("oops, couldn't finish command")                
            return None
    time.sleep(1)
    found = click_if_exists(r'images\MagicArt Saves file 2.png', double = True)
    if not found:
        found_f = click_if_exists(r'images\MagicArt Saves file.png', double = True)
        if not found_f:
            print("oops, couldn't finish command")                
            return None
    time.sleep(1)
    click_if_exists(r'images\Open .925 Template.png', double = True)
    time.sleep(2)

    for i in template_list:
        hotkey("ctrl", "o")
        time.sleep(1)
        copy(i)
        hotkey("ctrl", "v")
        hotkey("enter")
        time.sleep(2)
            
    click_if_exists(r'images\Logos Template.png')
    click_if_exists(r'images\fit to page.png')
    click_if_exists(r'images\10%.png')
        
    for k in zoom_list:
        print(f"Looking for {k}...")
        click_if_exists(k)
        click_if_exists(r'images\fit to page.png')
        click_if_exists(r'images\15%.png')
            
    print("Command Finished")

@commands_on_off
def open_Spotify(): 
    print("Opening Spotify...")
    os.startfile("C:\\Users\\rcherveny\\AppData\\Roaming\\Spotify\\Spotify.exe")
    time.sleep(2)
    click_if_exists(r'images\minimise spotify.png')
    time.sleep(1)
    click_if_exists(r'images\Bluetooth.png')
    time.sleep(1)
    click_if_exists(r'images\Show Bluetooth Devices.png')
    time.sleep(2)

    connected = found(r'images\Bluetooth connected.png')
    
    if not connected:
        r = confirm("No devices connected. Try connecting?", buttons = ['Yes', 'No'])
        if r == 'Yes':
            connected = found(r'images\Bluetooth connected.png')
            while not connected:
                timeout = 20
                timeout_start = time.time()
                while time.time() < timeout_start + timeout:
                    connected = found(r'images\Bluetooth connected 2.png')
                    click_if_exists(r'images\Bluetooth not connected.png')
                    time.sleep(1)
                    if connected:
                        print("Bluetooth Connected")
                        click_if_exists(r'images\exit bluetooth.png')
                        return None
                if time.time() > timeout_start + timeout:
                    alert("Sorry, I couldn't connect any devices...")
                    return None
                
        if r == 'No':
            print("No devices connected")
    if connected:
        print("Bluetooth Connected")
        click_if_exists(r'images\exit bluetooth.png')
        
    print("Command Finished")

@commands_on_off
def open_toolbar():
    t = confirm('What would you like to open?', 'Toolbar', buttons = ['Google', 'Workday', 'SKU Search', 'Spotify', 'Calculator', 'Shutdown'])
    if t == 'Google':
        webbrowser.open(f"https://www.google.com/")
    if t == 'Workday':
        webbrowser.open(f"https://www.myworkday.com/wday/authgwy/signetjewelers/login.htmld")
    if t == 'SKU Search':
        os.startfile(r'sku_search.py')
    if t == 'Spotify':
        open_Spotify()
    if t == 'Calculator':
        os.system("calc")
    if t == 'Shutdown':
        shut_down_computer()

def toggle_keyboard_commands():
    global Keyboard_Command
    if not Keyboard_Command:
        enable_disable = 'disable' if Keyboard_Command else 'enable'
        on_off = 'on' if Keyboard_Command else 'off'
        r = confirm("Do you want to {enable_disable} Joe's Keyboard Commands?", buttons = ['Yes', 'No'])
        if r == 'Yes':
            Keyboard_Command = False if Keyboard_Command else True
            alert("Keyboard Commands {on_off}")    
@commands_on_off                
def shut_down_computer():
    hold_key('alt', 5 )
    hotkey('tab')
    hold_key('delete', 2)
    hotkey('F4')
    time.sleep(2)
    click_if_exists(r'images\shutdown.png')
        
def exit_application():
        alert("Exiting Application. Have a good day!")
        quit()


# Key Bindings for Commands

        

bindings = [
    [["F2"], None, commands_on_off(lambda : click_if_exists(r'images\Silver Template.png'))],
    [["F3"], None, lambda : click_if_exists(r'images\10K Template.png')],
    [["F4"], None, lambda : click_if_exists(r'images\14K Template.png')],
    [["F5"], None, lambda : click_if_exists(r'images\Logos Template.png')],
    [["F6"], None, open_toolbar],
    [["F11"], None, exit_application],
    [["F12"], None, open_MagicArt],
    [["control", "`"], None, toggle_keyboard_commands],
    [["control", "shift"], None, lambda : click_if_exists(r'images\horizontal allign.png')],
    [["control", "alt"], None, lambda : click_if_exists(r'images\center button.png')],
]

# Always Running

register_hotkeys(bindings)

start_checking_hotkeys()

while awake:
    for m in sleeplist: 
        time.sleep(60 * 5)
        hotkey("F15")
        print(m)

while is_alive:
    time.sleep(0.1)
