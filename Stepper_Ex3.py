
#git clone https://github.com/Majdawad88/ECET411_Stepper.git

#git clone https://github.com/Majdawad88/ECET411_Stepper.git

import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)  # Ignore warnings
stepPads = [19, 13, 6, 5]
stepPadsStatus = [0, 0, 0, 0]
GPIO.setmode(GPIO.BCM)
for i in range(0, 4):
        GPIO.setup(stepPads[i], GPIO.OUT)

def motorDrive(numberSteps, Frequency, Direction):
        speed = float(1 / Frequency)
        if Direction == 'R':
                print("Reverse")
                for k in range(0, numberSteps // 4):
                        print("Step Number = ", k)
                        for x in range(3, -1, -1):
                                for j in range(0, 4):
                                        if x == j:
                                                GPIO.output(stepPads[j], True)
                                                stepPadsStatus[j] = 1
                                        else:
                                                GPIO.output(stepPads[j], False)
                                                stepPadsStatus[j] = 0
                                print(stepPadsStatus)
                                time.sleep(speed)
        elif Direction == 'F':
                print("Forward")
                for k in range(0, numberSteps // 4):
                        print("Step Number = ", k)
                        for x in range(0, 4, 1):
                                for j in range(0, 4):
                                        if x == j:
                                                GPIO.output(stepPads[j], True)
                                                stepPadsStatus[j] = 1
                                        else:
                                                GPIO.output(stepPads[j], False)
                                                stepPadsStatus[j] = 0
                                print(stepPadsStatus)
                                time.sleep(speed)
        else:
                print("WRONG DIRECTION ENTERED!")
        for p in stepPads:              # release coils after move
                GPIO.output(p, False)

try:
        while True:
                numSteps = int(input("Enter Number of Steps: "))
                Freq = float(input("Enter Frequency: "))
                Dir = input("Enter Direction: ").strip().upper()
                motorDrive(numSteps, Freq, Dir)
except KeyboardInterrupt:
        GPIO.cleanup()

						
