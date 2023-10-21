import RPi.GPIO as GPIO          
from time import sleep

ENA = 18
IN1 = 22
IN2 = 23
temp1=1

GPIO.setmode(GPIO.BCM)
GPIO.setup(IN1,GPIO.OUT)
GPIO.setup(IN2,GPIO.OUT)
GPIO.setup(ENA,GPIO.OUT)
GPIO.output(IN1,GPIO.LOW)
GPIO.output(IN2,GPIO.LOW)
p=GPIO.PWM(ENA,1000)
p.start(25)
print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")    

while(1):

    x=input()
    
    if x=='r':
        print("run")
        if(temp1==1):
         GPIO.output(IN1,GPIO.HIGH)
         GPIO.output(IN2,GPIO.LOW)
         print("forward")
         x='z'

    elif x=='s':
        print("stop")
        GPIO.output(IN1,GPIO.LOW)
        GPIO.output(IN2,GPIO.LOW)
        x='z'

    elif x=='f':
        print("forward")
        GPIO.output(IN1,GPIO.HIGH)
        GPIO.output(IN2,GPIO.LOW)
        temp1=1
        x='z'

    elif x=='l':
        print("low")
        p.ChangeDutyCycle(25)
        x='z'

    elif x=='m':
        print("medium")
        p.ChangeDutyCycle(50)
        x='z'

    elif x=='h':
        print("high")
        p.ChangeDutyCycle(75)
        x='z'
     
    
    elif x=='e':
        GPIO.cleanup()
        break
    
    else:
        print("<<<  wrong data  >>>")
        print("please ENAter the defined data to continue.....")
