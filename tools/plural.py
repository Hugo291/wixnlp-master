import re

def plurales(es):
    newes = re.sub(r'([aeoi])$', r'\1s', es)
    print(es)
    if newes:
        es = newes
    newes = re.sub(r'([lnr])$', r'\1es', es)
    if newes:
        es = newes

    #if newesr2:
    #    es = newesr2
    return es


d = "/home/gog/wixes/dic.txt"

F = open(d)

#regarde chaque ligne du fichier
for line in F:

    #creation de liste
    #séparation du wixarika et de l'espagnol
    (wix, es) = line.split(" = ")
    # [:-1] = all of the elements up to but not including the last element.
    es = es[:-1]

    #si il y a un caractere s
    if "[s]" in wix:
        #séparation au niveau du s
        wixnew = wix.split(" [s]")
        if wixnew[-1] == "":
            wixnew = wixnew[:-1]

        #si la longueur de wixnew est supérieur a 1 caractère
        if len(wixnew) > 1:
            ples = plurales(es)
            
            #affiche ( "nouvelle version du wixarika" = "espagnol")
            print("".join(wixnew[:-1]), "=", es)

            #je sais pas
            if wixnew[-1][0] == " ":
                print("-".join(wixnew[:-1]),"-",wixnew[-1][1:], " = ", ples, sep="")

            #sinon affiche wixnew
            else:
                print(wixnew)
        #sinon affiche ( "premier element de wixnew"  = "espagnol" )
        else:
            print(wixnew[0], "=", es)

    # si il y a un caractere p
    if "[p]" in wix:
        #remplace les p par des ""
        wixnew = wix.replace(" [p]", "")

        #affichage ("wixarika" = "espagnol")
        print(wixnew, "=", es)
