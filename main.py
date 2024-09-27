"""
Pas de module importé
"""

#### Imports et définition des variables globales


#### Fonctions secondaires


def artcode_i(s):
    """
    Retourne la liste de tuples encodant une chaîne de caractères passée en argument
    selon un algorithme itératif

    Args: s (str): la chaîne de caractères à encoder

    Returns: list: la liste des tuples (caractère, nombre d'occurences)
    """
    n = 1
    liste_tuple = []
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            n += 1
        else:
            liste_tuple.append((s[i-1],n))
            n = 1
        if i == len(s)-1:
            liste_tuple.append((s[i],n))
    return liste_tuple

def artcode_r(s):
    """
    Retourne la liste de tuples encodant une chaîne de caractères passée en argument 
    selon un algorithme récursif

    Args: s (str): la chaîne de caractères à encoder

    Returns: list: la liste des tuples (caractère, nombre d'occurences)
    """
    liste_carac = []
    # cas de base
    if len(s) == 0:
        return []
    # recherche nombre de caractères identiques au premier
    n = 1
    while n < len(s) and s[n] == s[0]:
        n += 1
    liste_carac.append((s[0], n))
    # appel récursif
    return liste_carac + artcode_r(s[n:])

#### Fonction principale

def main():
    """
    Test les deux fonctions précédentes

    Arg:None

    Return: None
    """
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
