import js as p5
from js import document

data_string = None
data_list = None
sensor_val = None
button_val = None

def setup():
  p5.createCanvas(300, 300)

def draw():
  p5.background(255)
  global data_string, data_list
  global sensor_val, button_val

  # assign content of "data" div on index.html page to variable:
  data_string = document.getElementById("data").innerText
  # split data_string by comma, making a list:
  data_list = data_string.split(',')

  # assign 1st item of data_list to sensor_val:
  sensor_val = int(data_list[0])
  # assign 2nd item of data_list to sensor_val:
  button_val = int(data_list[1])

  p5.fill(0)
  p5.text('sensor_val = ' + str(sensor_val), 10, 20)
  p5.text('button_val = ' + str(button_val), 10, 35)

  # change fill color with button value:
  if(button_val == 0):
    p5.fill(0)  # black fill
  else:
    p5.fill(255, 0, 0)  # red fill

  # change circle size with sensor value:
  p5.ellipse(150, 150, sensor_val, sensor_val)
  
  