# Programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame
pygame.mixer.init()
pygame.mixer.music.load('Desafio_21 - teste.mp3')
pygame.mixer.music.play()
pygame.event.wait()
