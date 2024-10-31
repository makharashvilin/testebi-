from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('test/<int:pk>', views.detail_test, name='detail_test'),
    path('create_test/', views.create_test, name='create_test'),
    path('test/update_test/<int:pk>', views.update_test, name='update_test'),
    path('test/delete_test/<int:pk>', views.delete_test, name='delete_test'),
]
