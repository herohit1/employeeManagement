from django.urls import path
from .views import employee_list,create_employee,update_employee,delete_employee,get_employee_by_id


urlpatterns = [
    # employee crud url
    path('employees/', employee_list, name='employee_list'),
    path('employees/create/', create_employee, name='create_employee'),
    path('employees/<int:pk>/update/', update_employee, name='update_employee'),
    path('employees/<int:pk>/delete/', delete_employee, name='delete_employee'),
    path('employees/<int:pk>/', get_employee_by_id, name='get_employee_by_id'),
]