from django.urls import path
from . import views

 

urlpatterns=[
 
    path('',views.home,name='home'),
 
    path('chatrooms/',views.home,name='chatrooms'),
    path('room/<str:pk>',views.room,name='room'),
    path('profile/<str:pk>',views.userProfile,name='user-profile'),
    path('create-room/',views.createRoom,name='create-room'),
    path('update-room/<str:pk>',views.updateRoom,name='update-room'),
    path('delete-room/<str:pk>',views.deleteRoom,name='delete-room'),
    path('delete-chatmessage/<str:pk>',views.deleteChatMessage,name='delete-chatmessage'),
 
    path('topics/',views.topicsPage,name='topics'),
    path('activity/',views.activityPage,name='activity'),
]