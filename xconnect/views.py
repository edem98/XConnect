from django.contrib.auth.models import User
from django.core.mail import BadHeaderError, send_mail
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from member.models import Xmember

from post.models import Party

from post.forms import PartyForm
from .forms import SignUpForm, LoginForm
from django.contrib.auth.hashers import make_password


def home(request):
    parties = Party.objects.all()[:10]
    context = {}
    context['parties'] = parties
    return render(request, 'index.html', context)


def sign_up(request):
    context = {}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        new_user = User.objects.create(username=username, email=email,
                                       password=make_password(password),
                                       )
        member = Xmember(user=new_user)
        member.save()
        if new_user is not None:
            login(request, new_user)
            print('****************************************')
            return redirect('/')
        else:
            print(new_user)
            return render(request, 'signup.html', context)
    else:
        form = SignUpForm()
        context['form'] = form
    return render(request, 'signup.html', context)


def login_view(request):
    context = {}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            my_user = User.objects.get(username=username)
            user = authenticate(username=my_user.username, password=password, )
            if user is not None:
                login(request, user)
                print(user)
                return redirect("/")
        else:
            pass
    else:
        form = SignUpForm()
        context['form'] = form
    return render(request, 'login.html', context)


def logout_view(request):
    logout(request)
    return redirect("/")

def add_party(request):
    context = {}
    if request.method == "POST":
        city = request.POST.get('city')
        title = request.POST.get('title')
        image = 'media/party_place/'+ request.POST.get('image')
        description = request.POST.get('description')
        location = request.POST.get('location')
        member = Xmember.objects.get(user=request.user)
        party = Party(organiser=member,city=city,title=title,image=image,description=description,location=location)
        party.save()
    else:
        form = PartyForm()
        context['form'] = form
    return render(request, 'post.html', context)

def join(request,id):
    if request.user == None:
        redirect("login")
    else:
        member = Xmember.objects.get(user=request.user)
        party = Party.objects.get(id=id)
        party.attenders.add(member)
        context = {}
        context['party'] = party
        return render(request,'unique.html',context)

def my_parties(request):
    member = Xmember.objects.get(user=request.user)
    parties = Party.objects.all()
    context = {}
    returned_parties = []
    for party in parties:
        if member in party.attenders.all():
            returned_parties.append(party)
    print('*******************'+str(returned_parties))
    context['returned_parties'] = returned_parties
    return render(request,'parties.html', context)
