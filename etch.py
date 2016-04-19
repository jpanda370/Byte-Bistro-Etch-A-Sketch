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
  
  while(draw):
    str = requestString("What would you like to do? (r, l, rl, -rl, -r, -l, exit, shak")
    x = 0
    y = 0
    if('s' in str):
       char = 's'
       y += getChars(char, str, len)
    if('w' in str):
       char = 'w'
       y -= getChars(char, str, len)
    if('d' in str):
       char = 'd'
       x += getChars(char, str, len)
    if('a' in str):
      char = 'a'
      x -= getChars(char, str, len)
    dial(x,y)
    if(str == "exit"):
       draw = false