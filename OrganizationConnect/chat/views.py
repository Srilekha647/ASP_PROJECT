from django.shortcuts import render,redirect
from .models import Room,Topic,ChatMessage 
from accounts.models import  Account as User
from .forms import RoomForm 
from django.db.models import Q
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
import re
# Create your views here.
 

def home(request):
    q=request.GET.get('q') if request.GET.get('q') !=None else ''
    rooms=Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
        )
    room_count=rooms.count()
    topics=Topic.objects.all()[0:5]
    room_chatmessages=ChatMessage.objects.filter(Q(room__name__icontains=q))
    context={'rooms':rooms,'topics':topics,'room_count':room_count,'room_chatmessages':room_chatmessages}
    return render(request,'chat/home.html',context)

def room(request,pk):
    room=Room.objects.get(id=pk)
    room_chatmessages = room.chatmessage_set.all()
    participants=room.participants.all()
    if request.method=='POST':
        chatmessage=ChatMessage.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body')
        )
        room.participants.add(request.user)
        return redirect('room',pk=room.id)
    
    context={'room':room,'room_chatmessages':room_chatmessages,'participants':participants}
    return render(request,'chat/room.html',context)

def userProfile(request,pk):
    user=User.objects.get(id=pk)
    rooms=user.room_set.all()
    room_chatmessages=user.chatmessage_set.all()
    topics=Topic.objects.all()
    context={'user':user,'rooms':rooms,'room_chatmessages':room_chatmessages,'topics':topics}
    return render(request,'chat/profile.html',context)

@login_required(login_url='login')
def createRoom(request):
    page='create'
    form=RoomForm()
    topics=Topic.objects.all()
    if request.method=='POST':
        topic_name=request.POST.get('topic')
        topic,created=Topic.objects.get_or_create(name=topic_name)
        Room.objects.create(
            host=request.user,
            topic=topic,
            name=request.POST.get('name'),
            description=request.POST.get('description'),
        )
        return redirect('home')
    context={'form':form,'topics':topics,'page':page}
    return render(request,'chat/room_form.html',context)

@login_required(login_url='login')
def updateRoom(request,pk):
    page='register'
    room=Room.objects.get(id=int(pk))
    form=RoomForm(instance=room)
    topics=Topic.objects.all()
    
    if request.user!=room.host:
        return HttpResponse('You are not allowed here!!')
    
    if request.method=='POST':
        topic_name=request.POST.get('topic')
        topic,created=Topic.objects.get_or_create(name=topic_name)
        form = RoomForm(request.POST, instance=room)
        room.name=request.POST.get('name')
        room.topic=topic
        room.description=request.POST.get('description')
        room.save()
        return redirect(home)
    
    context={'form':form,'topics':topics,'page':page}
    return render(request,'chat/room_form.html',context)

@login_required(login_url='login')
def deleteRoom(request,pk):
    room=Room.objects.get(id=int(pk))
    if request.method=='POST':
        room.delete()
        return redirect('home')
    return render(request,'chat/delete.html',{'obj':room})

@login_required(login_url='login')
def deleteChatMessage(request,pk):
    post_chatmessage=ChatMessage.objects.get(id=int(pk))
    
    if request.user != post_chatmessage.user:
        return HttpResponse('You are not allowed here!!!')
    
    if request.method=='POST':
        post_chatmessage.delete()
        return redirect('home')
    context={'obj': post_chatmessage}
    return render(request,'chat/delete.html',context)

 
    
    
def topicsPage(request):
    q=request.GET.get('q') if request.GET.get('q') !=None else ''
    topics=Topic.objects.filter(name__icontains=q)
    context={'topics':topics}
    return render(request,'chat/topics.html',context)

def activityPage(request):
    activity_chatmessages=ChatMessage.objects.all()
    context={'activity_chatmessages':activity_chatmessages}
    return render(request,'chat/activity.html',context)