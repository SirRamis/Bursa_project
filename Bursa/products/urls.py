
from django.urls import path, re_path
from .views import *


#def re_path(param, archive):
 #   pass


urlpatterns = [
    path('', index), #name='home'),
    path('cats/<int:catid>/', categories),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive),
]
