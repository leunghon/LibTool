from django.shortcuts import render
import pandas as pd
from .models import *
from .filters import *
import uuid
import numpy
# Create your views here.

def home(request):
    return render(request,'home.html')

def search(request):
    records = Record.objects.all().order_by('authorEnglish')
    namesEng = []
    namesKr = []
    for i in records:
        if i.authorEnglish:
            namesEng.append(i.authorEnglish)
        if i.authorKorean:
            namesKr.append(i.authorKorean)
    newNamesEng = [*set(namesEng)]
    newNamesKr = [*set(namesKr)]
    newNamesEng.sort()
    newNamesKr.sort()
    newNamesEng = [i for a,i in enumerate(newNamesEng) if i!=' ']
    newNamesKr = [i for a,i in enumerate(newNamesKr) if i!=' ']
    myFilter = RecordFilter(request.GET, queryset = records)
    records = myFilter.qs
    context = {'records':records,'myFilter':myFilter, 'NamesEng':newNamesEng,'NamesKr':newNamesKr}
    for i in records:
        if len(i.year) < 4:
            print("this is the year ", i.year, "for", i.sourceTitle)
            if i.year == None:
                print("is it nan")
            if not i.year:
                print("is it nan")
            if i.year == "nan":
                print("it is a string nan")
            # print(type(i.sourceTitle))
    return render(request,'search.html',context)

def generateAuthorLinks(names):
    for i in names:
        print(i)
    return 0

def populateDatabase(request):
    df1 = pd.read_csv('/Users/hrithik/Desktop/PC/UofW/work/LibTool/klet/searchtool/data/dataClean.csv')
    GENRE = (('Fictions'),
			('Poems'),
			('Essays'),
			('Plays'),
			('Childrens'),
			('Classic_General'),
			('Classic_Poem'),
			('Classic_History'),
			('Classic_Folk Tale'),
			('Classic_Fiction'),
			('Misc'))
    GenreDict = {'Fiction':0,
			'Poem': 1,
			'Essay': 2,
			'Play':3,
			'Children':4,
			'Classic/General':5,
			'Classic/Poem': 6,
			'Classic/History':7,
			'Classic/Folk Tale':8,
			'Classic/Fiction':9,
            'Misc.':10}
    for dbframe in df1.itertuples():
        obj = Record.objects.create(genre= GENRE[GenreDict[dbframe.GENRE]],authorEnglish = dbframe.authorEnglish, authorKorean = dbframe.authorKorean, 
        workTitle = dbframe.workTitle, translator = dbframe.translator, sourceTitle = dbframe.sourceTitle, 
        publisher = dbframe.publisher, yearCreated = dbframe.yearCreated, authorEnglish2 = dbframe.authorEnglish2, year= populateYear(str(dbframe.yearCreated)), uid2 = str(uuid.uuid4()))
        obj.save()
    context = {'message':"Populating database completed"}
    return render(request, 'message.html', context)

def deleteDatabase(request):
    records = Record.objects.all()
    records.delete()
    context = {'message':"deleting the whole database completed"}
    return render(request, 'message.html', context)

def populateYear(yearint):
    year = str(yearint).replace(".0","")
    return year

def updateYear(request):
    records = Record.objects.all()
    context = {'message':"Changes years greater than 4 digits and adds ."}
    for i in records:
        year = i.year
        if len(year) > 4 and year.find('.') == -1:
            i.year = i.year[:len(i.year)-1]+'.'+i.year[len(i.year)-1:]
            i.save()
    return render(request, 'message.html', context)

def populateuuid(request):
    records = Record.objects.all()
    context = {'message':"Created uuid for all the records in the database"}
    for i in records:
        if len(i.year) > 4:
            i.year = i.year[:len(i.year)-1]+'.'+i.year[len(i.year)-1:]
            # i.save()
    return render(request, 'message.html', context)

def populateAlternateNames(request):
    records = Record.objects.all()
    context = {'message':"Populating alternate names in eglish2 for all the records"}
    authors = {}
    for i in records:
        if i.authorKorean != "" or i.authorKorean != "nan" or not i.authorKorean:
            authors[i.authorKorean] = [i.authorEnglish2]
            for j in records:
                if j.authorKorean != "" or j.authorKorean != "nan" or not j.authorKorean:
                    if i.authorKorean == j.authorKorean and i.authorEnglish != j.authorEnglish:
                        authors[i.authorKorean].append(j.authorEnglish2)
                        authors[i.authorKorean] = list(set(authors[i.authorKorean]))
    for i in records:
        if (i.authorKorean != "nan" and i.authorKorean != "" and i.authorKorean != " "):
            i.authorEnglish2 = i.authorEnglish2 + ",".join(authors[i.authorKorean])
            print(i.authorKorean+" : "+i.authorEnglish2)
            # i.save()
    return render(request, 'message.html', context)