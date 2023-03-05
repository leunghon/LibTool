from django.urls import path
from . import views

urlpatterns = [
    path('/',views.home),
    path('search/',views.search),
    path('populatedatabase/',views.populateDatabase),
    path('delete/',views.deleteDatabase)
]