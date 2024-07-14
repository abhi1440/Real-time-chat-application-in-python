from django.shortcuts import render, redirect
from .models import Room, Message

# Create your views here.
def home(request):
    return render(request,'home.html')

def room(request,room):
    return render(request,'room.html')



def checkview(request):
    room_name = request.POST.get('room_name')  # Use lowercase 'post', and use parentheses () instead of square brackets [] for get method
    username = request.POST.get('username')  # Use lowercase 'post', and use parentheses () instead of square brackets [] for get method
   
    if Room.objects.filter(name=room_name).exists():  # Use lowercase 'exists' instead of 'exist'
        return redirect('/' + room_name + '/?username=' + username)
    else:
        new_room = Room.objects.create(name=room_name)
        new_room.save()
        return redirect('/' + room_name + '/?username=' + username)


