import pygame
print ('EEEEEEEUUUUUUUGHHHHhhhh')
pygame.init() #Inicia o pygame
pygame.mixer.music.load('lego-yoda-death-sound-effect.mp3') #O mp3 tem que estar na mesma pasta do programa
pygame.mixer.music.play()
input()
pygame.event.wait()