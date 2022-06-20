from hashlib import new
from os import remove
from pyexpat import model
from turtle import mode, position
from ursina import *
from ursina.prefabs.\
    first_person_controller \
        import FirstPersonController
        
app = Ursina()
Sky(texture = 'sky')
player = FirstPersonController()

boxes = []
for n in range(12):
    for k in range(12):
        box = Button(
            color = color.green,
            model = 'cube',
            position = (k,0,n),
            texture = load_texture('grass.jpg'),
            parent = scene,
            origin_y = 0.5
        )
        boxes.append(box)
        
        
        sword = Entity(
            model = 'blade',
            texture = load_texture('sword.png'),
            rotation = (30,-40),
            position = (0.5,-0.6),
            parent = camera.ui,
            scale = (0.2,0.15)
            )
    
    def update():
        if held_keys ['left mouse']:
            sword.position = (0.4,-0.5)
        elif held_keys ['right mouse']:
            sword.position = (0.4,-0.5)
        else:
            sword.position = (0.5,-0.6)
            
            
    def input(key):
        for box in boxes:
            if box.hovered:
                if key == 'left mouse down':
                    new = Button (
                        color = color.brown,
                        model = 'cube',
                        position = box.position + mouse.normal,
                        texture = load_texture('soil.jpg'),
                        parent = scene,
                        origin_y = 0.5
                    ) 
                    boxes.append(new)
                if key == 'right mouse down':
                    boxes.remove(box)
                    destroy(box)

                

app.run()