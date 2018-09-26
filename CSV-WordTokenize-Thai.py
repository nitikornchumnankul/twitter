# -*- coding: utf-8 -*-
from pythainlp.tokenize import word_tokenize,etcc
from pythainlp.summarize import summarize_text
from pythainlp.rank import rank
import numpy as nump
import csv

i = 0 
k = 0
results = ['','']
tokened = ['','']
collect = ['','']
printcsv = ['','']

file = open('tokenizedword.csv','w', encoding="utf8")
write = csv.writer(file, delimiter=',')

with open("twitt.csv", encoding="utf8") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        i = i+1
        results.append(row)
        tokened = results[i]
        for token in tokened:
            collect = word_tokenize(token)
            for col in collect:
                if len(col) < 1:
                    print("Empty")
                elif col != "":
                    write.writerow(['Word',col])
file.close()

        
