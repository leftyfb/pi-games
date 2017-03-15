from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED, InputEvent
from time import sleep
from signal import pause
import subprocess

# colors
O = [255,  92,   0] # Red
Y = [255, 255,   0] # Yellow
G = [  0, 255,   0] # Green
B = [  0, 153, 255] # Blue
R = [  255, 0, 0] # Blue
W = [  255, 255, 255] # White
P = [  255, 0, 255] # Purple
N = [  0,   0,   0] # Noir

seq_0 = [
N, N, N, N, N, N, N, N,
W, N, Y, Y, Y, Y, Y, N,
N, N, R, R, R, R, R, N,
N, N, O, O, O, O, O, N,
N, N, G, G, G, G, G, N,
N, N, P, P, P, P, P, N,
N, N, B, B, B, B, B, N,
N, N, N, N, N, N, N, N,
]
seq_1 = [
N, N, N, N, N, N, N, N,
N, N, Y, Y, Y, Y, Y, N,
W, N, R, R, R, R, R, N,
N, N, O, O, O, O, O, N,
N, N, G, G, G, G, G, N,
N, N, P, P, P, P, P, N,
N, N, B, B, B, B, B, N,
N, N, N, N, N, N, N, N,
]
seq_2 = [
N, N, N, N, N, N, N, N,
N, N, Y, Y, Y, Y, Y, N,
N, N, R, R, R, R, R, N,
W, N, O, O, O, O, O, N,
N, N, G, G, G, G, G, N,
N, N, P, P, P, P, P, N,
N, N, B, B, B, B, B, N,
N, N, N, N, N, N, N, N,
]
seq_3 = [
N, N, N, N, N, N, N, N,
N, N, Y, Y, Y, Y, Y, N,
N, N, R, R, R, R, R, N,
N, N, O, O, O, O, O, N,
W, N, G, G, G, G, G, N,
N, N, P, P, P, P, P, N,
N, N, B, B, B, B, B, N,
N, N, N, N, N, N, N, N,
]
seq_4 = [
N, N, N, N, N, N, N, N,
N, N, Y, Y, Y, Y, Y, N,
N, N, R, R, R, R, R, N,
N, N, O, O, O, O, O, N,
N, N, G, G, G, G, G, N,
W, N, P, P, P, P, P, N,
N, N, B, B, B, B, B, N,
N, N, N, N, N, N, N, N,
]
seq_5 = [
N, N, N, N, N, N, N, N,
N, N, Y, Y, Y, Y, Y, N,
N, N, R, R, R, R, R, N,
N, N, O, O, O, O, O, N,
N, N, G, G, G, G, G, N,
N, N, P, P, P, P, P, N,
W, N, B, B, B, B, B, N,
N, N, N, N, N, N, N, N,
]

def prog_0():
	subprocess.call(["python", "/home/ubuntu/pi-games/treasure.py"])
def prog_1():
	subprocess.call(["timeout", "10", "python", "/home/ubuntu/pi-games/random_sparkles.py"])
def prog_2():
	subprocess.call(["timeout", "10", "python", "/home/ubuntu/pi-games/temperature.py"])
def prog_3():
	subprocess.call(["timeout", "10", "python", "/home/ubuntu/pi-games/conway.py"])
def prog_4():
	subprocess.call(["timeout", "10", "python", "/home/ubuntu/pi-games/nyan.py"])
def prog_5():
	subprocess.call(["python", "/home/ubuntu/pi-games/marble.py"])

seq = [seq_0,seq_1,seq_2,seq_3,seq_4,seq_5]
prog = [prog_0,prog_1,prog_2,prog_3,prog_4,prog_5]

sense = SenseHat()
pos = 0
sense.set_pixels(seq[pos])
flag = True

while True:
	if flag:
		events = sense.stick.get_events()
		if len(events) != 0:
			event = events[-1]
		else:
			event = None
		
	if type(event) == InputEvent: 
		if event.direction == "down" and (event.action == "released" or event.action == "held"):
			pos += 1
		if event.direction == "up" and (event.action == "released" or event.action == "held"):
			pos -= 1
		if event.direction == "middle" and event.action == "pressed":
			flag = False
			prog[pos]()
			flag = True
		pos = pos%(len(seq))
		sense.set_pixels(seq[pos])
		sense.stick.get_events()
		sleep(0.1)
