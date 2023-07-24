from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from pytube import * 

def youtube(request):

    ## checking whether request.method is post or not
    if request.method == "POST":
        #getting link from frontend
        link = request.POST['link']
        video = YouTube(link)
        # setting viddeo resolution
        stream = video.streams.get_lowest_resolution()
        # download video
        stream.download()

        return render(request, 'youtube.html')
    return render(request, 'youtube.html')




