from django.urls import path
from . import views
urlpatterns = [
    path('',views.loadindex,name='loadindex'),
    path('singlepost',views.loadsinglepost,name='singlepost'),
]