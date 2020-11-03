from django.urls import path
from firstapp.views import index, question_collection, question_element

urlpatterns = [
    path('', index, name='index'),
    path('questions/', question_collection, name='question_collection'),
    path('questions/<int:question_id>', question_element, name='question_element')
]
