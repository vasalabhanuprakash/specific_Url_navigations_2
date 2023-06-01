from django.urls import path
from app1.views import * 

app_name='simple'

urlpatterns=[

    path('yash/',yash,name='yash'),
    
]

