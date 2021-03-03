from django.shortcuts import render

# Some code here taken from boutique ado project
def index(request):
    """ A view to return the index page """
    
    return render(request, 'home/index.html')