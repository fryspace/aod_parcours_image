#!/usr/bin/env python3

"""
exploration d'une image aleatoire avec une pile
"""

from image import Image
from algos import exploration_tas_ordonné, animer
from imagep import ImageParesseuse
from utils import limitation_memoire
import matplotlib.pyplot as pl
import numpy as np

def main():
    """
    creation d'une image aleatoire avec 30% de chance que chaque pixel
    soit noir puis on explore a l'aide d'un tas ordoné par entrelacement en generant une animation.
    """
    #limitation_memoire()
    img = Image.aleatoire(256, 30)
    animer(img, exploration_tas_ordonné(img), fichier="exploration_aleatoire_entrelacer.gif")


if __name__ == "__main__":
    main()