from django.shortcuts import render, HttpResponse, redirect
from random import randint
from .models import Account
from django.contrib import messages
import io
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import random
import numpy as np
plt.switch_backend('Agg')

def index(request):
    if 'current_user' not in request.session:
        request.session['current_user'] = 0
    if request.session['current_user'] != 0:
        return redirect('/lobby')
    return redirect('/login')


def login(request):
    if request.session['current_user'] != 0:
        return redirect('/lobby')
    return render(request, 'login.html')


def register(request):
    if request.session['current_user'] != 0:
        return redirect('/lobby')
    return render(request, 'register.html')


def login_process(request):
    errors = Account.objects.another_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/login')
    else:
        curr = Account.objects.filter(email=request.POST['email'])
        request.session['current_user'] = curr[0].id
        return redirect('/lobby')


def register_process(request):
    errors = Account.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/register')
    # password = request.POST['r_password']
    # pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    Account.objects.create(first_name=request.POST['r_first_name'], last_name=request.POST['r_last_name'],
                           email=request.POST['r_email'], password=request.POST['r_password'])
    current = Account.objects.filter(email=request.POST['r_email'])
    request.session['current_user'] = current[0].id
    user = request.session['current_user']
    curr = Account.objects.get(id=user)
    curr.game_id = '0'
    curr.save()
    return redirect('/lobby')


def lobby(request):
    if request.session['current_user'] == 0:
        return redirect('/')
    user = request.session['current_user']
    curr = Account.objects.get(id=user)
    curr.waiting_for_game = True
    curr.save()
    if curr.game_id != '0':
        return redirect('/game')
    users = Account.objects.all()
    users2 = users.exclude(id=user)
    none = True
    for i in users2:
        if i.waiting_for_game == True:
            none = False
    context = {
        'users': users2,
        'waiting': users2.all(),
        'noneq': none,
    }
    return render(request, 'lobby.html',context)

def lobby_process(request):
    user = request.session['current_user']
    curr = Account.objects.get(id=user)
    curr.game_id = '0'
    curr.save()
    return redirect('/lobby')

def game(request):
    if request.session['current_user'] == 0:
        return redirect('/')
    user = request.session['current_user']
    curr = Account.objects.get(id=user)
    curr.waiting_for_game = False
    curr.save()
    ran_list = [randint(1, 6), randint(1, 6), randint(
        1, 6), randint(1, 6), randint(1, 6)]
    number_of_1 = 0
    number_of_2 = 0
    number_of_3 = 0
    number_of_4 = 0
    number_of_5 = 0
    number_of_6 = 0
    list2 = []
    total = 0
    pair = 0
    triple = 0
    num = 0

    for i in range(5):
        if ran_list[i] == 1:
            number_of_1 += 1
        if ran_list[i] == 2:
            number_of_2 += 1
        if ran_list[i] == 3:
            number_of_3 += 1
        if ran_list[i] == 4:
            number_of_4 += 1
        if ran_list[i] == 5:
            number_of_5 += 1
        if ran_list[i] == 6:
            number_of_6 += 1
    
    if number_of_1 == 2:
        total += number_of_1*1
        pair += 1
    if number_of_1 == 3:
        triple = 1
        total += number_of_1*1
    if number_of_1 == 4:
        total += number_of_1*1
    if number_of_1 == 5:
        total = 30

    if number_of_2 == 2:
        total += number_of_2*2
        pair += 1
    if number_of_2 == 3:
        triple = 1
        total += number_of_2*2
    if number_of_2 == 4:
        total += number_of_2*2
    if number_of_2 == 5:
        total = 30

    if number_of_3 == 2:
        total += number_of_3*3
        pair += 1
    if number_of_3 == 3:
        triple = 1
        total += number_of_3*3
    if number_of_3 == 4:
        total += number_of_3*3
    if number_of_3 == 5:
        total = 30

    if number_of_4 == 2:
        total += number_of_4*4
        pair += 1
    if number_of_4 == 3:
        triple = 1
        total += number_of_4*4
    if number_of_4 == 4:
        total += number_of_4*4
    if number_of_4 == 5:
        total = 30

    if number_of_5 == 2:
        total += number_of_5*5
        pair += 1
    if number_of_5 == 3:
        triple = 1
        total += number_of_5*5
    if number_of_5 == 4:
        total += number_of_5*5
    if number_of_5 == 5:
        total = 30

    if number_of_6 == 2:
        total += number_of_6*6
        pair += 1
    if number_of_6 == 3:
        triple = 1
        total += number_of_6*6
    if number_of_6 == 4:
        total += number_of_6*6
    if number_of_6 == 5:
        total = 30

    list2.extend([number_of_1, number_of_2, number_of_3,
                  number_of_4, number_of_5, number_of_6])
    if pair == 1 and triple == 1:
        num = 1
        pair = 0
        triple = 0

    context = {
        "num1": f"/static/imgs/dice{ran_list[0]}.png",
        "num2": f"/static/imgs/dice{ran_list[1]}.png",
        "num3": f"/static/imgs/dice{ran_list[2]}.png",
        "num4": f"/static/imgs/dice{ran_list[3]}.png",
        "num5": f"/static/imgs/dice{ran_list[4]}.png",
        "score": list2,
        "total": total,
        "full": num,
        "triple": triple,
        "pair": pair,
    }
    return render(request, 'game.html', context)

def game_process(request, num):
    user = request.session['current_user']
    curr = Account.objects.get(id=user)
    curr2 = Account.objects.get(id=num)
    print(curr.first_name)
    print(curr2.first_name)
    game = randint(0,999999999)
    print(game)
    curr.game_id = game
    curr2.game_id = game
    curr.waiting_for_game = False
    curr2.waiting_for_game = False
    curr.save()
    curr2.save()
    return redirect('/game')

def probability(request):
    if request.session['current_user'] == 0:
        return redirect('/')
    user = request.session['current_user']
    curr = Account.objects.get(id=user)
    curr.waiting_for_game = False
    curr.save()
    if curr.game_id != '0':
        return redirect('/game')
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    return render(request, 'probability.html', {'arr': arr,'user':curr})


def plt2png():
    buf = io.BytesIO()
    
    plt.savefig(buf, format='png', dpi=80)
    s = buf.getvalue()
    buf.close()
    return s


def img_plot(request):
    n = 100
    x = [i for i in range(n)]
    y = [random.randint(1, 100) for a in range(n)]
    request.session['max'] = max(y)
    request.session['ave'] = sum(y)/n
    plt.plot(x,y,color=cm.hsv(30.0))
    png = plt2png()
    plt.cla()
    response = HttpResponse(png, content_type='image/png')
    return response


def log_out(request):
    user = request.session['current_user']
    curr = Account.objects.get(id=user)
    curr.waiting_for_game = False
    curr.save()
    request.session['current_user'] = 0
    return redirect('/login')

def benis(request):
    return render(request,'benis.html')
