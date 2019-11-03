import machine
import utime

from hcsr04 import HCSR04

sensor = HCSR04(trigger_pin=16, echo_pin=0)

#pins for motors
pin1 = machine.Pin(16, machine.Pin.OUT)
pin2 = machine.Pin(5, machine.Pin.OUT)
pin3 = machine.Pin(4, machine.Pin.OUT)
pin4 = machine.Pin(0, machine.Pin.OUT)

# set motors stopped by default
pin1.off()
pin2.off()
pin3.off()
pin4.off()

# distance sensor pins
trigger = machine.Pin(14, machine.Pin.OUT)
echo = machine.Pin(12, machine.Pin.IN)

#pins for line sensors
adc = machine.ADC(0)

def forward() :
    ''' make the robot go forward '''
    pin1.on()
    pin2.off()
    pin3.on()
    pin4.off()

def stop() :
    ''' make the robot stop '''
    pin1.off()
    pin2.off()
    pin3.off()
    pin4.off()

def turn_left() :
    ''' make the robot turn left '''
    pin1.off()
    pin2.on()
    pin3.on()
    pin4.off()

def turn_right() :
    ''' make the robot turn right '''
    pin1.on()
    pin2.off()
    pin3.off()
    pin4.on()

def callback(p, t1) :
    print('pin change', p, utime.ticks_us() - t1)

def get_distance() :
    return sensor.distance_cm()

def get_distance2() :
    # make sure trigger and echo is off
    trigger.off()
    echo.off()
    utime.sleep_us(5)
    
    t1 = utime.ticks_us()
    fun  = lambda p: callback(p, t1)
    echo.irq(trigger=machine.Pin.IRQ_RISING, handler=fun)
    
    # send echo
    print(utime.ticks_us())
    
    trigger.on()
    utime.sleep_us(10)
    trigger.off()
    
    # wait for response or for a timeout
    while (echo.value() == 0) :
        if (utime.ticks_us() - t1) >= 200*1000 :
            break
    
    # compute the time take to return the echo
    duration = (utime.ticks_us() - t1)
    return duration, duration /1000 *  34.029

def check_line() :
    '''
     check if the line sensor can see a line
    '''
    return adc.read() < 512