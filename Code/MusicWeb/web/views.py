from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from web.models import Song,Img
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage


# Create your views here.
def index(request):
    return render(request, 'index.html')


def search(request):
    return render(request, "search.html")

def explore(request):
    return render(request, "explore.html")



def help(request):
    if request.method == 'POST':
        image= request.FILES.get('OriImg')
        ori_filename= image.name
        print("Receive : ", ori_filename)
        result_list=(ori_filename).split('.')
        _png_filename=result_list[0]+'.png'
        print("Convent to : ", _png_filename)
        image.name= _png_filename
        p= Img( png_url=  image,  png_filename=_png_filename )
        p.save()
        print(p.png_url.url)
        return render(request, 'help.html',{'Img':p})

    return render(request, 'help.html')


def domain(request,a):
    response =HttpResponse()
    response['Content-Type'] ="text/json"
    if a=="Classical":
        return render_to_response("domain.html", {'Domain':a, 'Songs':Song.objects.filter(Domain="Classical")})
    elif a=="Electronic":
        return render_to_response("domain.html", {'Domain':a,'Songs': Song.objects.filter(Domain="Electronic")})
    elif a=="Folk":
        return render_to_response("domain.html", {'Domain':a,'Songs': Song.objects.filter(Domain="Folk")})
    elif a=="Blues":
        return render_to_response("domain.html", {'Domain':a,'Songs': Song.objects.filter(Domain="Blues")})
    elif a=="Game":
        return render_to_response("domain.html", {'Domain':a,'Songs': Song.objects.filter(Domain="Game")})
    elif a=="Japanese":
        return render_to_response("domain.html", {'Domain':a,'Songs': Song.objects.filter(Domain="Japanese")})
    elif a=="Pop":
        return render_to_response("domain.html", {'Domain':a,'Songs': Song.objects.filter(Domain="Pop")})
    elif a=="Urban":
        return render_to_response("domain.html", {'Domain':a,'Songs': Song.objects.filter(Domain="Urban")})

def play(request,a):
    response =HttpResponse()
    response['Content-Type'] ="text/json"
    return render_to_response("play.html", {'SongContent':Song.objects.get(id=a)})

@csrf_exempt
def dealsearch(request):
    search_text = ""
    if request.method == "POST":
        search_text = request.POST.get("search_text", "")
        print("search text: " + search_text)
        if (search_text != ""):
            try:
                print(Song.objects.filter(
                        Q(AlbumName__icontains=search_text) | Q(SingerName__icontains=search_text)
                        | Q(SongName__icontains=search_text) ))
                return render(request, "search.html", {
                    'Songs': Song.objects.filter(
                        Q(AlbumName__icontains=search_text) | Q(SingerName__icontains=search_text)
                        | Q(SongName__icontains=search_text) )})
            except Exception as e:
                print(e)

        else:
            return render(request, "search.html")