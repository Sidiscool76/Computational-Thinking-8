# Section 1: Setup
import codesters
from codesters import StageClass
stage = StageClass()

stage.set_background("moon")
s1 = codesters.Sprite("person1",0,-200)
s1.set_size(0.5)



# Section 2: define controls
def turn_left(sprite):
    heading = sprite.heading
    sprite.set_heading(heading + 5)

def turn_right(sprite):
       heading = sprite.heading
       sprite.set_heading(heading - 5)

def forward(sprite):
       sprite.forward(5)

def backwards(sprite):
       sprite.backwards(-5)
# Section 3: define hide and show 
def hide(sprite):
        sprite.hide()
s1.event_key("h", hide)
def show(sprite):
        sprite.show()
s1.event_key("g", show)


# Section 4: bind controls to specific keys
s1.event_key("w", forward)
s1.event_key("s", backwards)
s1.event_key("a", turn_left)
s1.event_key("d", turn_right)

# Section 5: reminder message
print("Game has started. Open the screen using PORTS to play")