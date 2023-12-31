import RPi.GPIO as GPIO
from time import sleep
#motor 1
ENA = 13
IN1 = 27

#motor 2 
ENB = 24
IN3 = 17

#motor5
ENC = 26
IN5 = 5

#motor 4
END = 12
IN7 = 25

#motor 6
ENE = 19
IN9 = 20

#motor 3
ENF = 18
IN11 = 22


temp1=1
GPIO.setmode(GPIO.BCM)

#gpio pin set up motor1 pmw
GPIO.setup(IN1,GPIO.OUT)
GPIO.setup(ENA,GPIO.OUT)
#gpio pin set up motor2 pmw
GPIO.setup(IN3,GPIO.OUT)
GPIO.setup(ENB,GPIO.OUT)
#gpio pin set up motor3 pmw
GPIO.setup(IN5,GPIO.OUT)
GPIO.setup(ENC,GPIO.OUT)
#gpio pin set up motor4 pwm
GPIO.setup(IN7,GPIO.OUT)
GPIO.setup(END,GPIO.OUT)
#gpio pin set up for motor 5
GPIO.setup(IN9,GPIO.OUT)
GPIO.setup(ENE,GPIO.OUT)
#gpio pin set up for motor 6
GPIO.setup(IN11,GPIO.OUT)
GPIO.setup(ENF,GPIO.OUT)

#output setup:
GPIO.output(IN1,GPIO.LOW)
GPIO.output(IN3,GPIO.LOW)
GPIO.output(IN5,GPIO.LOW)
GPIO.output(IN7,GPIO.LOW)
GPIO.output(IN9,GPIO.LOW)
GPIO.output(IN11,GPIO.LOW)
#enable pwm signal
p1=GPIO.PWM(ENA,1000)
p2=GPIO.PWM(ENB,1000)
p3=GPIO.PWM(ENC,1000)
p4=GPIO.PWM(END,1000)
p5=GPIO.PWM(ENE,1000)
p6=GPIO.PWM(ENF,1000)
#start pwm duty cycle to 25%
p1.start(25)
p2.start(25)
p3.start(25)
p4.start(25)
p5.start(25)
p6.start(25)

print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward rev-reverse lt-leftturn rt-rightturn l-low m-medium h-high e-exit")
print("\n")

while(1):
    x=input()
    if x=='r':
        print("run")
        if(temp1==1):
            GPIO.output(IN1,GPIO.HIGH) #motor 1
            GPIO.output(IN7,GPIO.HIGH) #motor 4
            print("forward")
            x='z'
    elif x=='s':
        print("stop")
        GPIO.output(IN1,GPIO.LOW)
        GPIO.output(IN3,GPIO.LOW)
        GPIO.output(IN5,GPIO.LOW)
        GPIO.output(IN7,GPIO.LOW)
        GPIO.output(IN9,GPIO.LOW)
        GPIO.output(IN11,GPIO.LOW)
        x='z'
    elif x=='f':
        print("forward")
        GPIO.output(IN3,GPIO.HIGH) #motor 2
        GPIO.output(IN5,GPIO.HIGH) #motor 5
        temp1=1
        x='z'
    elif x=='rev':
        print("reverse")
        GPIO.output(IN11,GPIO.HIGH) #motor 3
        GPIO.output(IN9,GPIO.HIGH) #motor 6
        temp1=1
        x='z'
    elif x=='lt':
        print("turn left")
        GPIO.output(IN11,GPIO.HIGH) #motor 3
        GPIO.output(IN5,GPIO.HIGH)  #motor 5
        temp1=1
        x='z'
    elif x=='rt':
        print("turn right")
        GPIO.output(IN3,GPIO.HIGH)  #motor 2
        GPIO.output(IN9,GPIO.HIGH) #motor6
        temp1=1
        x='z'
    elif x=='l':
        print("low-1")
        p1.ChangeDutyCycle(25)
        p2.ChangeDutyCycle(25)
        p3.ChangeDutyCycle(25)
        p4.ChangeDutyCycle(25)
        p5.ChangeDutyCycle(25)
        p6.ChangeDutyCycle(25)
        x='z'
    elif x=='m':
        print("medium-2")
        p1.ChangeDutyCycle(50)
        p2.ChangeDutyCycle(50)
        p3.ChangeDutyCycle(50)
        p4.ChangeDutyCycle(50)
        p5.ChangeDutyCycle(50)
        p6.ChangeDutyCycle(50)
        x='z'
    elif x=='h':
        print("high-3")
        p1.ChangeDutyCycle(75)
        p2.ChangeDutyCycle(75)
        p3.ChangeDutyCycle(75)
        p4.ChangeDutyCycle(75)
        p5.ChangeDutyCycle(75)
        p6.ChangeDutyCycle(75)
        x='z'
    elif x=='e':
        GPIO.cleanup()
        break
    else:
        print("<<<  wrong data  >>>")
        print("please Enter the defined data to continue.....")
