from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Record

class RecordForm(ModelForm):
    class Meta:
        model = Record
        fields = '__all__'

class NewRecordForm(ModelForm):
	GENRE = [ (1,'Fiction'),
			(2,'Poetry'),
			(3,'Essay'),
			(4,'Play'),
			(5,"Children’s Literature"),
			(6,'Classic_General'),
			(7,'Classic_Poetry'),
			(8,'Classic_History'),
			(9,'Classic_Folk Tale'),
			(10,'Classic_Fiction'),
			(11,'Misc')]
	authorKorean = forms.CharField(max_length=100, label="Name of author in Korean")
	authorEnglish = forms.CharField(max_length=100, label="Name of author in English")
	workTitle = forms.CharField(max_length=100, label="Work title in genglish")
	genre= forms.ChoiceField(choices=GENRE, required=True)
	translator = forms.CharField(max_length=100, label="Name of Translator in English")
	sourceTitle = forms.CharField(max_length=100, label="Name of Shource Title in English", required=True)
	publisher = forms.CharField(max_length=100, label="Name of Publisher in English")
	year = forms.CharField(max_length=100, label="Year")
	other = forms.CharField(max_length=300, label="Any other additional information the approver should know")