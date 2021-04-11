from django.shortcuts import render

from .models import Tweet

# Create your views here.



def home(request):
    context = {'tweets': Tweet.objects.all}
    return render(request, 'feed/home.html', context)
