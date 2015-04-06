#-*- coding: utf-8 -*-
from nltk.util import ngrams
from nltk.tokenize import RegexpTokenizer
def ngramsoperator(inputfile,n):
  mydict={}
  fh=file(inputfile,"r")
  while True:
    line = fh.readline()
    if line =='':
      break
    else:
      toker = RegexpTokenizer('[\"?,;:\.]|\s+', gaps=True)
      token= toker.tokenize(line)
      grams = ngrams(token, n)
      for word in grams:
        if word in mydict:
            mydict[word]+=1
        else:
            mydict[word]=1

  fh.close()
  return mydict

def Top5(inputdic):
  items = [(v, k) for k, v in inputdic.items()]
  items.sort()
  items.reverse()
  items = [(k, v) for v, k in items]           
  Top5 = items[:5]

  return Top5



tempdict=ngramsoperator("D:\\python data\\Apple.txt",5)
print "The top 5 are ",Top5(tempdict)
#print dictc

