"""
les algorithmes un peu costauds sont ici
"""
from itertools import takewhile, chain
from os import system
import tempfile
from imagep import Bloc, ImageParesseuse
from utils import voisins, compte


"""
Partie 1 : exploration et animation des gif
"""

def animer(image, etapes, fichier="animation.gif", pas=100):
    """
    genere un fichier
    montrant l'evolution de l'image toutes les 'pas' 'etapes'
    """
    image_dir = tempfile.TemporaryDirectory()
    compte_images = 0
    image.pbm("{}/{:07d}.pbm".format(image_dir.name, compte_images))
    compte_images += 1

    for numero_etape, _ in enumerate(etapes):
        if numero_etape % pas == 0:
            image.pbm("{}/{:07d}.pbm".format(image_dir.name, compte_images))
            compte_images += 1

    image.pbm("{}/{:07d}.pbm".format(image_dir.name, compte_images))
    compte_images += 1
    if system("convert -delay 10 -loop 1 {}/*.pbm {}".format(image_dir.name, fichier)):
        print("echec de la creation du gif.\
image magick (convert) est-il installe ?")


def exploration(image):
    """
    exploration (et modification)
    de l'image en profondeur d'abord,
    a l'aide d'une pile.
    on yield a chaque etape la pile.
    """
    def pixel_blanc(p):
        return not image.pixel(*p)
    taille_pile=0
    a_voir = [(0, 0)]
    while a_voir:
        if len(a_voir)>taille_pile:
            taille_pile = len(a_voir)
        
        courant = a_voir.pop()
        if pixel_blanc(courant):
            image.noircir_pixel(*courant)
            yield a_voir
            a_voir.extend(filter(pixel_blanc, voisins(image.taille, courant)))
    print(taille_pile)


def suppression(tab):
    s = len(tab) -1
    e = tab[s]
    i=0
    while(2*i+1 < s and e < tab[2*i+1])or(2*i+2 < s and e < tab[2*i+2]):
        if 2*i+2 < s and tab[2*i+1] < tab[2*i+2]:
            tab[i]=tab[2*i+2]
            i=2*i+2
        else:
            tab[i]=tab[2*i+1]
            i=2*i+1
    tab[i] = e
    tab.pop()

def insertion_tas(tab, elem):
    i=len(tab)
    tab.append(elem)
    while i>0 and elem > tab[int((i-1)/2)]:
        tab[i]=tab[int((i-1)/2)]
        i = int((i-1)/2)
    tab[i]=elem



def exploration_tas(image):
    """ 
    exploration en tas 
    """
    def pixel_blanc(p):
        return not image.pixel(*p)
    
    tas = [(0,0)]
    while tas:
        
        courant = tas[0]
        suppression(tas)
        if pixel_blanc(courant):
            image.noircir_pixel(*courant)
            yield tas
            new_vois = []
            new_vois.extend(filter(pixel_blanc, voisins(image.taille, courant)))
            for i in range(len(new_vois)):
                insertion_tas(tas, new_vois[i])
            




def entrelacement(t):
    abs, ord = t[0], t[1]
    a=bin(abs)
    b=bin(ord) #on a b du type b='0b010101'
    res = "0b"
    if len(a)>len(b):
        comp = ""
        for i in range(len(a)-len(b)):
            comp+="0"
        b=comp+b[2::] #on complète par des zeros
        a=a[2::] #on enlève la marque du binaire '0b'
        for i in range(len(a)):
            res+=b[i]
            res+=a[i]
    else:
        comp=""
        for i in range(len(b)-len(a)):
             comp+="0"
        a=comp+a[2::]
        b=b[2::]
        for j in range(len(b)):
            res+=b[j]
            res+=a[j]

    return int(res, 2)

def desentrelacement(t):
    abs, ord = "0b", "0b"
    a=bin(t)
    a=a[2::]
    i=0
    if len(a)%2!=0:
        a='0'+a
    while i<len(a):
        ord+=a[i]
        abs+=a[i+1]
        i+=2
    abs=int(abs, 2)
    ord=int(ord, 2)
    res=(abs, ord)
    return res


def exploration_tas_ordonné(image):
    def pixel_blanc(p):
        return not image.pixel(*p)
    tas=[entrelacement((0,0))]
    taille=0
    while tas:
        if (len(tas)>taille):
            taille=len(tas)
        courant = desentrelacement(tas[0])
        suppression(tas)
        if pixel_blanc(courant):
            image.noircir_pixel(*courant)
            yield tas
            new_vois = []
            new_vois.extend(filter(pixel_blanc, voisins(image.taille, courant)))
            for i in range(len(new_vois)):
                insertion_tas(tas, entrelacement(new_vois[i]))
    print(taille)


"""
Partie 2 : vue dégagée et les 3 itérateurs
"""


def iterateur_ligne(image):
    n= image.taille
    for i in range (0,n):
        for j in range (0, n):
            yield (i,j)


def iterateur_bloc(image):
    n=image.taille
    nombre_bloc_ligne = n//int(Bloc.TAILLE ** (1/2))
    nombre_point_ligne_bloc= n * int(Bloc.TAILLE ** (1/2))
    #on veut faire du blocking pour des blocs de taille 256, on doit donc se baser sur une taille de bloc 
    #telle que 2K²=256 avec K la longueur du bloc, pour cela on utilise la classe bloc
    for i in range(n**2//4):
        bloc=image.bloc(i)
        colonne_bloc= i % nombre_bloc_ligne
        ligne_bloc = i // nombre_bloc_ligne
        ligne_depart = ligne_bloc * int(bloc.TAILLE ** (1/2))
        colonne_depart = colonne_bloc * int(bloc.TAILLE ** (1/2))
        for j in range(0, bloc.TAILLE):
            k = ligne_depart + j // int(bloc.TAILLE ** (1/2))
            l= colonne_depart + j % int(bloc.TAILLE ** (1/2))
            yield (k,l)


def iterateur_recursif(image):
    n=image.taille
    yield from decoupage(n, (0,0))
    
                
def decoupage(n, debut):
    x, y = debut
    if n == 2:
        for tuple in [(x,y), (x, y+1), (x+1, y), (x+1, y+1)]:
            yield tuple
    else:
        yield from decoupage(n//2, (x,y))
        yield from decoupage(n//2, (x, y + int(n//2)))
        yield from decoupage(n//2, (x + int(n//2) , y ))
        yield from decoupage(n//2, (x + int(n//2) , y + int(n //2)) )



def vue_degagee(image, iterateur_pixels):
    """
    renvoie la position avec la meilleure vue
    """
    def pixel_blanc(pixel):
        return not image.pixel(*pixel)
    
    #l=[0]

    def vue_pixel(pixel):
        def vision(pixels):
            return takewhile(pixel_blanc, pixels)

        ligne, colonne = pixel
        haut = vision((l, colonne) for l in reversed(range(0, ligne)))
        bas = vision((l, colonne) for l in range(ligne+1, image.taille))
        vertical = chain(haut, bas)

        gauche = vision((ligne, c) for c in reversed(range(0, colonne)))
        droite = vision((ligne, c) for c in range(colonne+1, image.taille))
        horizontal = chain(gauche, droite)
        val2=compte(chain(horizontal, vertical))
        #l[0] = max(l[0], val2)
        return val2
    
    
    return max(filter(pixel_blanc, iterateur_pixels), key=vue_pixel)
