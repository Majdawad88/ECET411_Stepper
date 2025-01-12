
#git clone https://github.com/Majdawad88/ECET411_Stepper.git

import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False) # Ignore warning for now stepPads = [19,13,6,5]
stepPads = [19,13,6,5]
stepPadsStatus = [0,0,0,0]
GPIO.setmode(GPIO.BCM)
for i in range(0,4):
        GPIO.setup(stepPads[i], GPIO.OUT)
def motorDrive(numberSteps, Frequency, Direction):
        speed = float(1/Frequency)
        if Direction == 'R':
                print("Reverse")
                for k in range(0, numberSteps):
                        print("Stepp Number = ", k)
                        for x in range(3,-1,-1):
                                for j in range(3,-1,-1):
                                        if x == j:
                                                GPIO.output(stepPads[j],True)
                                                stepPadsStatus[j] = 1
                                        else:
                                                stepPadsStatus[j] = 0
                                                GPIO.output(stepPads[j],False)

                                        time.sleep(speed)
                                print(stepPadsStatus)
        elif Direction == 'F':
                print("Forward")
                for k in range(0, numberSteps):
                        print("Stepp Number = ", k)
                        for x in range(0,4,1):
                                for j in range(0,4,1):
                                        if x == j:
                                                GPIO.output(stepPads[j],True)
                                                stepPadsStatus[j] = 1
                                        else:
                                                GPIO.output(stepPads[j],False)
                                                stepPadsStatus[j] = 0

                                        time.sleep(speed)
                                print(stepPadsStatus)
        else:
                print("WRONG DIRECTION ENTERED!")
while True:
        numSteps = int(input("Enter Number of Steps: "))
        Freq = float(input("Enter Frequency: "))
        Dir = input("Enter Direction: ")
        motorDrive(numSteps, Freq, Dir)


						
