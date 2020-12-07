import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(16,GPIO.OUT)

my_pwm = GPIO.PWM(16,1)
my_pwm.start(50)

stopit = False

while(stopit != True):
        dutycycle = input("Enter ( 1 to QUIT) ")
        if dutycycle ==1:
                stopit = True
        my_pwm.ChangeDutyCycle(int(dutycycle))

GPIO.cleanup()
