"""
TODO:
RECORDING SAVING **
RECORDING MANIPULATION ****

INTERFACE **
LOGIC *

BUGS
"""

from os import system, chdir
from time import sleep
from colorama import Fore, Back, Style
import pyaudio
import wave

system("title Red Means Recording")
system("cls")

check = ".m"
cow_p = """
\|/          (__)    
     `\------({})   {} 
       ||    (__)
       ||w--||     \|/
   \|/
"""

f = open("settings.txt", 'r').read()


def Settings():	
	print("PASTE IN THE DESTINATION")
	loc = input("")
	open("settings.txt", 'w').write(loc)

	
if (f == ""):
	Settings()

chdir(open("settings.txt", 'r').read().replace('\\', '/'))

p = pyaudio.PyAudio()
stream = p.open(format = pyaudio.paInt16, channels = 2, rate = 44100, input = True, frames_per_buffer = 1024)

wf = wave.open("output.wav", 'wb')
wf.setnchannels(2)
wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
wf.setframerate(44100)

frames = []
SEC = 5

def MainLoop():
	global rec;
	global check;
		
	while True:
		if (check == ".e"):
			system("cls");
			print(Fore.RED + Style.DIM + "(O) - RECORDING OFF");
			print(cow_p.format("XX", "MOO!"))	
			print(Style.RESET_ALL)
			sleep(1)
			check = ".m"
			continue
			
		elif (check == ".s"):
			system("cls");
			print(Fore.RED + Style.DIM + "(O) - RECORDING ON");
			print(cow_p.format("oo", "MOO"))
			
			for i in range(0, int(44100/1024*SEC)):
				data = stream.read(1024)
				frames.append(data)
			
			stream.stop_stream()
			wf.writeframes(b''.join(frames))
			wf.close()
			
			check = ".e"
			continue
				
		elif (check == ".q"):
			stream.close()
			p.terminate()
			quit()
		
		elif (check == ".d"):
			settings()
		
		elif (check == ".m"):
			system('cls');
			print("(O) - RECORDING OFF")
			print(cow_p.format("oo", ""))
		
		check = input(Fore.WHITE + ">");

MainLoop()


