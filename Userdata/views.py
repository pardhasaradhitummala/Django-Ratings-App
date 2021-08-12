from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from movies.models import Movie,Rating

# Create your views here.
def user_login(request):
    return render(request,'loginuser.html')

def user_register(request):
    return render(request,'registeruser.html')

def user_registering(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    user = User.objects.create_user(username, email, password)
    user.save()
    return HttpResponse("saved")

def login_user(request):
    user = request.POST['username']
    passw = request.POST['password']
    obj = authenticate(username=user,password=passw)
    # obj = User.objects.get(username=user)
    # if obj.password == passw:
    #     print('match')
    if obj is  not None:
        login(request,obj)
        movies = Movie.objects.all()
        return render(request,'display.html',{'data':movies})
    return render(request,'loginuser.html')

def moviedata(request,id):
    moviedata = Movie.objects.get(id=id)
    movieratings = Rating.objects.filter(movie=moviedata)
    return render(request,'moviedata.html',{'data':moviedata,'rating':movieratings})

def save_rating(request,id):
    r = Rating()
    movie = Movie.objects.get(id=id)
    r.movie = movie
    r.rating = request.POST['rating']
    r.review = request.POST['review']
    r.person = request.user
    r.save()
    movieratings = Rating.objects.filter(movie=movie)

    return render(request, 'moviedata.html', {'data': movie,'rating':movieratings})

    