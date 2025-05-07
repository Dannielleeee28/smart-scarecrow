# sound_loop.py
import pygame

def play_sound():
    pygame.mixer.init()
    pygame.mixer.music.load("hawk.wav")
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play(-1)  # Loop forever
