#!/usr/bin/env python

import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("name", help="LaTeX file's name")
parser.add_argument("--section", help="Number of section(s)")
parser.add_argument("--size", help="Police size")

args = parser.parse_args()

fileName = args.name


if args.section is None:
	nbSection = 0
else:
	nbSection = int(args.section)

if args.size is None:
	policeSize = ("12")
else:
	policeSize = str(args.size)


path = ("/home/hibou/LaTeX/")
docClassTxt = ("\\documentclass[" + policeSize + "pt]{article}\n")
packageTxt = ("\\usepackage{amsmath,amsfonts,amsthm,amssymb}\n\\usepackage{fancyhdr}\n\\usepackage{color}\n\\usepackage{graphicx}\n\\usepackage{enumerate}\n\n")
text = ("\\title{Title}\n\\author{Brice Grandvalet}\n\\begin{document}\n\\maketitle\n\n")
sectionTxt = ("\\section{}\n\n")
endTxt = ("\\end{document}")


FileExt = (".tex")

saveFile = open(path + fileName + FileExt,"w")
saveFile.write(docClassTxt)
saveFile.write(packageTxt)
saveFile.write(text)
for i in range(nbSection):
	saveFile.write(sectionTxt)
saveFile.write(endTxt)
saveFile.close()
os.system("gedit " + path + fileName + FileExt)

