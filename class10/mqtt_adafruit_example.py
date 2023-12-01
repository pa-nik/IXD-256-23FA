import os, sys, io
import M5
from M5 import *
from umqtt import *
from hardware import *
import time

mqtt_client = None
user_name = 'INSERT_YOUR_AIO_USERNAME'
mqtt_timer = 0
adc = None
adc_val = None

def setup():
  global mqtt_client
  global adc
  M5.begin()
  mqtt_client = MQTTClient(
      'testclient',
      'io.adafruit.com',
      port=1883, 
      user=user_name,
      password='INSERT_YOUR_AIO_PASSWORD',
      keepalive=3000
  )
  mqtt_client.connect(clean_session=True)
  # configure ADC input on pin G8 with 11dB attenuation:
  adc = ADC(Pin(8), atten=ADC.ATTN_11DB)


def loop():
  global mqtt_client
  global mqtt_timer
  global adc, adc_val
  M5.update()
  # publish when button is pressed:
  if BtnA.wasPressed():
    print('button pressed..')
    mqtt_client.publish(user_name+'/feeds/button-feed', 'ON', qos=0)
  # publish when button is released:
  if BtnA.wasReleased():
    print('button released..')
    mqtt_client.publish(user_name+'/feeds/button-feed', 'OFF', qos=0)
  # publish every 2.5 seconds:
  if(time.ticks_ms() > mqtt_timer + 2500):
    # read 12-bit analog value (0 - 4095 range):
    adc_val = adc.read()
    # publisch analog value as a string:
    mqtt_client.publish(user_name+'/feeds/adc-feed', str(adc_val), qos=0)
    print('publish data..')
    # update timer:
    mqtt_timer = time.ticks_ms()  
      

if __name__ == '__main__':
  try:
    setup()
    while True:
      loop()
  except (Exception, KeyboardInterrupt) as e:
    try:
      from utility import print_error_msg
      print_error_msg(e)
    except ImportError:
      print("please update to latest firmware")
