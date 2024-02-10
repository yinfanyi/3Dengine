from model import *

class Scene:
    def __init__(self, app) -> None:
        self.app = app
        self.objects = []
        self.load()
        # print(self.objects)
        self.skybox = SkyBox(app)
        
    def add_object(self, obj):
        self.objects.append(obj)
        
    def load(self):
        app = self.app
        add = self.add_object
        
        n, s = 30, 3
        for x in range(-n, n, s):
            for z in range(-n, n, s):
                add(Cube(app, tex_id=1, pos=(x, -s, z)))
        
        add(Cat(app, pos=(0, -2, -10), rot=(-90, 0, 0)))
        
    def render(self):
        for obj in self.objects:
            obj.render()
        self.skybox.render()
        