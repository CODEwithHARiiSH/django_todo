from . import views
from django.conf.urls.static import static

from django.urls import path
app_name='todo'

urlpatterns = [


     path('', views.home, name='home'),
     path('delete/<int:taskid>/', views.delete, name='delete'),
     path('update/<int:id>/', views.update, name='update'),
     path('cbvhome/', views.todolistview.as_view(), name='cbvhome'),
     path('cbvdetail/<int:pk>', views.todoDetailview.as_view(), name='cbvdetail'),
     path('cbvupdate/<int:pk>', views.todoUpdateview.as_view(), name='cbvupdate'),
     path('cbvdelete/<int:pk>', views.todoDeleteview.as_view(), name='cbvdelete'),
 ]