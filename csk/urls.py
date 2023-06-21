from django.urls import path
from csk.views import *
app_name='sushma'
urlpatterns=[
    path('dhoni/',dhoni,name='dhoni')
]