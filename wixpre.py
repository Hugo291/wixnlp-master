#!/usr/bin/env python3

# Copyright (C) 2016.
# Author: Jesús Manuel Mager Hois
# e-mail: <fongog@gmail.com>
# Project website: http://turing.iimas.unam.mx/wix/

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.



import sys
from normwix import normwix, tokenizewix
from seg import segment, segtext

sin = 0
Fo = 0 

if __name__ == "__main__":

    #Il faut lors du lancement, 3 argument
    # arg1= fichier source
    # arg2= fichier d'entrée(fichier à traduire)
    # arg3= fichier de sortie
    # On peut mettre 4 argument si le 3eme est une anotations (-s)

    #Stop le programme si moins de 2 ou plus de 4 arguments
    if len(sys.argv) < 2 or len(sys.argv) > 4:
        print("Formant:")
        print("     wixpre.py inputfile [-s] [outputfile]")
        sys.exit()

    #Si il y a 4 arguments
    if len(sys.argv) == 4:
        #si le 3eme argument est une anotation
        if sys.argv[2] == "-s":
            sin = 1
            print("Writing to ", sys.argv[3], "without morph anotations")
            #recupere le 4eme argument pour le mettre en fichier de sortie
            outfile = sys.argv[3]
            #ouvre le fichier de sortie
            Fo = open(outfile, "w")

    #si il y a 3 argument.
    elif len(sys.argv) == 3:
        print("Writing to ", sys.argv[2])
        #recupere le chemin du fichier de sortie
        outfile = sys.argv[2]
        #ouvre le fichier de sortie
        Fo = open(outfile, "w")

    #recupere le 2eme argument et le designe en fichier d'entrée
    infile = sys.argv[1]
    #ouvre ce ficher en lecture
    Fi = open(infile, "r")
    text = Fi.read()
    Fi.close()
    #met en forme le texte qu'il contient
    text = normwix(text)
    text = tokenizewix(text)
    text = segtext(text, s=sin)

    #Si il n'y a pas de fichier de sortie, il affiche ce texte.
    if Fo == 0:
        print(text)
    #Ou écrit le texte dans celui-ci.
    else:
        print("Writing to ", sys.argv[2])
        Fo.write(text)
        #referme le fichier de sortie
        Fo.close()

