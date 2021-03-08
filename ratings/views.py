from django.shortcuts import render
from .models import Rating
# my ratings code

def main_view(request):
    obj = Rating.objects.filter(score=0).order_by("?").first()
    context ={
        'object': obj
    }
    return render(request, 'ratings/main.html', context)
    
