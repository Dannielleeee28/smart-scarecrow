# sms_sender.py
import serial
import time

PHONE_NUMBER = "+639919019849"  # Change this to the target number

def send_sms(message):
    try:
        gsm = serial.Serial("/dev/serial0", baudrate=115200, timeout=1)
        time.sleep(1)
        gsm.write(b'AT\r')
        time.sleep(1)
        gsm.write(b'AT+CMGF=1\r')
        time.sleep(1)
        gsm.write(f'AT+CMGS="{PHONE_NUMBER}"\r'.encode())
        time.sleep(1)
        gsm.write((message + "\x1A").encode())  # Ctrl+Z
        time.sleep(3)
        gsm.close()
    except Exception as e:
        print("Failed to send SMS:", e)
