import pygame

import lib.display as display
from lib.task_timer import TaskTimer
from views.ahrs_element import AhrsElement


class Altitude(AhrsElement):
    def __init__(self, degrees_of_pitch, pixels_per_degree_y, font, framebuffer_size):
        self.task_timer = TaskTimer('Altitude')
        self.__font__ = font
        center_y = framebuffer_size[1] >> 2
        text_half_height = int(font.get_height()) >> 1
        self.__text_y_pos__ = center_y - text_half_height
        self.__rhs__ = int(framebuffer_size[0]) # was 0.9

    def render(self, framebuffer, orientation):
        self.task_timer.start()
        altitude_text = f"{int(orientation.alt)}' MSL"
        alt_texture = self.__font__.render(
            altitude_text, True, display.WHITE, display.BLACK)
        text_width, _text_height = alt_texture.get_size()

        framebuffer.blit(
            alt_texture, (self.__rhs__ - text_width, self.__text_y_pos__))
        self.task_timer.stop()


if __name__ == '__main__':
    import hud_elements
    hud_elements.run_ahrs_hud_element(Altitude)
