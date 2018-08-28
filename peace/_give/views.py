from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .forms import *

class Home(APIView):
    def get(self, request, format=None):
        
        pass

class Item(APIView): #html파일
    def get(self, request, format=None):
        
        ItemPostDatas = ItemPostModel.objects.all()
        
        context = { 'ItemPostDatas' : ItemPostDatas }

        return render(request, "List/ItemList.html", context)

class ItemAdd(APIView): 
    def get(self, request, format=None):
    
        form = ItemPostForm()

        return render(request, "Create/posting.html", {'form': form})

    def post(self, request, format=None):

        user = request.user

        form = PostingDataForm(request.POST)

        if form.is_valid():
            form.save(commit=False)
     
class ItemDetail(APIView):
    def get(self, request, format=None):
        
        pass

class ItemMe(APIView): #html파일
    def get(self, request, format=None):
        
        ItemPickDatas = ItemPickModel.objects.all()

        context = { 'ItemPickDatas' : ItemPickDatas }

        #return render(request, "list.html", context)

    def post(self, request, format=None):

        pass

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

class SignUp(generic.CreateView):

    form_class = UserCreationForm
    success_url = reverse_lazy('login') 
    template_name = 'registration/signup.html'


