# converting predicate calculus in spreadsheet to be causal chains
# Jan 2017


import csv, re


path = thisPath

myDict={}

calcDict={}

with open(path, 'r', encoding = "ISO-8859-1") as g:
    g.readline()
    reader = csv.reader(g, delimiter=',')
    
    count=1
    for row in reader:
        vn, asc, fd1, fd2, fd3, example, sem_plain, sem_variables, notes = row
        myDict[count]=row
        count+=1
        
for v in myDict.values():
    if v[7] not in calcDict:
        calcDict[v[7]]=[]
        


def searchVariables(string):
    #identifying string between parenthesis
    
    strVar=re.search(r'\((.*?)\)',string).group(1).split(',')
    
    return strVar
    
    
    
    
preamble=r"\documentclass{article} \usepackage{tikz-dependency} \usepackage{mathtools} \usepackage{tikz} \usepackage{caption} \usepackage{amsmath} \usepackage{stackengine} \begin{document}".split()

for k, v in calcDict.items():
    thisList=[]
    variables=[]
    for i in k.split('&'):
        thisList.append(i.strip())
    for j in thisList:
        var=searchVariables(j)
        for v in var:
            if v not in variables:
                variables.append(v)
    print(thisList, variables)
    print()            
    
        
        
    
       
