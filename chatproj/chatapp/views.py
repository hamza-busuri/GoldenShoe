from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from chatapp.serializers import UsersSerializer,ChatSerializer
from chatapp.models import Users,Chat
from django.shortcuts import render
import datetime
from django.utils import timezone
from django.db.models import Q
from django.core.mail import send_mail

def index(request):
    return render(request, 'chat_app/index.html')

def chat(request):
    return render(request, 'chat_app/chat.html')

def prodone(request):
    return render(request, 'chat_app/productone.html')

def prodtwo(request):
    return render(request, 'chat_app/producttwo.html')

def prodthree(request):
    return render(request, 'chat_app/productthree.html')

def send(request):
    if request.method=='POST':
        fname = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        send_mail(fname + '(' + phone + ')' + ' has sent you an email', message, email, ['cvnowmail@gmail.com'], fail_silently=False,)

        return render(request, 'chat_app/index.html')

@api_view(['POST'])
def view_users(request):
    if request.method == 'POST':     
        user, created = Users.objects.update_or_create(
            user_id=request.data['sender'],
            defaults={
                'last_visit':datetime.datetime.now(tz=timezone.utc)
            })

        time=datetime.datetime.now(tz=timezone.utc)- datetime.timedelta(seconds=15)
        data={
            'status': 'true',
            'data': UsersSerializer(Users.objects.filter(last_visit__gte=time), many=True).data
        }
        return Response(data, status=status.HTTP_200_OK)
        
    
@api_view(['POST'])
def save_msg(request):
    if request.method == 'POST':
        time=datetime.datetime.now(tz=timezone.utc)
        chat = Chat(
            sender=request.data['sender'],
            receiver=request.data['receiver'],
            msg=request.data['msg'],
            time=time
            )
        chat.save();
        data={
            'status': 'true'
        }
        return Response(data, status=status.HTTP_200_OK)   

@api_view(['POST'])
def get_chat(request):
    if request.method == 'POST':
        time=datetime.datetime.now(tz=timezone.utc)- datetime.timedelta(seconds=150)
        data={
            'status': 'true',
            'data': ChatSerializer(Chat.objects.filter(time__gte=time,receiver=request.data['sender']), many=True).data
        }
        return Response(data, status=status.HTTP_200_OK)

@api_view(['POST'])
def view_msg(request):
    if request.method == 'POST':
        data={
            'status': 'true',
            'data': ChatSerializer(Chat.objects.filter(Q(receiver=request.data['sender'],sender=request.data['receiver']) | Q(receiver=request.data['receiver'],sender=request.data['sender'])), many=True).data
        }
        return Response(data, status=status.HTTP_200_OK)
