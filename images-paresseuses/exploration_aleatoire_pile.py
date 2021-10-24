#!/usr/bin/env python3

"""
exploration d'une image aleatoire avec une pile
"""

from image import Image
from algos import exploration_tas_ordonné, animer, exploration, exploration_tas, iterateur_bloc, iterateur_ligne, iterateur_recursif, vue_degagee
from imagep import ImageParesseuse
from utils import compte, limitation_memoire
import matplotlib.pyplot as pl
import numpy as np

def main():
    """
    creation d'une image aleatoire avec 30% de chance que chaque pixel
    soit noir puis on explore a l'aide d'une pile en generant une animation.
    """

    #limitation_memoire() 
    img = Image.aleatoire(256, 30)
    img.sauvegarde("fichier_paresseux.png")
    imgp=ImageParesseuse("fichier_paresseux.png")
    #animer(img, exploration_tas(img), fichier="bidule.gif")
    vue_degagee(imgp, iterateur_ligne(imgp))
    #print(imgp.bloc.cache_info())
    #imgp.bloc.cache_clear()
    #vue_degagee(imgp, iterateur_bloc(imgp))
    #iterateur_ligne(imgp)
    #print(compte(iterateur_ligne(imgp)))
    #print(compte(iterateur_bloc(imgp)))
    #iterateur_bloc(imgp)
    #print(imgp.bloc.cache_info())
    #print(imgp.bloc.cache_info())
    #imgp.bloc.cache_clear()
    #vue_degagee(imgp, iterateur_recursif(imgp))
    #print(imgp.bloc.cache_info())
    #imgp.bloc.cache_clear()
    #print(iterateur_recursif(imgp))
    
    #animer(img, exploration_tas_ordonné(img), fichier="exploration_aleatoire_entrelacer.gif")


if __name__ == "__main__":
    main()
