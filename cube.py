from ursina import *
from rotation import ROTATION_DICTIONARY


class RubiksCube(Ursina):
    ROTATION_SPEED = 0.5

    def __init__(self):
        super().__init__()
        self.set_up_window()
        self.set_up_camera()
        self.cube = []
        self.action_trigger = True
        self.center = Entity()
        self.create_cube()

    @staticmethod
    def set_up_window():
        window.borderless = False
        window.size = (800, 800)
        window.color = color.black
        window.position = (200, 200)

    @staticmethod
    def set_up_camera():
        camera.position = (5.7, 6.5, -10)
        camera.rotation_x = 30
        camera.rotation_y = -30

    def rotation_trigger(self):
        self.action_trigger = not self.action_trigger

    def create_cube(self):
        texture_number = 1

        for x in range(-1, 2):
            for y in range(-1, 2):
                for z in range(-1, 2):
                    self.cube.append(Entity(model='model/cube.obj',
                                            texture=f'textures/{texture_number}.png',
                                            position=(x, y, z),
                                            scale=0.48))
                    texture_number += 1

    def side_for_rotation(self, axis, shift, is_rotate_all_cube=False):
        for c in self.cube:
            c.position, c.rotation = round(c.world_position, 1), c.world_rotation
            c.parent = scene

        self.center.rotation = 0

        for c in self.cube:
            if is_rotate_all_cube:
                c.parent = self.center

            elif eval(f'c.position.{axis}') == shift:
                c.parent = self.center

    def rotate(self, key):
        axis, shift, angle, is_rotate_all_cube = ROTATION_DICTIONARY[key]
        self.side_for_rotation(axis, shift, is_rotate_all_cube)
        self.action_trigger = False
        eval(f'self.center.animate_rotation_{axis} ({angle}, duration=self.ROTATION_SPEED)')
        invoke(self.rotation_trigger, delay=self.ROTATION_SPEED + 0.11)

    def input(self, key):
        if not (key in ROTATION_DICTIONARY and self.action_trigger):
            return
        self.rotate(key)
