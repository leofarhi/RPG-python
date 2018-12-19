import pygame
from pygame.locals import *
from win32api import GetSystemMetrics
import time
import os
import sys
from bs4 import BeautifulSoup
import urllib3
import requests
import texture
import entité
rep=os.getcwd()+"//lib//"
sys.path.insert(0, rep)
x=0
y=0
with open(rep+"entité"+".txt", "r") as fic:
    i=fic.readline()
    eval(compile("entité_element="+str(i), '<string>', 'exec'))
    fic.close()

def écrit(code,name):
    with open(rep+"//"+str(name)+".py", "w",encoding='utf-8', errors='ignore') as fic:
        fic.write(code)
        fic.close()
def game_refress(liste, x, y):

    for i in liste:
        eval("surface.blit("+str(i[0])+", ("+str(i[1]+x)+","+str(i[2]+y)+"))")
        
game_refress(entité_element, x, y)
