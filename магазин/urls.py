from django.urls import path
from .views import *

urlpatterns = [
	path('', index),
	path('products/', products),
	path('categories/', categories),

]
