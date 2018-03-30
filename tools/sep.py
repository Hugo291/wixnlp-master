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

#retourne 2 fichiers (.es et .wix) qui sont les dictionnaires de langues apres avois dissocier dans le .wixes
def split(infile):
    #root contient le infile
    root = infile
    #ouverture du fichier en lecture avec l'extension .wixes
    text = open(infile+".wixes", "r")
    #ouvre le fichier root en ecriture avec l'extension .wix
    es = open(root+".wix", "w")
    #ouvre le fichier root en ecriture avec l'extension .es
    wix = open(root+".es", "w")

    i = 0
    for line in text:
        if "=" in line:
            #dissocie au '='
            #line devient une liste
            line = line.split("=")
            #verifie si l'un des deux est vide
            if line[0] == "" or line[1]=="":
                #signalisation de l'erreur
                print("Error en:", line)
                #si erreur, on sort du document
                sys.exit()

            #met la premiere partie dans un fichier .es(dictionnaire espagnol)
            es.write(line[0] + "\n")
            #creation variable w qui enleve les sauts de lignes
            w = line[1].replace("\n", "")
            # met la deuxieme partie dans un fichier .wix(dictionnaire espagnol)
            wix.write(w + "\n")

            i = i + 1
        else:
            print("Ignored: ", line, end="")

    print("     We got ", str(i), "aligned phrases.")

    #fermeture des fichiers
    text.close()
    wix.close()
    es.close()

# fusionne les fichiers .wix et .es en retournant un ficher .wixes
def merge(infile):
    root = infile
    text = open(infile+".wixes", "w")
    es = open(root+".wix", "r")
    wix = open(root+".es", "r")

    #stock dans esline le contenu du fichier .es ligne par ligne
    esline = es.readline()

    # stock dans wixline le contenu du fichier .wix ligne par ligne
    wixline = wix.readline()

    #fusionne les deux contenu dans une forme de "esline = wixline"
    while (esline and wixline):
        esline = esline.replace("\n", "")
        wixline = wixline.replace("\n", "")
        #ecrit dans le fichier
        text.write(esline+" = "+wixline+"\n")
        #lit la prochaine ligne
        esline = es.readline()
        wixline = wix.readline()

    #fermeture des fichiers
    text.close()
    wix.close()
    es.close()


if __name__ == "__main__":

    # if len(sys.argv) < 2:
#     #     print("sep.py splits or merges an wixes file. An wixes file contains a pair")
#     #     print("of phrases in wixárika and spanish, separeted by an = symbol")
#     #     print("The in file must be *.wixes; or a root that shares .es and .wix")
#     #     print("usage: sep.py infile [-s|-m]")
#     #     print("     -s split the file (default)")
#     #     print("     -m merge two files")
#     #     sys.exit()
#     #
#     # infile = sys.argv[1]
#     #
#     # try:
#     #     op = sys.argv[2]
#     # except:
#     #     op = "-s"
#     #
#     # if "s" in op:
#     #     split(infile)
#     # else:
#     #     merge(infile)


