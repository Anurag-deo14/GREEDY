from http.client import HTTPResponse
import re
from django.shortcuts import render
from flask import request
import db
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from django.contrib import messages

def home(request):
    return render(request, "index.html")


def edit(request):
    x = db.rows("users")
    print(x)
    db.addUser("piyush", "xyz", "abcd")
    return render(request, "index.html")

def signup(request):
    d = request.POST
    print(d)
<<<<<<< HEAD
    fname = d['fname']
=======
>>>>>>> 55cf727ed66b77200909d121b1bb530cf65d677d
    usnm = d['usnm']
    mail = d['email']
    passd = d['password']
    repass = d['re-passd']

    if (passd != repass):
        # unmatched password
        messages.info(request, 2)
        return render(request, "index.html")

    check1 = db.check_username(usnm)
    check2 = db.check_mail(mail)

    if check1:
        # username exists
        messages.info(request, 1)
        return render(request, "index.html")
    
    if check2:
        # email exists
        messages.info(request, 3)
        return render(request, "index.html")

<<<<<<< HEAD
    db.addUser(usnm, fname, mail, passd)
=======
    db.addUser(usnm, mail, passd)
>>>>>>> 55cf727ed66b77200909d121b1bb530cf65d677d
        
    return render(request, "index.html")

def login(request):
    data = request.POST
    usnm = data['usnm']
    passd = data['passd']

    check = db.check_username(usnm)

    if check:
        if check == passd:
            # logged in
            messages.info(request, 4)
            return render(request, "index.html")
        else:
            # wrong password
            messages.info(request, 5)
            return render(request, "index.html")
    else:
        # no account
        messages.info(request, 6)
        return render(request, "index.html")

    return render(request, "index.html")