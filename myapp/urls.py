from django.urls import path
from . import views
from .views import *
from .forms import myform


urlpatterns = [
    path('',views.get,name='home'),
    path('formdata/',data.as_view(),name='myform'),
    path('',ContactListView.as_view(),name='page'),
]
