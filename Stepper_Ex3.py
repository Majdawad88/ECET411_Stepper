#git clone https://github.com/Majdawad88/ECET411_Stepper.git

#Try
#Steps #: 50 100 200 300 
#Freq:    50 100 200 300
#Dir:     F, R,  F,  R
import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)  # Ignore warning for now
stepPads = [19, 13, 6, 5]
GPIO.setmode(GPIO.BCM)
for i in range(0, 4):
    GPIO.setup(stepPads[i], GPIO.OUT)

def motorDrive(numberSteps, Frequency, Direction):
    speed = float(1 / Frequency)
    if Direction == 'R':
        print("Reverse")
        for k in range(0, numberSteps):
            print("Stepp Number = ", k)
            for x in range(3, -1, -1):
                for j in range(3, -1, -1):
                    if x == j:
                        GPIO.output(stepPads[j], True)
                    else:
                        GPIO.output(stepPads[j], False)
                time.sleep(speed)
    elif Direction == 'F':
        print("Forward")
        for k in range(0, numberSteps):
            print("Stepp Number = ", k)
            for x in range(0, 4, 1):
                for j in range(0, 4, 1):
                    if x == j:
                        GPIO.output(stepPads[j], True)
                    else:
                        GPIO.output(stepPads[j], False)
                time.sleep(speed)
    else:
        print("WRONG DIRECTION ENTERED!")

while True:
    numSteps = int(input("Enter Number of Steps: "))
    Freq = float(input("Enter Frequency: "))
    Dir = input("Enter Direction: ").strip().upper()
    motorDrive(numSteps, Freq, Dir)
