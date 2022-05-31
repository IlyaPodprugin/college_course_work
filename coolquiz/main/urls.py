from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('quiz/<slug:quiz_slug>/', views.display_quiz, name='quiz_page'),
    path('quiz/<slug:quiz_slug>/<slug:username>/result', views.display_result, name='result_of_quiztake'),
]
