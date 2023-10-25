import js as p5
from js import document

data_string = None
data_list = None
sensor_val = None

def setup():
  p5.createCanvas(300, 300)
  # change mode to draw rectangles from center:
  p5.rectMode(p5.CENTER)

def draw():
  p5.background(255)
  global data_string, data_list, sensor_val

  # assign content of "data" div on index.html page to variable:
  data_string = document.getElementById("data").innerText
  # split data_string by comma, making a list:
  data_list = data_string.split(',')

  # assign first item of data_list to sensor_val:
  sensor_val = int(data_list[0])

  p5.noStroke()  # disable stroke
  # fill function can take 1 argument (gray)
  p5.fill(0)  # black fill
  
  # draw circle changing size with sensor data:
  # ellipse function takes (x, y, width, height)
  p5.ellipse(75, 75, sensor_val, sensor_val)
  
  # draw square changing color with sensor data:
  # fill function can take (red, blue, green)
  p5.fill(sensor_val, 0, 255 - sensor_val)  
  # rectangle function takes (x, y, width, height)
  p5.rect(225, 75, 100, 100)
  