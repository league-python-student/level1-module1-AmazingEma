
def setup():
    # 1. Use the size function to set the size of your sketch
    size (800,600)
    # 2. Create 2 global variables for the background and the frog
    # using the loadImage("frog.png") function. For example:
    # global bg, frog
    # bg = loadImage("froggerBackground.png")
    
    # 3. Use the resize method to set the size of the background variable
    # to the width and height of the sketch. Resize the frog to an
    # appropriate size.
    
    global frog_x, frog_y, frogxspeed, frogyspeed
    frog_x = 500
    frog_y = 300
    frogxspeed = 0
    frogyspeed = 0
    global car1
    car1 = Car(100,200,100,2)
    global car2
    car2 = Car(400,300,200,1)
    
def draw():
    global frog_x, frog_y,frogxspeed, frogyspeed
    # 4. Use the background function to draw the background
    background(0)
    fill(60,120,30);
    ellipse(frog_x, frog_y, 50, 50);
    frog_x += frogxspeed
    frog_y += frogyspeed
    # 5. Use the image function to draw the frog.
    # Run the program and check the background and frog are displayed.

    # 6. Create global frog_x and frog_y variables in the setup function
    # and use them when drawing the frog. You will also have to put the
    # following in the draw function:
    if frog_x > 800:
        frog_x = 0
    elif frog_x < 0:
        frog_x = 800
    if frog_y > 600:
        frog_y = 0
    elif frog_y < 0:
        frog_y = 600
        
    car1.draw()
    car1.update()
    
    car2.draw()
    car2.update()
        
    if intersects(car1):
        frog_x = 800
        frog_y = 600
    if intersects(car2):
        frog_x = 800
        frog_y = 600
    
def keyPressed():
    global frog_x, frog_y, frogyspeed, frogxspeed
    if key == CODED:
        if keyCode == UP:
            frogyspeed = -10
            # Frog Y position goes up
            
            print("up")
        elif keyCode == DOWN:
            frogyspeed = 10
            # Frog Y position goes down
            print("down")
        elif keyCode == RIGHT:
            frogxspeed = 10
            # Frog X position goes right
            print("right")
        elif keyCode == LEFT:
            frogxspeed = -10
            # Frog X position goes left
            print("left")
            
def keyReleased():
    
    global frogyspeed, frogxspeed
    if key == CODED:
        if keyCode == UP:
            frogyspeed = 0
            # Frog Y position goes up
            print("up")
        elif keyCode == DOWN:
            frogyspeed = 0
            # Frog Y position goes down
            print("down")
        elif keyCode == RIGHT:
            frogxspeed = 0
            # Frog X position goes right
            print("right")
        elif keyCode == LEFT:
            frogxspeed = 0
            
    # 7. Use the Car class below to create a global car object in the
    # setup function and call the update and draw functions here.

    

    # 8. Create an intersects method that checks whether the frog collides
    # with the car. If there's a collision, move the frog back to the starting
    # point.
    # 9. Create more car objects of different lengths, speed, and size

def intersects(car):
    
  if frog_y > car.y and frog_y < car.y + 50 and frog_x > car.x and frog_x < car.x + car.length:
    return True
  else:
    return False

class Car:
    def __init__(self, x, y, length, speed):
        self.x = x
        self.y = y
        self.length = length
        self.speed = speed
        
        self.car_image = loadImage("carRight.png")
        if self.speed < 0:
            self.car_image = loadImage("carLeft.png")
        
        self.car_image.resize(self.length, self.length / 3)
        
    def draw(self):
        image(self.car_image, self.x, self.y)
    
    def update(self):
        self.x += self.speed
        
        if self.x > width:
            self.x = -self.length
            
        if self.x < -self.length:
            self.x = width
