import time
from cpu import Chip8CPU
from screen import Screen


fontset = [
    0xF0, 0x90, 0x90, 0x90, 0xF0,		# 0
    0x20, 0x60, 0x20, 0x20, 0x70,		# 1
    0xF0, 0x10, 0xF0, 0x80, 0xF0,		# 2
    0xF0, 0x10, 0xF0, 0x10, 0xF0,		# 3
    0x90, 0x90, 0xF0, 0x10, 0x10,		# 4
    0xF0, 0x80, 0xF0, 0x10, 0xF0,		# 5
    0xF0, 0x80, 0xF0, 0x90, 0xF0,		# 6
    0xF0, 0x10, 0x20, 0x40, 0x40,		# 7
    0xF0, 0x90, 0xF0, 0x90, 0xF0,		# 8
    0xF0, 0x90, 0xF0, 0x10, 0xF0,		# 9
    0xF0, 0x90, 0xF0, 0x90, 0x90,		# A
    0xE0, 0x90, 0xE0, 0x90, 0xE0,		# B
    0xF0, 0x80, 0x80, 0x80, 0xF0,		# C
    0xE0, 0x90, 0x90, 0x90, 0xE0,		# D
    0xF0, 0x80, 0xF0, 0x80, 0xF0,		# E
    0xF0, 0x80, 0xF0, 0x80, 0x80		# F
]


def run():
    filename = 'space_invaders.ch8'
    screen = Screen(filename)
    cpu = Chip8CPU(screen)

    cpu.load_rom('FONTS.chip8', 0)
    # cpu.load_font(fontset)
    cpu.load_rom(filename)

    while True:
        # screen.draw_pixel(0, 0, 1)
        # screen.draw_pixel(0, 1, 1)
        # screen.draw_pixel(0, 2, 1)
        # screen.draw_pixel(0, 3, 1)
        # screen.draw_pixel(0, 4, 1)
        # screen.draw_pixel(1, 4, 1)
        # screen.draw_pixel(2, 4, 1)
        # screen.draw_pixel(3, 4, 1)
        # screen.draw_pixel(4, 4, 1)
        cpu.execute_instruction()
        screen.update()


if __name__ == "__main__":
    run()
