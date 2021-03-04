from django.shortcuts import render

# code taken from botuique abo project
def profile(request):
    """ Display the user's profile. """

    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)
    