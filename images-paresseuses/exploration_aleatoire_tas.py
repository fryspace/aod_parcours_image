#!/usr/bin/env python3

"""
exploration d'une image aleatoire avec une pile
"""

from image import Image
from algos import animer, exploration_tas
from imagep import ImageParesseuse
from utils import limitation_memoire
import matplotlib.pyplot as pl
import numpy as np

def main():
    """
    creation d'une image aleatoire avec 30% de chance que chaque pixel
    soit noir puis on explore a l'aide d'un tas en generant une animation.
    """
    #limitation_memoire()
    img = Image.aleatoire(256, 30)
    animer(img, exploration_tas(img), fichier="exploration_aleatoire_tas.gif")


if __name__ == "__main__":
    main()