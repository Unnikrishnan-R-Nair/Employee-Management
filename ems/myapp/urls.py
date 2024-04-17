from django.urls import path

from myapp import views

urlpatterns = [
    
    # path('employees/all/', views.employees_list_view, name='employees-list'),

    path('', views.EmployeeListView.as_view(), name='employee-list'),

    path('employees/add/', views.EmployeeCreateView.as_view(), name='employee-add'),

    path('employees/<int:pk>/', views.EmployeeDetailView.as_view(), name='employee-detail'),

    path('employees/<int:pk>/remove/', views.EmployeeDeleteView.as_view(), name='employee-delete'),

    path('employees/<int:pk>/change/', views.EmployeeUpdateView.as_view(), name='employee-update'),

]
