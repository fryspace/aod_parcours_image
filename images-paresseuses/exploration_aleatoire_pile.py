#!/usr/bin/env python3

"""
exploration d'une image aleatoire avec une pile
"""

from image import Image
from algos import exploration_tas_ordonné, animer, exploration, exploration_tas
from utils import limitation_memoire
import matplotlib.pyplot as pl
import numpy as np


def main():
    """
    creation d'une image aleatoire avec 30% de chance que chaque pixel
    soit noir puis on explore a l'aide d'une pile en generant une animation.
    """
    for taille in range(32, 600, 16):
        img = Image.aleatoire(taille, 30)
        print(taille, end=" ")
        animer(img, exploration_tas_ordonné(img), fichier="bidule.gif")
        
    #pl.plot(np.array(taille), np.array(taille_pile), "-r")
    #pl.plot(np.array(taille), np.array(taille_tas), "-b")
    #pl.plot(np.array(taille), np.array(taille_entrelacer), "-y")
    #pl.title("nombre_pixels")
    #pl.legend("pile", "tas", "entrelacer")
    #pl.show()


    
    # limitation_memoire()  # decommentez-moi pour voir si ca passe
    #animer(img, exploration_tas_ordonné(img), fichier="exploration_aleatoire_entrelacer.gif")


if __name__ == "__main__":
    main()
