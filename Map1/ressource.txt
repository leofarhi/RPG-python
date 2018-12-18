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
rep=os.getcwd()+"//lib//"
sys.path.insert(0, rep)

with open(rep+"entité"+".txt", "r") as fic:
    i=fic.readline()
    eval(compile("entité_element="+str(i), '<string>', 'exec'))
    fic.close()
