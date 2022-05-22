from datetime import datetime
from re import TEMPLATE
from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .forms import PostForm


# Create your views here.
def index(request):
    today = datetime.datetime.now().date()
    form = PostForm()
    data = {'today': today, 'form': form}
    
    return render(request,'index.html', data)