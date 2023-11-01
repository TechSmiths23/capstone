import RPi.GPIO as GPIO          
from time import sleep
#motor 1
ENA = 8
IN1 = 4
IN2 = 25
#motor 2 
ENB = 7
IN3 = 17
IN4 = 5
#motor5
ENC = 13
IN5 = 21
IN6 = 27
#motor 4
END = 24
IN7 = 6
IN8 = 12
#motor 6
ENE = 10
IN9 = 20
IN10 = 16
#motor 3
ENF = 18
IN11 = 23
IN12 = 22

temp1=1
GPIO.setmode(GPIO.BCM)

#gpio pin set up motor1 pmw
GPIO.setup(IN1,GPIO.OUT)
GPIO.setup(IN2,GPIO.OUT)
GPIO.setup(ENA,GPIO.OUT)
#gpio pin set up motor2 pmw
GPIO.setup(IN3,GPIO.OUT)
GPIO.setup(IN4,GPIO.OUT)
GPIO.setup(ENB,GPIO.OUT)
#gpio pin set up motor3 pmw
GPIO.setup(IN5,GPIO.OUT)
GPIO.setup(IN6,GPIO.OUT)
GPIO.setup(ENC,GPIO.OUT)
#gpio pin set up motor4 pwm
GPIO.setup(IN7,GPIO.OUT)
GPIO.setup(IN8,GPIO.OUT)
GPIO.setup(END,GPIO.OUT)
#gpio pin set up for motor 5
GPIO.setup(IN9,GPIO.OUT)
GPIO.setup(IN10,GPIO.OUT)
GPIO.setup(ENE,GPIO.OUT)
#gpio pin set up for motor 6
GPIO.setup(IN11,GPIO.OUT)
GPIO.setup(IN12,GPIO.OUT)
GPIO.setup(ENF,GPIO.OUT)

#output setup:
GPIO.output(IN1,GPIO.LOW)
GPIO.output(IN2,GPIO.LOW)

GPIO.output(IN3,GPIO.LOW)
GPIO.output(IN4,GPIO.LOW)

GPIO.output(IN5,GPIO.LOW)
GPIO.output(IN6,GPIO.LOW)

GPIO.output(IN7,GPIO.LOW)
GPIO.output(IN8,GPIO.LOW)

GPIO.output(IN9,GPIO.LOW)
GPIO.output(IN10,GPIO.LOW)

GPIO.output(IN11,GPIO.LOW)
GPIO.output(IN12,GPIO.LOW)

p1=GPIO.PWM(ENA,1000)
p2=GPIO.PWM(ENB,1000)
p3=GPIO.PWM(ENC,1000)
p4=GPIO.PWM(END,1000)
p5=GPIO.PWM(ENE,1000)
p6=GPIO.PWM(ENF,1000)

p1.start(25)
p2.start(25)
p3.start(25)
p4.start(25)
p5.start(25)
p6.start(25)

print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")    

while(1):

    x=input()
    
    if x=='r'
				print("run")
				if(temp1==1):
         GPIO.output(IN1,GPIO.HIGH) #motor 1
         GPIO.output(IN2,GPIO.LOW)  #motor 1
         GPIO.output(IN7,GPIO.HIGH) #motor 4
         GPIO.output(IN8,GPIO.LOW) #motor 4
         print("forward")
         x='z'

    elif x=='s':
        print("stop")
        GPIO.output(IN1,GPIO.LOW)
        GPIO.output(IN2,GPIO.LOW)
        GPIO.output(IN3,GPIO.LOW)
        GPIO.output(IN4,GPIO.LOW)
        GPIO.output(IN5,GPIO.LOW)
        GPIO.output(IN6,GPIO.LOW)
        GPIO.output(IN7,GPIO.LOW)
        GPIO.output(IN8,GPIO.LOW)
        GPIO.output(IN9,GPIO.LOW)
        GPIO.output(IN10,GPIO.LOW)
        GPIO.output(IN11,GPIO.LOW)
        GPIO.output(IN12,GPIO.LOW)
        x='z'

    elif x=='f':
        print("forward")
        GPIO.output(IN3,GPIO.HIGH) #motor 2
        GPIO.output(IN4,GPIO.LOW)  #motor 2
        GPIO.output(IN5,GPIO.HIGH) #motor 5
        GPIO.output(IN6,GPIO.LOW)  #motor 5
        temp1=1
        x='z'

    elif x=='r':
        print("reverse")
        GPIO.output(IN9,GPIO.HIGH) #motor 6
        GPIO.output(IN10,GPIO.LOW) #motor 6
        GPIO.output(IN11,GPIO.HIGH) # motor 3
        GPIO.output(IN12,GPIO.LOW)  #motor 3
        temp1=1
        x='z' 

    elif x=='l':
        print("turn left")
        GPIO.output(IN11,GPIO.HIGH) #motor 3
        GPIO.output(IN12,GPIO.LOW) #motor 3
        GPIO.output(IN5,GPIO.HIGH)  #motor 5
        GPIO.output(IN6,GPIO.LOW) #motor 5
        temp1=1
        x='z'

     elif x=='r':
        print("turn right")
        GPIO.output(IN3,GPIO.HIGH)  #motor 2
        GPIO.output(IN4,GPIO.LOW)  #motor 2
        GPIO.output(IN9,GPIO.HIGH) #motor6 
        GPIO.output(IN10,GPIO.LOW)  #motor 6
        temp1=1
        x='z'

    elif x=='1':
        print("low-1")
        p1.ChangeDutyCycle(25)
        p2.ChangeDutyCycle(25)
        p3.ChangeDutyCycle(25)
        p4.ChangeDutyCycle(25)
        p5.ChangeDutyCycle(25)
        p6.ChangeDutyCycle(25)
        x='z'

    elif x=='2':
        print("medium-2")
        p1.ChangeDutyCycle(50)
        p2.ChangeDutyCycle(50)
        p3.ChangeDutyCycle(50)
        p4.ChangeDutyCycle(50)
        p5.ChangeDutyCycle(50)
        p6.ChangeDutyCycle(50)
        x='z'

    elif x=='3':
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
        print("please ENAter the defined data to continue.....")
