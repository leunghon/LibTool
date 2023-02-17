import django_filters
from django_filters import DateFilter, CharFilter, NumberFilter

from .models import *

class RecordFilter(django_filters.FilterSet):
	authorEnglish = CharFilter(field_name='authorEnglish', lookup_expr='icontains')
	authorKorean  = CharFilter(field_name='authorKorean', lookup_expr='icontains')
	workTitle  = CharFilter(field_name='workTitle', lookup_expr='icontains')
	translator  = CharFilter(field_name='translator', lookup_expr='icontains')
	sourceTitle  = CharFilter(field_name='sourceTitle', lookup_expr='icontains')
	start_date  = NumberFilter(field_name='yearCreated', lookup_expr='gte')
	end_date  = NumberFilter(field_name='yearCreated', lookup_expr='lte')
	
	class Meta:
		model = Record
		fields = '__all__'
