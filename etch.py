canvas = 0
frame = 0
point = {'x': 0, 'y': 0}
media = 0
def init():
  global point, canvas, media
  setMediaFolder("C:\Users\Bob\Documents\CSUMB\Python\Final\byte-bistro-etch-a-sketch\\")
  canvas = makeEmptyPicture(700,500)
  frame = makePicture("frame.png")
  copyInto(frame, canvas, 0 ,0 )
  point['x'] = getWidth(canvas)/2;
  point['y'] = getHeight(canvas)/2;
  show(canvas)
  
def dial(x, y):
  addLine(canvas, point['x'], point['y'], point['x']+ x, point['y']+ y )
  point['x'] += x
  point['y'] += y
  repaint(canvas)
  
def shake():
  p = getPixels(canvas)

def main():
  init()
  draw = true
  len = 5
  
  while(draw):
    str = requestString("What would you like to do? (r, l, rl, -rl, -r, -l, exit, shak")
    x = 0
    y = 0
    if('s' in str):
      y += len
    if('w' in str):
      y -= len
    if('d' in str):
      x += len
    if('a' in str):
      x -= len
    dial(x,y)
    if(str == "exit"):
       draw = false