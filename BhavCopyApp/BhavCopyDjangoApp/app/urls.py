from django.urls import path,include
from .api import queryData
from .views import frontPage

urlpatterns = [

    path('',frontPage,name="frontPage"),
   path('api/search/',queryData,name='queryData'),

]
