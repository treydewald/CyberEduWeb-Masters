from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

import pyrebase

# store the configuration credentials for firebase
# allows the application to connect to firebase BAAS services
from .models import Video, Article

firebaseConfig = {
    'apiKey': "AIzaSyB6GEKunj1-iZa83pJwTY6_rS-jnCLx3UM",
    'authDomain': "cybersecurity-education.firebaseapp.com",
    'databaseURL': "https://cybersecurity-education-default-rtdb.firebaseio.com",
    'projectId': "cybersecurity-education",
    'storageBucket': "cybersecurity-education.appspot.com",
    'messagingSenderId': "146291628595",
    'appId': "1:146291628595:web:d568bf7322adf935646146",
    'measurementId': "G-3MEJ5SF34V"}

# initialize application to firebase, with above config information
firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()
authe = firebase.auth()
storage = firebase.storage()


# Create your views here.
def sign_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            email = request.user.username
            # sign user in if email and password are correct
            # user = authe.sign_in_with_email_and_password(email, pasw)
            user = form.get_user()
            login(request, user)  # takes two parameters: request and user object
            print(user)
            return redirect('index')
    else:
        form = AuthenticationForm()

    context = {'form': form}
    return render(request, 'cyber/sign_in.html', context)


def sign_up(request):
    if request.method == 'POST':
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        form = UserCreationForm(request.POST or None)
        if form.is_valid():

            # create firebase uID for DB functions
            # email = request.user.username
            # form.username
            # pasw = request.user.password
            # form.password1
            # user_firebase = authe.create_user_with_email_and_password(email, pasw)
            # print(user_firebase)
            # uid = user_firebase['localId']
            # idtoken = request.session['uid']
            # print(uid)

            form.save()
            return redirect('index')  # redirect user to index page after registering
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'cyber/sign_up.html', context)


def forget_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            authe.send_password_reset_email(email)
            message = "An email to reset password was sent"
            context = {'message': message}
            return render(request, 'cyber/forget_password.html', context)
        except:
            message = "something went wrong, make sure email is valid"
            context = {'message': message}
            return render(request, 'cyber/forget_password.html', context)
    return render(request, 'cyber/forget_password.html')


@login_required(login_url='sign_in')
def index(request):
    return render(request, 'cyber/index.html')

def videos(repsonse, cat, pos):
    db_videos = db.child("YouTubeData").get().val()
    ilist = list(db_videos.items())
    video_list = []
    for i in range(0, len(ilist)):
        if ilist[i][1]["cat"] == cat:
            video = Video(cat=ilist[i][1]["cat"], title=ilist[i][1]["title"], url=ilist[i][1]["url"][32:], pos=ilist[i][1]["pos"])
            video_list.append(video)
    for i in video_list:
        if i.pos == pos:
            featured = i
    # print(featured)
    return render(repsonse, "cyber/videos.html", {"video_list": video_list, "featured":featured})

def articles(response, cat):
    db_articles = db.child("Article").get().val()
    ilist = list(db_articles.items())
    article_list = []
    for i in range(0, len(ilist)):
        if ilist[i][1]["cat"] == cat:
            article = Article(cat=ilist[i][1]["cat"], title=ilist[i][1]["title"], url=ilist[i][1]["url"])
            article_list.append(article)
    print(article_list)
    return render(response, "cyber/articles.html", {"article_list": article_list})

def log_out(request):
    logout(request)
    # del request.session['uid']
    # auth.logout(request)
    return redirect('sign_in')

@login_required(login_url='sign_in')
def demo_survey(request):
    return render(request, 'cyber/demo.html')
