from django.urls import path 

from control.views import parteDiario

urlpatterns = [
    path('parte', parteDiario, name='parte_diario'),
]