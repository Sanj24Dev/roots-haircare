from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View
from store.models.product import Products
from store.models.category import Category
def quiz (request):
    if request.method != 'POST':
        return render (request, 'quiz.html')

    postData = request.POST
    type = postData.get('type')
    density = postData.get('density')
    condition = postData.get('condition')
    hairfall = postData.get('hairfall')
    dandruff = postData.get('dandruff')
    gray = postData.get('gray')
    treatment = postData.get('treatment')


    request.session['type'] = type
    request.session['density'] = density
    request.session['condition'] = condition
    request.session['hairfall'] = hairfall
    request.session['dandruff'] = dandruff

    if treatment == "yes":
        request.session['discoloration']='discoloration'
    elif gray == "no":
        request.session['discoloration']='no'
    else:
        request.session['discoloration'] = 'graying'

    print(gray,treatment,request.session['discoloration'])
    return redirect ('result')
        

