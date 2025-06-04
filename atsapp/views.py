from django.shortcuts import render
#


# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, "index.html")


def profile_photo(request):
    photo = get_user_photo(request.user)
    return render(request, 'blocks/header_block.html', {'photo': photo})


def resume_view(request):
    return render(request,"resume_view.html")


def edit_view(request):
    return render(request,"edit_view.html")