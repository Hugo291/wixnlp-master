import io
import sys


#re
#re.compile() et sauvegarder l’expression rationnelle renvoyée pour la réutiliser est plus efficace
# quand l’expression est amenée à être utilisée plusieurs fois dans un même programme.

import re
import codecs

#prefixes and affixes of wixarika verbs
from wix.wixaffixes import pre, post

class Verb:
    def __init__(self, verb, debug=0):
        #!!!!!!!!!!!!il met en petit caractere
        self.verb = verb.lower()
        #print(self.verb)

        self.paths = []

        #contient les lignes du fihier stream
        self.roots = []

        self.rootslarge = []
        self.debug=debug

        #Fl = codecs.open("data/steam.large", mode="r", encoding="utf-8")

        #codecs librairie python qui permet la lecture du fichier data/stream
        F = codecs.open("data/steam", mode="r", encoding="utf-8")

        #on lit la prochaine ligne
        line = F.readline()

        #Lecture du fichier
        while 1:
            #supprimssion des saut de ligne
            line=line.replace("\n", "")

            #on ajoute la ligne au roots
            self.roots.append(line)

            #on lit ensuite la ligne suivante
            line=F.readline()

            #si on n'a plus de fichier on arrete tous
            if not line:
                break

        #en fin de boucle si on debug on affiche les lignes (list)
        if self.debug:
            print("**************************")
            print(self.roots)

        #on demarre
        self.start()

    def start(self, prev="", pos=0, path=[]):
        #pre est une liste contenue dans le fichier
        #si la taille de la liste pre -1  est inferieur a la postiion on stop le programme
        if pos > len(pre)-1:
            return

        #si le debug est a 1
        if self.debug:
            print("New branch: ", str(pos), str(prev), str(path))

        #gotone est faux par defaut
        gotone = False

        #on parcour la liste pre a la position rentrer
        for s in pre[pos]:

            #exemple de pre[pos]
            #pre[pos]  = ["'a", 'a', 'ke', 'u', "'u", 'e', "'e"] & pos = 0
            #s = 'a

            #on ajoute \ a +
            #s avec le reg
            s_reg = s.replace("+", "\+")

            #on ajoute \ a + dans le
            #prev avec le reg
            prev_reg=prev.replace("+", "\+")

            #si en debug
            if self.debug:
                print("Searching ^"+prev_reg+s_reg+"+")
            #ajoute une expression reguliere
            #prev avec le reg et s avec le reg
            reg = re.compile("^"+prev_reg+s_reg+"+")

            #retourn le resultat apres expression reg
            m = reg.match(self.verb)


            if m:
                #gotone passe a true si m est true
                gotone= True

                #si en debug
                if self.debug:
                    print("Found:" + str(pos) + m.group())

                nprev = m.group()
                npath = list(path)
                npath.append((""+str(pos)+"", s))

                self.start(nprev, pos+1, npath)
                nprev = nprev.replace("+","\+")


                #boucle sur le contenu du fihier stream
                for root in self.roots:

                    #on ajout un / a tous les + de chaque route
                    root2 = root.replace("+","\+")

                    #creation du preg
                    rootmatch=re.compile("^"+nprev+root2+"+")

                    rm = rootmatch.match(self.verb)
                    if rm:

                        # si en debug
                        if self.debug:
                            print("Found:" + "[root]" + rm.group())
                            print("Found:" + "[root]" + root)

                        nrprev = rm.group()
                        nrpath = list(npath)
                        nrpath.append(("", root))#id of steam TODO

                        # si en debug
                        if self.debug:
                            print(nrprev)

                        if len(self.verb) == len(nrprev):
                            self.paths.append(nrpath)
                        self.end(prev=nrprev,path=nrpath)
                        continue
        if not gotone:
            if pos > 17:
                return
            self.start(prev, pos+1, path)
            return

    def end(self, prev="", pos=1, path=[]):
        if pos <= 0 or pos >= len(post):
            return
        if self.debug:
            print("Actual path", prev)
        if len(prev) == len(self.verb):
            if self.debug:
                print(path)
            return
        gotone=False        
        if self.debug:
            print(str(-pos), str(post[-pos]))
        for s in post[-pos]:
            if self.debug:
                print("Actual suffix:", s, "at pos", str(pos))
            s_reg = s.replace("+", "\+")
            prev_reg= prev.replace("+", "\+")
            if self.debug:
                print("Searching ^"+prev_reg+s_reg+"+")
            reg = re.compile("^"+prev_reg+s_reg+"+")
            m = reg.match(self.verb)
            if m:
                gotone= True
                if self.debug:
                    print("Found:" + str(pos) + m.group())
                nprev = m.group()
                if self.debug:
                    print("Next search:", nprev)
                npath = list(path)
                npath.append(("-"+str(pos)+"", s))
                
                if len(self.verb) == len(nprev):
                    self.paths.append(npath)
                self.end(nprev, pos+1, npath)
        #if not gotone:
        self.end(prev, pos+1, path)

    def __str__(self):
        return 'verbe : '+self.verb


class Word:
    def __init__(self, model_file):
        F = codecs.open("dic", mode="r", encoding="utf-8")
        self.dic = {}
        self.symbols = '!¡"¿?,.'
        self.model = io.read_binary_model_file(model_file)

        line = F.readline()
        while line:
            line = line.split()
            if line:
                self.dic[line[0]] = line
            line = F.readline()
    def checkdic(self,word):
        if word in self.dic.keys():
            try:
                pos = self.dic[word][1]
            except:
                pos =""
            print(word, end=" ")
        else:
            if word in self.symbols:
                print(word, end=" ")
            else: 
                #print(word, "[Nid]", end=" ")
                seg = self.model.viterbi_segment(word)
                for affix in seg[0]:
                    print(affix, end=" ")

if __name__ == "__main__":

    v = Verb("'ena ha p+xuawe", debug=0)
    print('v : '+str(v))

