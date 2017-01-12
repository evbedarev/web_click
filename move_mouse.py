import ctypes
import time
import random
mouse_event = ctypes.windll.user32.mouse_event
MOUSEEVENTF_MOVE = 0x0001

def main():
	if random.randint(1,2)%2 >0:
		dx = random.randint(1,100)
		dy = random.randint(1,100)
	else:
		dx = -random.randint(1,100)
		dy = -random.randint(1,100)
	mouse_event(MOUSEEVENTF_MOVE, dx, dy, 0, 0);
	time.sleep(10)#sleep for 60 seconds
	print("mouse moved")