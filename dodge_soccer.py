# Section 1 - Setup
import codesters, random
from codesters import StageClass
stage =  StageClass()
stage.disable_all_walls()

player = codesters.Sprite("goal")
player.goto(0, -200)
stage.set_background("field")

object_speed = -2

lives = 5


# Section 2 - Objects
def falling_object():
    global object_speed, lives
    if lives > 0:
        x = random.randint(-200, 200)
        y = 200
        object = codesters.Sprite("ball", x, y)
        object.set_size(1)
        object.set_y_speed(object_speed)
       
stage.event_interval(falling_object, 3)


# Section 3 - Collision
def collision(player, object):
    global lives

    if object.get_image_name() == "ball":
        stage.remove_sprite(object)
        lives -= 1
        if lives == 0:
            player.say(f"out of lives - you lose!,5")
        else:
            player.say(f"{lives} lives",0.5)

player.event_collision(collision)

# section 4 - Controls


# Right Key
def go_right():
    player.move_right(10)

player.event_key("right", go_right)

# Left Key
def go_left():
    player.move_left(10)

player.event_key("left", go_left)
