import django_filters
from django_filters import DateFilter, CharFilter, NumberFilter
from django import forms
from .models import *

class RecordFilter(django_filters.FilterSet):
	authorEnglish2 = CharFilter(label='Author Name (Eng)',field_name='authorEnglish2', lookup_expr='icontains',widget=forms.TextInput(attrs={"max_length":"100","style":"width:175px;margin-left:25px;margin-right:25px;margin-top:10px"}))
	authorKorean  = CharFilter(label='Author Name (Korean)',field_name='authorKorean', lookup_expr='icontains',widget=forms.TextInput(attrs={"max_length":"100","style":"width:175px;margin-left:25px;margin-right:25px;margin-top:10px"}))
	workTitle  = CharFilter(label='Work Title',field_name='workTitle', lookup_expr='icontains',widget=forms.TextInput(attrs={"max_length":"100","style":"width:175px;margin-left:25px;margin-right:55px;margin-top:10px"}))
	translator  = CharFilter(label='Translator',field_name='translator', lookup_expr='icontains',widget=forms.TextInput(attrs={"max_length":"100","style":"width:175px;margin-left:25px;margin-right:55px;margin-top:10px"}))
	publisher = CharFilter(label='Publisher',field_name='publisher', lookup_expr='icontains',widget=forms.TextInput(attrs={"max_length":"100","style":"width:175px;margin-left:45px;margin-right:25px;margin-top:10px"}))
	sourceTitle  = CharFilter(label='Source Title',field_name='sourceTitle', lookup_expr='icontains',widget=forms.TextInput(attrs={"max_length":"100","style":"width:175px;margin-left:25px;margin-right:55px;margin-top:10px"}))
	start_date  = NumberFilter(label='Published Year >=',field_name='yearCreated', lookup_expr='gte',widget=forms.TextInput(attrs={"max_length":"100","style":"width:175px;margin-left:25px;margin-right:55px;margin-top:10px"}))
	end_date  = NumberFilter(label='Published Year <=',field_name='yearCreated', lookup_expr='lte',widget=forms.TextInput(attrs={"max_length":"100","style":"width:175px;margin-left:25px;margin-right:25px;margin-top:10px"}))
	# Year  = NumberFilter(field_name='yearCreated', lookup_expr='iexact',widget=forms.TextInput(attrs={"max_length":"100","style":"width:450px;margin-left:25px;margin-right:25px;margin-top:10px"}))
	class Meta:
		model = Record
		fields = ['authorEnglish2','authorKorean','workTitle', 'translator', 'sourceTitle', 'start_date', 'end_date', 'genre']
