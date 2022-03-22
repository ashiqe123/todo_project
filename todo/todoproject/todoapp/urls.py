from django.urls import path

from todoapp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('detail',views.detail,name='detail'),
    path('delete/<int:task_id>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('cbvhome/',views.classview.as_view(),name='cbvhome'),
    path('cbvdet/<int:pk>/',views.detailview.as_view(),name='cbvdet'),
    path('cbvedit/<int:pk>/',views.updateview.as_view(),name='cbvedit'),
    path('cbvdel/<int:pk>/',views.deleteview.as_view(),name='cbvdel')]