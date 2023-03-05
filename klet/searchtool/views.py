from django.shortcuts import render
import pandas as pd
from .models import *
from .filters import *
# Create your views here.

def home(request):
    return render(request,'home.html')

def search(request):
    records = Record.objects.all()
    myFilter = RecordFilter(request.GET, queryset = records)
    records = myFilter.qs
    context = {'records':records,'myFilter':myFilter}
    return render(request,'search.html',context)

def populateDatabase(request):
    df1 = pd.read_csv('/Users/hrithik/Desktop/PC/UofW/work/LibTool/klet/searchtool/data/dataClean.csv')
    GENRE = (('Fictions', 'Fictions'),
			('Poems', 'Poems'),
			('Essays', 'Essays'),
			('Plays', 'Plays'),
			('Childrens', 'Childrens'),
			('Classic_General', 'Classic_General'),
			('Classic_Poem', 'Classic_Poem'),
			('Classic_History', 'Classic_History'),
			('Classic_Folk Tale', 'Classic_Folk Tale'),
			('Classic_Fiction', 'Classic_Fiction'),
			('Misc','Misc'))
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
        publisher = dbframe.publisher, yearCreated = dbframe.yearCreated, authorEnglish2 = dbframe.authorEnglish2)
        # obj.save()
    context = {'message':"Populating database completed"}
    return render(request, 'populate.html', context)

def deleteDatabase(request):
    records = Record.objects.all()
    # records.delete()
    context = {'message':"deleting database completed"}
    return render(request, 'delete.html', context)
