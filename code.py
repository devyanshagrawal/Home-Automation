import RPi.GPIO as GPIO
import time

LED_PIN = 17
LED_PIN2 = 26
MOT_PIN = 4
MOT_PIN2 = 27
MOT_PIN3 = 22
MOT_PIN4 = 23
MOTION_SENSOR = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(MOTION_SENSOR, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(LED_PIN2, GPIO.OUT)
GPIO.setup(MOT_PIN, GPIO.OUT)
GPIO.setup(MOT_PIN2, GPIO.OUT)
GPIO.setup(MOT_PIN3, GPIO.OUT)
GPIO.setup(MOT_PIN4, GPIO.OUT)
GPIO.output(MOT_PIN, GPIO.HIGH)
GPIO.output(MOT_PIN2, GPIO.HIGH)
choicee = int(input("1->AUTOMATIC Mode;;2->Mannual: "))
flag = 0
while(1):
    if choicee == 1:
        if GPIO.input(MOTION_SENSOR)==0:
            GPIO.output(LED_PIN, GPIO.HIGH)
        else:
            GPIO.output(LED_PIN, GPIO.LOW)
    else:
        n = int(input("1->light1 on;;2->light1 off;;3->light2 on;;4->light2 off;;5->FAN on;;6->FAN off;;7->Reverse direction FAN: "))
        if(n==1):
            GPIO.output(LED_PIN, GPIO.HIGH)
        elif n==2:
            GPIO.output(LED_PIN, GPIO.LOW)
        elif n==3:
            GPIO.output(LED_PIN2, GPIO.HIGH)
        elif n==4:
            GPIO.output(LED_PIN2, GPIO.LOW)
        elif n==5:
            GPIO.output(MOT_PIN3, GPIO.HIGH)
            GPIO.output(MOT_PIN4, GPIO.LOW)
        elif n==6:
            GPIO.output(MOT_PIN3, GPIO.LOW)
            GPIO.output(MOT_PIN4, GPIO.LOW)
        elif n==7:
            GPIO.output(MOT_PIN3, GPIO.LOW)
            GPIO.output(MOT_PIN4, GPIO.HIGH)
        else:
            GPIO.cleanup()
