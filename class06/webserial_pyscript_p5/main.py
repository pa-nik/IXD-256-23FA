import js as p5
from js import document

data = None

def setup():
  p5.createCanvas(300, 300)
  print('hello p5!')

def draw():
  p5.background(255)

  global data
  data = document.getElementById("data").innerText
  
  circle_size = int(data)
  p5.noStroke()
  p5.fill(150)
  p5.ellipse(150, 150, circle_size, circle_size)

def print_test(x):
  print(x)

  
