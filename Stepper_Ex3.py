#git clone https://github.com/Majdawad88/ECET411_Stepper.git

import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)  # Ignore warnings
stepPads = [19, 13, 6, 5]
GPIO.setmode(GPIO.BCM)
for i in range(0, 4):
        GPIO.setup(stepPads[i], GPIO.OUT)
        GPIO.output(stepPads[i], False)

def motorDrive(numberSteps, Frequency, Direction):
        seq = [[1, 0, 0, 0],
               [0, 1, 0, 0],
               [0, 0, 1, 0],
               [0, 0, 0, 1]]
        if Direction == 'R':
                print("Reverse")
                seq = seq[::-1]
        elif Direction == 'F':
                print("Forward")
        else:
                print("WRONG DIRECTION ENTERED!")
                return
        speed = 1.0 / Frequency
        for k in range(numberSteps):
                pattern = seq[k % 4]
                for j in range(4):
                        GPIO.output(stepPads[j], pattern[j])
                time.sleep(speed)
                if k % 256 == 0:
                        print("Step", k, pattern)
        print("Done:", numberSteps, "steps")
        for p in stepPads:              # release coils after move
                GPIO.output(p, False)

try:
        while True:
                numSteps = int(input("Enter Number of Steps: "))
                Freq = float(input("Enter Frequency: "))
                Dir = input("Enter Direction (F/R): ").strip().upper()
                motorDrive(numSteps, Freq, Dir)
except KeyboardInterrupt:
        GPIO.cleanup()
