#-*- coding: utf-8 -*-

import time
import os
import sys

from PIL import Image

def GenerationXML(filename, repertoire, Hauteur, Largeur, tag):
    nomfichierxml = filename[:-4] + ".xml"

    #On ouvre le fichier en lecture
    fichierxml = open(repertoire + nomfichierxml,"w+")

    fichierxml.write("<annotation verified=\"yes\"><folder>"+ repertoire +"</folder>")
    fichierxml.write("<filename>" + nomfichierxml + "</filename>")
    fichierxml.write("<path>" + repertoire + filename + "</path>")
    fichierxml.write("<source><database>Unknown</database></source>")
    fichierxml.write("<size><width>" + str(Largeur) + "</width><height>" + str(Hauteur) + "</height><depth>3</depth></size>")
    fichierxml.write("<segmented>0</segmented><object><name>" + tag + "</name><pose>Unspecified</pose><truncated>0</truncated><difficult>0</difficult>")
    fichierxml.write("<bndbox><xmin>0</xmin><ymin>0</ymin><xmax>" + str(Largeur) + "</xmax><ymax>" + str(Hauteur) + "</ymax></bndbox>")
    fichierxml.write("	</object></annotation>")

    fichierxml.close()
  
def main(repertoire,tag): 
    for filename in os.listdir(repertoire):
        ImageOuverte = Image.open(repertoire + filename)
        Hauteur = ImageOuverte.height
        Largeur = ImageOuverte.width

        GenerationXML(filename, repertoire, Hauteur, Largeur, tag)

        print(filename +  ': Opération Réussie !')


if __name__ == '__main__':
    if len(sys.argv) <= 2:
        print('USAGE: repertoire, tag')
    else:
        t1 = time.time()
        main(sys.argv[1],sys.argv[2])
        print('Temps de Traitement : %d s'%((time.time()-t1)))
