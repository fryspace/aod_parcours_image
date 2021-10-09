#!/usr/bin/env python3

"""
exploration d'une image aleatoire avec une pile
"""

from image import Image
from algos import exploration_tas_ordonné, animer
from utils import limitation_memoire


def main():
    """
    creation d'une image aleatoire avec 30% de chance que chaque pixel
    soit noir puis on explore a l'aide d'une pile en generant une animation.
    """

    img = Image.aleatoire(256, 30)
    # limitation_memoire()  # decommentez-moi pour voir si ca passe
    animer(img, exploration_tas_ordonné(img), fichier="exploration_aleatoire_ordonné.gif")


if __name__ == "__main__":
    main()
