
from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('employees', views.EmployeeViewSet,basename='employees')
urlpatterns = [path('students/', views.studentsView),
               path('students/<int:pk>/', views.studentDetailView, name='studentDetailView'),
               # path('employees/', views.employees.as_view()),
#                path('employees/<int:pk>/', views.employeeDetailView.as_view(), name='employeeDetailView'),
              path('', include(router.urls)),
              path('blogs/', views.blogsView.as_view()),
              path('comments/', views.commentsView.as_view()),
              path('blogs/<int:pk>/', views.blogsDetailView.as_view()),
              path('comments/<int:pk>/', views.commentsDetailView.as_view())

 ] 