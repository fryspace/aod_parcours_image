#!/usr/bin/env python3

"""
exploration d'une image aleatoire avec une pile
"""

from image import Image
from algos import animer, exploration
from imagep import ImageParesseuse
from utils import limitation_memoire
import matplotlib.pyplot as pl
import numpy as np

def main():
    """
    creation d'une image aleatoire avec 30% de chance que chaque pixel
    soit noir puis on explore a l'aide d'une pile en generant une animation.
    """

    #limitation_memoire() 
    img = Image.aleatoire(256, 30)
    animer(img, exploration(img), fichier="exploration_pile.gif")


if __name__ == "__main__":
    main()
