from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('search/',views.search, name="search"),
    path('populatedatabase/',views.populateDatabase),
    path('delete/',views.deleteDatabase),
    path('populateYear/',views.updateYear),
    path('populateAlternames/',views.populateAlternateNames),
    path('updateRec/',views.changeAnything),
    path('admin/', views.adminLogin)
]