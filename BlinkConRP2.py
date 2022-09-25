# nop(): Do nothing.
# [31] works for making the rapsberry to stop for 31 status, which lasts 8 ns each

'''
INTEGRANTES DEL GRUPO DE TRABAJO: 
Michael Andrés Olívares Herrera - 20212005063
Luding Andrés Castañeda García - 20211005022
Mateo Salamanca Pulido - 20211005107
'''

import time
import rp2 as sm
from machine import Pin

@rp2.asm_pio(set_init=rp2.PIO.OUT_LOW)
def blink():
    cycletime=4
    wrap_target()
    set(pins,1)	[0]
    set(pins,0)	[0]
    nop()		[2]
    nop()		[cycletime]
    nop()		[cycletime]
    nop()		[cycletime]
    nop()		[cycletime]
    nop()		[cycletime]
    nop()		[cycletime]
    nop()		[cycletime]
    nop()		[cycletime]
    nop()		[cycletime]
    wrap()

sm=rp2.StateMachine(0,blink,freq=2000,set_base=Pin(25))

sm.active(1)
time.sleep(10)
sm.active(0)