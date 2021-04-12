from django.shortcuts import render

from .models import Tweet
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def home(request):
    context = {'tweets': Tweet.objects.all}
    return render(request, 'feed/home.html', context)
