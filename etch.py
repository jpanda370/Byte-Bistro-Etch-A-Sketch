import random

canvas = 0
frame = 0
point = {'x': 0, 'y': 0}
media = 0

def init():
  global point, canvas, media
  setMediaFolder("/home/michael/Documents/CST 205/JES/final/Byte-Bistro-Etch-A-Sketch")
  canvas = makeEmptyPicture(700,500)
  frame = makePicture("frame.png")
  copyInto(frame, canvas, 0 ,0 )
  point['x'] = getWidth(canvas)/2;
  point['y'] = getHeight(canvas)/2;
  show(canvas)
  
def dial(x, y):
  if (point['x'] + x > 80) and (point['x'] + x <= 620):
    addLine(canvas, point['x'], point['y'], point['x']+ x, point['y']+ y )
    point['x'] += x
    point['y'] += y
    repaint(canvas)
  
def shake(shakecount, canvas):
  if shakecount >= 3:
    canvas = makeEmptyPicture(700,500)
    frame = makePicture("frame.png")
    copyInto(frame, canvas, 0 ,0 )
    repaint(canvas)
    return 0
  for x in range(80, 620, random.randint(1, 4)):
    for y in range(73, 425, random.randint(1, 4)):
      p = getPixel(canvas, x, y)
      r = random.randint(1, 2)
      if r == 1:
        setColor(p, makeColor(255, 255, 255))
  repaint(canvas)
  return (shakecount + 1)

def getChars(char, str, len):
  press = 0
  for key in str:
    if key == char:
      press += len  
  return press
       
def main():
  init()
  draw = true
  len = 20
  shakecount = 0
  
  while(draw):
    str = requestString("What would you like to do? (r, l, rl, -rl, -r, -l, exit, shak")
    x = 0
    y = 0
    if(str == 'shake'):
      shakecount = shake(shakecount, canvas)
      continue;
    if(str == "exit"):
       draw = false
    y += getChars('s', str, len)
    y -= getChars('w', str, len)
    x += getChars( 'd', str, len)
    x -= getChars( 'a', str, len)
    dial(x,y)
