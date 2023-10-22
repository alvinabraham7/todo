from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('list/',views.TaskListview.as_view(),name='list'),
    path('detail/<int:pk>/',views.TaskDetailview.as_view(),name='detail'),
    path('update/<int:pk>/',views.TaskUpdateview.as_view(),name='update'),
    path('delete/',views.TaskDetailview.as_view(),name='delete'),
]