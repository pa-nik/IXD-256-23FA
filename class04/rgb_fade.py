# using loops and variables to fade RGB LEDs between red and green colors

import os, sys, io
import M5
from M5 import *
from hardware import *
import time

rgb = None
r = None
g = None

def setup():
  global rgb
  M5.begin()
  
  # default built-in RGB LED setting on M5 AtomS3 Lite:
  #rgb = RGB()
  
  # custom RGB setting using pin G35 (M5 AtomS3 Lite built-in LED):
  #rgb = RGB(io=35, n=1, type="SK6812")
  
  # custom RGB setting using pin G2 (M5 AtomS3 Lite bottom connector) and 10 LEDs:
  rgb = RGB(io=2, n=10, type="SK6812")  

def loop():
  global rgb, r, g
  M5.update()
  # loop to 100 increasing r, decreasing g values:
  for i in range(100):
    r = i
    g = 100 - i
    rgb.fill_color((r << 16) | (g << 8) | 0)
    time.sleep_ms(20)
  # loop to 100 decreasing r, increasing g values:
  for i in range(100):
    r = 100 - i
    g = i
    rgb.fill_color((r << 16) | (g << 8) | 0)
    time.sleep_ms(20)

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
