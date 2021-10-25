#!/usr/bin/env python3

"""
exploration d'une image aleatoire avec une pile
"""

from image import Image
from algos import iterateur_bloc_v2,  vue_degagee
from imagep import ImageParesseuse
from utils import limitation_memoire
import matplotlib.pyplot as pl
import numpy as np

def main():
    """
    creation d'une image aleatoire avec 30% de chance que chaque pixel
    soit noir puis on regarde le nombre de défauts de cache pour chaque itérateur avec vue_dégagée
    """

    #limitation_memoire() 
    img = Image.aleatoire(384, 30)
    img.sauvegarde("fichier_paresseux.png")
    imgp=ImageParesseuse("fichier_paresseux.png")
    #vue_degagee(imgp, iterateur_ligne(imgp))
    #vue_degagee(imgp, iterateur_recursif(imgp))
    vue_degagee(imgp, iterateur_bloc_v2(imgp))
    print(imgp.bloc.cache_info())
    imgp.bloc.cache_clear()
    


if __name__ == "__main__":
    main()
