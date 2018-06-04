from colorama import init, Fore, Back, Style # excellent library for colorful text for terminal output
import os
import pathlib
import PIL.ImageGrab
import sys
import datetime
import time

init() # colorama

def get_utc_from_datetime(dt):
	return int((dt - datetime.datetime(1970, 1, 1)).total_seconds())

def get_current_datetime():
    return datetime.datetime.utcnow()

def add_final_slash_to_dir(path):
	if os.path.isdir(path):
		path = os.path.join(path, "")
		return str(path)

if len(sys.argv) < 2:
	print(Fore.RED)
	print("Please specify the directory in which you want to store your images.")
	print(Fore.MAGENTA)
	print("Ex. python timelapse.py C:\\Users\\Alex\\Documents\\DesktopTimelapseImages")
	print(Style.RESET_ALL)
	exit()


img_dir = add_final_slash_to_dir(sys.argv[1])
pathlib.Path(img_dir).mkdir(parents=True, exist_ok=True)
print("Storing images in " + Fore.GREEN + img_dir + Style.RESET_ALL)

while True:
	im = PIL.ImageGrab.grab()
	dt = get_current_datetime()
	utc = get_utc_from_datetime(dt)
	print(dt, utc)
	fname = str(os.path.join(img_dir, str(utc) + ".jpg"))
	im.save(fname)
	time.sleep(8)