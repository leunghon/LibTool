from django.shortcuts import render
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