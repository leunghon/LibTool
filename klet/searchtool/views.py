from django.shortcuts import render
import pandas as pd
from .models import *
from .filters import *
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
        publisher = dbframe.publisher, yearCreated = dbframe.yearCreated, authorEnglish2 = dbframe.authorEnglish2, year= str(dbframe.yearCreated).replace(".0",""))
        obj.save()
    context = {'message':"Populating database completed"}
    return render(request, 'populate.html', context)

def deleteDatabase(request):
    records = Record.objects.all()
    records.delete()
    context = {'message':"deleting database completed"}
    return render(request, 'delete.html', context)

def populateYear(request):
    records = Record.objects.all()
    context = {'message':"Updating years of all the records"}
    for i in records:
        i.yearCreated = str(i.yearCreated).replace(".0","")
    records.save()
