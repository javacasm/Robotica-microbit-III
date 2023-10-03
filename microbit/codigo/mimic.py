mimic python.py
I
Tipo
Texto
Tamaño
3 KB (3.092 bytes)
Almacenamiento usado
3 KB (3.092 bytes)
Ubicación
Mimic - the micro:bit parrot
Propietario
Ivan Bosnić
Modificado
5 ene 2021 por Ivan Bosnić
Abierto
20:37 por mí
Creado
5 ene 2021
Sin descripción
Los usuarios con acceso de lectura pueden descargar este elemento
# mi:mic (C) 2020 Micro:bit Educational Foundation
# MIT https://spdx.org/licenses/MIT.html
# Original Author D.J.Whale. Updated to latest API by J Austin
# Sonic function written by D.J.Whale in 2017

from microbit import *
import music

MOUTH_CLOSED = Image("09090:00000:00000:99999:00000")
MOUTH_OPENED = Image("09090:00000:09990:90009:09990")
LOUD = Image("99999:90009:90009:90009:99999")
QUIET = Image("00000:09990:09090:09990:00000")
ASLEEP = Image("00000:00000:00900:00000:00000")

def sonic(f=3000, fstep=32, fdepth=100, ton=10, toff=0, duration=2000):
    # from sonic screwdriver, written by D.J.Whale for BBC Doctor Who.
    # first surfaced in "mission sonic' in April 2017.
    try:
        ft = f
        music.pitch(ft)
        st = running_time()
        while running_time() < st+duration:
            sleep(ton)
            if toff != 0:
                music.stop()
                sleep(toff)
            fn = ft + fstep
            if fn >= f + fdepth:
                fstep *= -1
                fn = f + fdepth
            elif fn <= f - fdepth:
                fstep *= -1
                fn = f - fdepth
            if fn != ft:
                ft = fn
                music.pitch(int(ft))
    finally:
        music.stop()

def squeak(duration):
    depth = 1000
    sonic(duration=duration, ton=1, fdepth=depth, fstep=depth/(duration/4))

user_speaking = False
loud = False
start = 0

def record(pattern):
    global user_speaking, loud, start
    now = running_time()
    s = microphone.current_event()
    microphone.get_events() # stop sound buffer filling up
    if not user_speaking:
        if s == SoundEvent.LOUD:
            start = now
            user_speaking = True
            loud = True
            pattern.clear()
            display.show(LOUD)
        else: # quiet
            display.show(ASLEEP)
    else: #user speaking
        duration = now - start
        if loud:
            if s == SoundEvent.QUIET:
                pattern.append(duration)
                start = now
                loud = False
                display.show(QUIET)
        else: # quiet
            if s == SoundEvent.LOUD:
                pattern.append(duration)
                start = now
                loud = True
                display.show(LOUD) 
            else:
                if duration > 1000:
                    user_speaking = False
                    return True  # recorded
                    
    return False # not recorded
        
def mimic(pattern):
    loud = True
    for d in pattern:
        if loud:
            display.show(MOUTH_OPENED)
            squeak(d)
        else:
            display.show(MOUTH_CLOSED)
            sleep(d)
        loud = not loud

def run():
    phrasing = []
    #Change how 'loud' a sound we need for 'loud' to trigger
    microphone.set_threshold(SoundEvent.LOUD, 80)
    while True:
        if record(phrasing):
            mimic(phrasing)
            phrasing.clear()


run()
