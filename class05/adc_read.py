# use analog-to-digital converter (ADC) to read analog input on pin G1,
# convert the value to 8 bits (0 - 255 range) and print it

import os, sys, io
import M5
from M5 import *
from hardware import *
import time

adc = None
adc_val = None

def setup():
  global adc, adc_val
  M5.begin()
  # configure ADC input on pin G1 with 11dB attenuation:
  adc = ADC(Pin(1), atten=ADC.ATTN_11DB)

def loop():
  global adc, adc_val
  M5.update()
  # read 12-bit analog value (0 - 4095 range):
  adc_val = adc.read()
  #print(adc_val)
  # convert adc_val from 12-bit to 8-bit (0 - 255 range):
  adc_val_8bit = map_value(adc_val, in_min = 0, in_max = 4095,
                           out_min = 0, out_max = 255)
  print(adc_val_8bit)
  time.sleep_ms(100)
  
# map an input value (v_in) between min/max ranges:
def map_value(in_val, in_min, in_max, out_min, out_max):
  v = out_min + (in_val - in_min) * (out_max - out_min) / (in_max - in_min)
  if (v < out_min): 
    v = out_min 
  elif (v > out_max): 
    v = out_max
  return int(v)

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

