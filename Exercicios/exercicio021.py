# Toque um mp3 no python

import pygame

pygame.mixer.init()
pygame.mixer.music.load('./assets/musicas/beethoven_virus.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
