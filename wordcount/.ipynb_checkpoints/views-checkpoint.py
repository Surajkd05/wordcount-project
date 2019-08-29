from django.http import HttpResponse as resp 
from django.shortcuts import render
from collections import Counter

def homepage(request):
    return render(request,"home.html",{"hithere" : "my home"})

def count(request):
    fulltext = request.GET["fulltext"]
    wordlist = fulltext.split()
    countword = dict(Counter(wordlist))
    m = 0
    d = []
    for i,v in countword.items():
        if(v > m):
            m = v
            d.append(i)
        elif(v == m):
            m = v
            d.append(i)
    return render(request,"count.html",{"fulltext":fulltext,"count":len(wordlist),"maximum":d, "words":countword})

def about(request):
    return render(request,"about.html")
    
    