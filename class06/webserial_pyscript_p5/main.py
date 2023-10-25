import js as p5
from js import document

data_string = None
data_list = None
sensor_val = None

def setup():
  p5.createCanvas(300, 300)

def draw():
  p5.background(255)
  global data_string, data_list, sensor_val
  
  # assign content of "data" div on index.html page to variable: 
  data_string = document.getElementById("data").innerText
  # split data_string by comma, making a list:
  data_list = data_string.split(',')

  # assign first item of data_list to sensor_val:
  sensor_val = int(data_list[0])

  # draw circle responding to sensor data:
  p5.push()  # save transformation coordinates
  # move coordinates by (x, y):
  p5.translate(75, 75)
  p5.noStroke()  # disable stroke
  p5.fill(0)  # black fill
  # draw ellipse with (x, y, width, height): 
  p5.ellipse(0, 0, sensor_val, sensor_val)
  p5.push()  # restore transformation coordinates
  

  
