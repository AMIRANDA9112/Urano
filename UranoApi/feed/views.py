from django.shortcuts import render

# Create your views here.
tweets = [{'name': 'ami', 'text': 'This is my first tweet'},
          {'name': 'randa', 'text': 'This is my second tweet'}]


def home(request):
    context = {'tweets': tweets}
    return render(request, 'feed/home.html', context)
