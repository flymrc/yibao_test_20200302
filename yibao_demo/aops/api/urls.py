from django.urls import path
from .views import EmployeeUserReadView
from .views import EmployeeUserCreateView

urlpatterns = [
    path('', EmployeeUserReadView.as_view()),
    path('add/', EmployeeUserCreateView.as_view()),
]
