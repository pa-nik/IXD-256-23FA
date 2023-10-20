import js as p5
from js import document

data = None

def setup():
  p5.createCanvas(400, 400)
  #print('assignment 2 template')

def draw():
  p5.background(255)

  global data
  data_string = document.getElementById("data").innerText
  data_list = data_string.split(',')
  data = data_list[0]
  button_val = int(data_list[1])

  p5.text(int(data), 10, 20)
  p5.text(button_val, 10, 30)

  p5.noStroke()
  p5.fill(150)
  #p5.ellipse(150, 150, circle_size, circle_size)
  p5.push()
  # set angle variable to integer of data
  angle = int(data)
  # move to middle of canvas
  p5.translate(p5.width/2, p5.height/2)
  if(button_val == 0):
    # rotate canvas with angle converted from degrees to radians:
    p5.rotate(p5.radians(angle))
    # change mode to draw rectangles from center:
    p5.rectMode(p5.CENTER)
    # fill with gray responding to data:
    p5.fill(int(data))

    # draw rectangle at coordinate 0, 0 and 100 width and height:
    p5.rect(0, 0, 100, 100)
  else:
    circle_size = int(data)
    # fill with red color:
    p5.fill(255, 0, 0)
    p5.ellipse(0, 0, circle_size, circle_size)
  # rectore graphical transformation:
  p5.pop()




  
