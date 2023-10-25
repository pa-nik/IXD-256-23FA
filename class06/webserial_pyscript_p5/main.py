import js as p5
from js import document

data_string = None
data_list = None
sensor_val = None
button_val = None

# load image data and assign it to variable:
swirl_img = p5.loadImage('swirl.png')

# load font data and assign it to variable:
jellee_font = p5.loadFont('Jellee.otf')

def setup():
  p5.createCanvas(300, 300)
  # change mode to draw rectangles from center:
  p5.rectMode(p5.CENTER)
  # change mode to draw images from center:
  p5.imageMode(p5.CENTER)
  # change stroke cap to square:
  p5.strokeCap(p5.SQUARE)

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

  p5.noStroke()  # disable stroke
  # fill function can take 1 argument (gray)
  p5.fill(0)  # black fill
  
  # draw circle changing size with sensor data:
  # ellipse function takes (x, y, width, height)
  # map function takes (value, in_min, in_max, out_min, out_max)
  circle_size = p5.map(sensor_val, 0, 255, 25, 100)
  p5.ellipse(75, 75, circle_size, circle_size)
  
  # draw square changing color with sensor data:
  # fill function can take (red, green, blue)
  p5.fill(sensor_val, 0, 255 - sensor_val)  
  # rectangle function takes (x, y, width, height)
  p5.rect(225, 75, 100, 100)

  # draw text:
  p5.fill(255)  # white fill
  # use font installed on computer:
  p5.textFont('Courier')
  p5.textSize(18)
  p5.text(sensor_val, 190, 65)
  # use font from loaded font file:
  p5.textFont(jellee_font)
  p5.textSize(24)
  p5.text(button_val, 190, 100)

  # draw lines responding to button data:
  for i in range(8):
    if(button_val == 0):
      p5.strokeWeight(i+1)
    else:
      p5.strokeWeight(8-i)
    p5.stroke(0)
    # line function takes (x1, y1, x2, y2)
    x1 = x2 = 25 + i * 14
    y1 = 175
    y2 = 275
    p5.line(x1, y1, x2, y2)

  # draw image rotating with sensor data:
  p5.push()  # save transformation coordinates
  p5.translate(225, 225)  # move coordinates by (x, y)
  # use sensor_val as degrees converted to radians:
  angle = p5.radians(sensor_val)  
  p5.rotate(angle)  # rotate coordinates
  # image function takes (image, x, y, width, height)
  p5.image(swirl_img, 0, 0, 100, 100)
  p5.pop()  # restore transformation coordinates
