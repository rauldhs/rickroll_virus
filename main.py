from turtle import width
import urllib.request
from random import randint
import pyglet

gif = urllib.request.urlretrieve(
  'https://c.tenor.com/q0Ejci9EQhcAAAAi/rick-astley-rick-roll.gif',
   "rickroll.gif")


animation = pyglet.resource.animation("rickroll.gif")
animSprite = pyglet.sprite.Sprite(animation)

w = animSprite.width 
h = animSprite.height
r,g,b,alpha = 0.5,0.5,0.5,0.5


display = pyglet.canvas.Display()
screen = display.get_default_screen()
width = screen.width
height = screen.height

pyglet.gl.glClearColor(r,g,b,alpha)

print(""" ________  ___  ________  ___  __    ________  ________  ___       ___              
|\   __  \|\  \|\   ____\|\  \|\  \ |\   __  \|\   __  \|\  \     |\  \             
\ \  \|\  \ \  \ \  \___|\ \  \/  /|\ \  \|\  \ \  \|\  \ \  \    \ \  \            
 \ \   _  _\ \  \ \  \    \ \   ___  \ \   _  _\ \  \\\  \ \  \    \ \  \           
  \ \  \\  \\ \  \ \  \____\ \  \\ \  \ \  \\  \\ \  \\\  \ \  \____\ \  \____      
   \ \__\\ _\\ \__\ \_______\ \__\\ \__\ \__\\ _\\ \_______\ \_______\ \_______\    
    \|__|\|__|\|__|\|_______|\|__| \|__|\|__|\|__|\|_______|\|_______|\|_______|    
                                                                                    
                                                                                    
                                                                                    
                                ___      ___ ___  ________  ___  ___  ________      
                               |\  \    /  /|\  \|\   __  \|\  \|\  \|\   ____\     
                               \ \  \  /  / | \  \ \  \|\  \ \  \\\  \ \  \___|_    
                                \ \  \/  / / \ \  \ \   _  _\ \  \\\  \ \_____  \   
                                 \ \    / /   \ \  \ \  \\  \\ \  \\\  \|____|\  \  
                                  \ \__/ /     \ \__\ \__\\ _\\ \_______\____\_\  \ 
                                   \|__|/       \|__|\|__|\|__|\|_______|\_________\
                                                                        \|_________|""")

class WindowsDraw():  
    for window in range(0,4):
        window = pyglet.window.Window(width = w,height = h,resizable=True)
        x, y = window.get_location()
        window.set_location(x + randint(0,width), y + randint(0,height))
        @window.event
        def on_draw():  
            animSprite.draw()

pyglet.app.run()

