###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################

stage.set_background ("winter")

q1 = codesters.Square(100, 100, 200, 'gray')
q2 = codesters.Square(-100, 100, 200, 'yellow')
q3 = codesters.Square(-100, -100, 200,'red')

s1 = codesters.Sprite("KendrickLamar", 100, 100)
s1.set_size(0.2)
s2 = codesters.Sprite("mclaren", -100,-100)
s2.set_size(0.2)    
s3 = codesters.Sprite("dog", 100, -100)             
s3.set_size(0.3)
s4 = codesters.Sprite("pinetree", -100, 100)
s4.set_size(0.4)

message1 = codesters.Text("My name is Sid",0,220,"red")
message2 = codesters.Text("I like dogs",0,-220,"black")