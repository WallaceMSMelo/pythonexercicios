#from playsound import playsound
import pygame
# playsound('C:/Users/Wallace Melo/Music/Twelve_Carat_Toothache/01-Post-Malone-Reputation.mp3')

# resolução do professor
pygame.init()
pygame.mixer.music.load('teste.wav')
pygame.mixer.music.play()
input()
pygame.event.wait()