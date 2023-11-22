from pico2d import *
import game_world
import game_framework
import random

class Ball:
    image = None

    def __init__(self, x = None, y = None):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x = x if x else random.randint(100, 1180)
        self.y = y if y else random.randint(100, 924)


    def set_background(self, bg):
        self.bg = bg
        self.x = random.randint(50, self.bg.w)
        self.y = random.randint(50, self.bg.h)

    def draw(self):
        sx, sy = self.x - self.bg.window_left, self.y - self.bg.window_bottom
        self.image.clip_draw(0, 0, 21, 21, sx, sy)
        # draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def handle_collision(self, group, other):
        match group:
            case 'boy:ball':
                game_world.remove_object(self)
                other.ball = self # 소년이 볼을 소유하도록.
                pass
            # case 'zombie:ball':
            #     other.ball = self