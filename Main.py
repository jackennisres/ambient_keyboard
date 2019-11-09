from pynput.keyboard import Key, Listener
import os

themeList = []

for item in os.listdir():
    if '.' not in item:
        themeList.append(item)

print("Select a theme to use:\n")
for item in themeList:
    print(item)

selection = input("Type Your Selection Here: ")

dirpath = os.getcwd()
mine = dirpath +'\\' + 'Minecraft'
for i mine:
    print(i)