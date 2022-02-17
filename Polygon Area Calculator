class Rectangle():
  def __init__(self, width, height):
    self.w = width
    self.h = height

  def set_height(self, value):
    self.h = value

  def set_width(self,value):
    self.w = value
  
  def get_area(self):
    return self.w * self.h

  def get_perimeter(self):
    return 2 * self.w + 2 * self.h
  
  def get_diagonal(self):
    return (self.w ** 2 + self.h ** 2) ** .5

  def get_picture(self):
    if self.w > 50 or self.h > 50:
      return "Too big for picture."
    pic = ""
    
    layer = "*" * self.w
    for i in range(self.h):
      pic += layer + "\n"

    return pic

  def __str__(self):
    return f"Rectangle(width={self.w}, height={self.h})"

  def get_amount_inside(self, obj):
    w_1, h_1 = obj.w, obj.h

    width = self.w // w_1
    height = self.h  // h_1

    if width >= 1 and height >= 1:
      return width * height
    else:
      return 0

class Square(Rectangle):
  def __init__(self, side):
    self.s = side
    self.w = side
    self.h = side

  def set_side(self, value):
    self.s = value
    self.w = value
    self.h = value
  
  def __str__(self):
    return f"Square(side={self.w})"
  
  def set_width(self, value):
    self.s = value
    self.w = value
    self.h = value

  def set_height (self, value):
    self.s = value
    self.w = value
    self.h = value
