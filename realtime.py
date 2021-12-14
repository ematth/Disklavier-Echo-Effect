import threading
import rtmidi
import musx
import time
import sys

echo_level = [1.1, 1.1, 1, 0.7, 0.6, 0.5, 0.4, 0.2, 0.15, 0.1]

midiout = rtmidi.MidiOut()
midiin = rtmidi.MidiIn()
outports = midiout.get_ports()
inports = midiin.get_ports()
try:    
    # Playback to and from mio requires both ports to be 'mio'
    midiout.open_port(outports.index('mio'))
    midiin.open_port(inports.index('mio'))
except:
    print("Couldn't find specific in/out ports")
print('ready to run!')


def echo_effect(message, data, repeat, sustain, cutoff):
    msg = message
    print(msg)
    print('echo happens')
    if repeat < 1: # edge cases for repeat
        repeat = 1
    if cutoff < 21 or cutoff > 108: # edge cases for cutoff pitch
        cutoff = 1000
    if msg[1] <= cutoff:
        for i in range(repeat):
            print('play ', msg[1], ' ', i+1, ' times')
            print(int(msg[1] / 12))
            time.sleep(0.15)
            midiout.send_message(musx.note_on(msg[0], msg[1], 2.5 + i))
            if sustain <= 0: # edge cases for sustain
                time.sleep(data + echo_level[int(msg[1] / 12)])
            else:
                time.sleep(data + sustain)
            midiout.send_message(musx.note_off(128, msg[1], 0))
        midiout.send_message(musx.note_off(128, msg[1], 0))

def new_midi_callback(repeat, sustain, cutoff):
    msg = midiin.get_message()
    if msg is not None:
        print(msg)
    if msg and msg[0][2] == 0:
        thing = threading.Thread(target=echo_effect, args=(msg[0], msg[1], repeat, sustain, cutoff))
        thing.start()

if __name__ == '__main__':  
    while True:
        # arugments:
        # (1) repeat -> positive integer (n > 0)
        # (2) sustain -> positive integer (n >= 0)
        # (3) cutoff -> positive integer (21 <= n <= 108)
        new_midi_callback(int(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3])) 
        pass