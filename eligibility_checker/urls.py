from django.urls import path
from.import views

urlpatterns=[
    path('',views.home),
    #path('eli',views.check_eligibility),
    path('calc',views.calculate)

]