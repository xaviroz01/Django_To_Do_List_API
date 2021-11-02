from django.shortcuts import render


# Create your views here.
def inedx(request):
    return render(request, 'index.html')