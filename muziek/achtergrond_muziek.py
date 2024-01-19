import pygame


def speel_achtergrond_muziek():
    pygame.mixer.init()
    pygame.mixer.music.load("../muziek/rivendell_muziek.mp3")
    pygame.mixer.music.play(-1)
