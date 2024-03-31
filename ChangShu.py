# skeleton code for project 2
# vis 142 fall 2023 
# This can take 20 minutes to hours to run.

# imports, don't change these without consulting. It does not hurt to add. 
import pygame
from pygame.locals import *
from sys import exit
import random
import time
import math
# record the start time
start_time = time.time()

#####################################################################
# We will be producing FHD video from an image sequence
# Your software creates the image sequence at
# 1920 x 1080.
# You might want to work at 720p (1280x720) for production
# And then change these back to 1920 x 1080 for production.
# On the other hand, you will have to deal with scaling issues if you do.
#####################################################################
width = 1920
height = 1080

#####################################################################
# Name and title, update to your name and title!
#####################################################################
name = "Chang Shu"
title = "Blue-Theme Wave Pattern"

#####################################################################
# IMPORTANT - you will get your start sequence number from your TA
# If you use the default number 1000000 below, your work will not 
# be part of the class reel, as in every student must have different
# start sequence numbers.
#####################################################################
start_sequence_num = 7160000 # CHANGE HERE

# Do not change these variables
# normal pygame stuff
clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Blue-Theme Wave Pattern')
frame_num = start_sequence_num
titles_font = pygame.font.SysFont(None, int(width/12)) # if name or title run off screen, try setting the literal to 16 instead of 12
name_f = titles_font.render(name, True, (255,255,255))
title_f = titles_font.render(title, True, (255,255,255))

# print resolution warning
if (width != 1920 and height != 1080):
    print("Warning: dimensions not FHD, be sure width and height are set to 1920 and 1080.")

# this function makes one second of black frames
def make_black():
    global frame_num
    screen.fill((0,0,0))
    pygame.display.update()
    for i in range(0, 60):
    #    pygame.image.save(screen, "/Users/shuchang/Desktop/animation/ChangShu/" + str(frame_num) + ".png")
       frame_num = frame_num + 1
       clock.tick(60)
        
#############################################################
# this object is just for example purposes - Don't use this class
# unless of course to change it to be different from my circle foo
# using objects will make project 2 generally easier however

# Wave Pattern Settings
grid_rows, grid_cols = 10, 20  # Grid size
wave_amplitude = 100  # Wave height
wave_frequency = 0.2  # Wave frequency

# Function to generate a variation of blue color
def random_blue_color():
    red = random.randint(100, 140)  # Lower red
    green = random.randint(150, 180)  # Moderate green
    blue = random.randint(200, 220)  # High blue
    return (red, green, blue)


class MovingShape:
    def __init__(self, row, col, screen_width, screen_height):
        self.shape_type = random.choice(['rect', 'circle', 'ellipse', 'triangle'])
        self.color = random_blue_color()
        self.cell_width = screen_width // grid_cols
        self.cell_height = screen_height // grid_rows
        self.width = random.randint(50, min(100, self.cell_width))
        self.height = random.randint(50, min(100, self.cell_height))
        self.grid_x = col * self.cell_width + (self.cell_width - self.width) // 2
        self.grid_y = row * self.cell_height + (self.cell_height - self.height) // 2
        self.row = row
        self.col = col
        
    def draw(self, surface, t):
        wave_offset = math.sin(t * wave_frequency + self.col * 0.5) * wave_amplitude
        x = self.grid_x
        y = self.grid_y + wave_offset

        if self.shape_type == 'rect':
            pygame.draw.rect(surface, self.color, (x, y, self.width, self.height))
        elif self.shape_type == 'circle':
            radius = min(self.width, self.height) // 2
            pygame.draw.circle(surface, self.color, (x + radius, y + radius), radius)
        elif self.shape_type == 'ellipse':
            pygame.draw.ellipse(surface, self.color, (x, y, self.width, self.height))
        elif self.shape_type == 'triangle':
            point1 = (x, y + self.height)
            point2 = (x + self.width // 2, y)
            point3 = (x + self.width, y + self.height)
            pygame.draw.polygon(surface, self.color, [point1, point2, point3])

# Function to update and draw each shape with a wave effect
def draw_shape_with_wave(surface, shape, t, amplitude, frequency):
    # Calculate the wave offset using a sine function
    wave_offset = math.sin(t * frequency) * amplitude
    
    # Update the shape's y position with the wave offset
    shape.grid_y = wave_offset + (shape.row * height // grid_rows)
    
    # Draw the shape
    shape.draw(surface, t)

################################ end object

# this is the credits loop, which puts the title of your work
# and your name on the screen
make_black() # one second black
# produce title sequence
screen.fill((0,0,0))
screen.blit(name_f, (int(width/8), int(width/8)))
screen.blit(title_f, (int(width/8), int(width/4))) 
for i in range(0, 3*60):
    pygame.display.update()
    # pygame.image.save(screen, "/Users/shuchang/Desktop/animation/ChangShu/" + str(frame_num) + ".png")
    frame_num = frame_num + 1
    clock.tick(60)
make_black() # one second black

# make a list of moving things
moving_shapes = [MovingShape(row, col, width, height) for row in range(grid_rows) for col in range(grid_cols)]

# here is the main animation loop
#for i in range(0, 20*60): # 20*60 frames is 20 seconds
i = 0
#while int((time.time() - start_time)) < 20:
while i < 20*60:
    #########################################################
    # in the skeleton, your animation goes from here ########
    #########################################################
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.display.quit()
            pygame.quit()
            exit()
    
    screen.fill((0,0,0))
    t = i / 60.0  # Current time in seconds
    for shape in moving_shapes:
        draw_shape_with_wave(screen, shape, t, wave_amplitude, wave_frequency)
    #########################################################
    # to here ###############################################
    #########################################################

    # The next line can be commented out to speed up testing frame rate
    # by not writing the file. But for output to final frames,
    # you will need to ucomment it.
    # pygame.image.save(screen, "/Users/shuchang/Desktop/animation/ChangShu/" + str(frame_num) + ".png")
    frame_num = frame_num + 1
    pygame.display.update()
    i += 1
    clock.tick(60)

# print out stats
print("seconds:", int(time.time() - start_time))
print("~minutes: ", int((time.time() - start_time)/60))
# we just quit here
pygame.display.quit()
pygame.quit()
exit()

# you can make your files into a movie with ffmpeg:
# ffmpeg -r 60 -start_number 1000000 -s 4096x2160 -i %d.png -vcodec libx264 -crf 5 -pix_fmt yuv420p final.mp4
# with a few changes such as to start number, but this is just extra info here