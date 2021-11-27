import numpy as np
from .values import *
import pygame as pg


class Visualize:
    def __init__(self, md, e=None, b=None, dead_path=None, viable_paths=None, final_array=None):
        if final_array is None:
            final_array = []
        if viable_paths is None:
            viable_paths = []
        if dead_path is None:
            dead_path = []
        self.md = md  # original maze at the beginning of the process
        assert (self.maze_is_valid())
        self.pix_s = 5
        self.size_x, self.size_y = self._get_maze_size()
        self.viable_paths = viable_paths
        self.dead_paths = dead_path
        self.final_array = final_array
        self.screen = pg.display.set_mode(((self.size_x * self.pix_s), self.size_y * self.pix_s))
        self.sp = b
        self.ep = e

    def maze_is_valid(self):

        a = self._get_maze_size()
        return a[0] <= MAX_SIZE or a[1] <= MAX_SIZE

    def _get_maze_size(self):
        return self.md.__len__(), self.md[0].__len__()

    def draw_board(self, ver=1):
        p_y = 0
        for row in self.md:
            # we need to draw rectangles next to each other
            p_x = 0
            for point in row:
                if point == 0:
                    pg.draw.rect(self.screen, (0, 0, 0), [p_x, p_y, self.pix_s, self.pix_s])
                else:
                    pg.draw.rect(self.screen, (225, 225, 225), [p_x, p_y, self.pix_s, self.pix_s])

                p_x += self.pix_s
            p_y += self.pix_s
        #  draw the end and start point
        self.render_endpoints()
        self.render_viable_path(v=ver)
        self.render_dead_paths(v=ver)
        self.render_final_array()

    def render_board(self, v=2):
        print(self.dead_paths)
        pg.display.flip()
        self.screen.fill((225, 225, 225))
        self.draw_board(ver=v)

        # handle events
        events = pg.event.get()

        for event in events:
            if event.type == pg.QUIT:
                exit()

        pg.time.wait(100)

    def render_endpoints(self):
        self.render_relative_point(self.sp, (0, 225, 0))
        self.render_relative_point(self.sp, (225, 0, 0))

    def render_viable_path(self, v=2):
        if v != 1:
            for path in self.viable_paths:
                for point in path:
                    self.render_relative_point(point, (0, 225, 0))

        else:
            for point in self.viable_paths:
                self.render_relative_point(point, (0, 225, 0))

    def render_dead_paths(self, v=2):
        if v != 1:
            for path in self.dead_paths:
                for point in path:
                    self.render_relative_point(point, (225, 225, 0))
        else:
            for point in self.dead_paths:
                self.render_relative_point(point, (225, 225, 0))

    def render_final_array(self):
        for path in self.final_array:
            for point in path:
                self.render_relative_point(point, (225, 0, 0))

    def render_relative_point(self, coordinates, color):
        print(f'coordinates : {coordinates[1]} {coordinates[0]}')
        pg.draw.rect(self.screen,
                     color,
                     [(coordinates[1] * self.pix_s), (coordinates[0] * self.pix_s), self.pix_s, self.pix_s])

