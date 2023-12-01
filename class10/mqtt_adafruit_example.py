import os, sys, io
import M5
from M5 import *
from umqtt import *
from hardware import *

mqtt_client = None
user_name = 'INSERT_YOUR_AIO_USERNAME'

def setup():
  global mqtt_client

  M5.begin()
  mqtt_client = MQTTClient(
      'testclient',
      'io.adafruit.com',
      port=1883, 
      user=user_name,
      password='INSERT_YOUR_AIO_PASSWORD',
      keepalive=0
  )
  mqtt_client.connect(clean_session=True)


def loop():
  global mqtt_client
  M5.update()
  if BtnA.wasPressed():
    print('button pressed..')
    mqtt_client.publish(user_name+'/feeds/button-feed', 'press..', qos=0)


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
