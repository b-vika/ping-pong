from pygame import *
window = display.set_mode((700,500))
display.set_caption('Пинг-понг ')
back = (207,204,77)

window.fill(back)

clock = time.Clock()
game = True
rel_time = False
finish = False
num_fire = 0
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        
    display.update()
    clock.tick(60) 



