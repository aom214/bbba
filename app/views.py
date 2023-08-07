from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,get_user_model,logout,login
from django.contrib import messages
import warnings
from django.contrib.sessions.models import Session
from django.db.models import Sum,F
from app.models import upcoming,teams,addplayers,points,regteam,previous,matchCart,profile

# Create your views here.
def index(request):
    UPCOMING=upcoming.objects.all()
    previou=previous.objects.all()
    params={"UPCOMING":UPCOMING,"PREVIOUS":previou}
    return render(request,'inde.html',params)

def search(request):
    query=request.GET['sea']
    allmatches=upcoming.objects.filter(match_unique_name__icontains=query)
    allprev=previous.objects.filter(team1__icontains=query)
    params={'match':allmatches,'allprev':allprev}
    return render(request,'search.html',params)

def sign(request):
    if request.method=='POST':
        username=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirmpassword=request.POST.get('confirm-password')
        if get_user_model().objects.filter(username=username).exists():
            messages.warning(request, 'User with this username already exists.')
            return redirect('/sign')
        elif get_user_model().objects.filter(email=email).exists():
            messages.warning(request, 'Email already exists.')
            return redirect('/sign')
        else:
            if password!=confirmpassword:
                messages.warning(request, 'password does not match')
                return redirect('/sign')
            else:
                my_user=User.objects.create_user(username,email,password)
                my_user.save()
                return redirect('/login')
    return render(request,'sign.html')

def loginn(request):
    if request.method=="POST":
        username=request.POST.get('userr')
        password=request.POST.get('pass')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.warning(request, 'Email or Password does not match')
            return redirect('/login')
    return render(request,'login.html')

def logoutt(request):
    logout(request)
    return redirect('/')

def myteams(request):
    TEAMS=teams.objects.all()
    p={"team":TEAMS}
    return render(request,'teams.html',p)
def base(request):
    UPCOMING=upcoming.objects.all()
    params={"UPCOMING":UPCOMING}
    return render(request,'base.html',params)


def players(request, team_namee):
    team=teams.objects.filter(team_name=team_namee)
    players=addplayers.objects.filter(team=team_namee)
    pla={'players':players,'team':team}
    return render(request,'players.html',pla)


def regplayers(request,team_namee):
    teamee=teams.objects.filter(team_name=team_namee)
    players=addplayers.objects.all()
    params={'players':players,'team':teamee}
    return render(request,'addplayers.html',params)
def addplayerform(request,team_nam):
    if request.method=="POST":
        playername=request.POST.get('player-name')
        playertype=request.POST.get('player-type')
        playerimage=request.FILES.get('player-image')
        player=addplayers(player_name=playername,players_type=playertype,team=team_nam,player_image=playerimage)
        player.save()
        players=addplayers.objects.filter(team=team_nam)
        te=teams.objects.filter(team_name=team_nam)
        params={'players':players,'team':te}
        return redirect('addplayers',team_namee=team_nam)
    
    return render(request,'addplayerform.html')
def poi(request):
    point=points.objects.all()
    sorted_teams = sorted(point, key=lambda x: (x.poin(), x.plusminus), reverse=True)
    p={'sorted':sorted_teams}
    return render(request,'points.html',p)

def registerteam(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            teamname=request.POST.get('team-name')
            teamowner=request.POST.get('team-owner')
            teamcoach=request.POST.get('team-coach')
            teamcaptain=request.POST.get('team-captain')
            teamhome=request.POST.get('team-home')
            teamlogo=request.FILES.get('team-logo')
            team, created = teams.objects.get_or_create(user=request.user)
            team.team_coach=teamcoach
            team.team_owner=teamowner
            team.team_captain=teamcaptain
            team.team_name=teamname
            team.teams_image=teamlogo
            team.team_home=teamhome
            team.save()
            t=teams.objects.filter(user=request.user)
            params={'team':t}
            return render(request,'register.html',params)
        if teams.objects.filter(user=request.user):
            messages.warning(request, 'you already made your team to edit detail fill this else to edit players scroll down and click on add/edit players')
            t=teams.objects.filter(user=request.user)
            params={'team':t}
            return render(request,'register.html',params)
        else:
            return render(request,'register.html')
    else:
        messages.warning(request, 'YOU CAN REGISTER TEAM ONLY AFTER LOGIN')
        return redirect('/sign')

def bookticket(request,match_id):
    match=upcoming.objects.filter(id=match_id)
    product = get_object_or_404(upcoming, pk=match_id)
    if request.method=="POST":
        product_quantity=1
        cart_item, created = matchCart.objects.get_or_create(user=request.user, match_unique_name=product)
        cart_item.quantity=product_quantity
        cart_item.save()
        request.session.save()
    cart_items=matchCart.objects.filter(user=request.user,id=match_id).exists()
    params={'match':match,'cartitemss':cart_items}
    return render(request,'bookticket.html',params)

def ticketcounter(request):
    cart_it = matchCart.objects.filter(user=request.user)
    product=upcoming.objects.all()
    total_price=0
    total_tax=total_price*15/100
    priceafttax=total_price+total_tax
    if request.method=="POST":
        if int(request.POST.get('quantity',1))==None:
            product_quantity=1
        else:
            product_quantity=int(request.POST.get('quantity',1))

        match=request.POST.get('productid')
        cart_items, created = matchCart.objects.get_or_create(user=request.user, id=match)
        cart_items.quantity=int(product_quantity)
        cart_items.save()
        cart_it = matchCart.objects.filter(user=request.user)
        if cart_items:
            cart_items = matchCart.objects.filter(user=request.user)
            total_price = sum(item.priceofmatch() for item in cart_it)
        else:
            total_price=0
        total_tax=total_price*15/100
        priceafttax=total_price+total_tax
    param={'cart':cart_it,'match':product,'total_price':total_price,'total_tax':total_tax,'price_includes_tax':priceafttax}
    return render(request,'ticketcounter.html',param)

def removeproduct(request,product_id):
    cart_ite, created = matchCart.objects.get_or_create(user=request.user, match_unique_name=product_id)
    cart_ite.delete()
    return redirect('/ticketcounter')
def previousmat(request):
    previ=previous.objects.all()
    params={'PREVIOUS':previ}
    return render(request,'previousmatches.html',params)
def previousdesc(request,previous_id):
    match=previous.objects.filter(id=previous_id)
    params={'match':match}
    return render(request,'previousdesc.html',params)

def deleteplayer(request,team_name,player_id):
    player, created = addplayers.objects.get_or_create(id=player_id)
    player.delete()
    team=team_name
    return redirect('addplayers', team_namee=team)
def profil(request):
    if profile.objects.filter(user=request.user):
        messages.warning(request, 'YOU already save your profile to edit put all inputs second time')

    if request.method=="POST":
        userfname=request.POST.get('first-name')
        userlname=request.POST.get('last-name')
        userage=request.POST.get('age')
        useroccupation=request.POST.get('occupation')
        userphoto=request.FILES.get('image')
        prof, created = profile.objects.get_or_create(user=request.user)
        prof.first_name=userfname
        prof.last_name=userlname
        prof.user_age=userage
        prof.user_image=userphoto
        prof.user_occupation=useroccupation
        prof.save()
    return render(request,'profile.html')