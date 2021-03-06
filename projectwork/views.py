# Views.py controls what is being seen in the browser
from django.http import HttpResponse 
from django.shortcuts import render
from .forms import urlForm, ContactForm
import requests
import urllib
import json

def home_page(request):
    contact = ContactForm()
    context = {
        "feedback":"Feedback",
        "contact":contact
    }
    
    return render(request, "index.html", context)

# The sql function below contain all about the sql injection page
def sql(request):
         
    form = urlForm(request.POST or None)
    contact = ContactForm()
    context ={
        "form": form,
        "feedback":"Feedback",
        "contact":contact,
    }

    if request.method == 'POST':
        search_id = request.POST.get('url', None)

        if form.is_valid():

            response = requests.get(search_id+"%27").text #This line tests the url for sql injection vulnurability
            printout = ' is vulnerable to SQL injection'

            url = search_id
            url.split("/")[2:]
            array = url.split("/")[0:3]
            str1 = '/'.join(array)
            
            if 'You have an error in your SQL syntax;' in response:
                
                if 'MsSQL' in response:
                    form = urlForm(request.POST or None)
                    resp= 'Found database type: MSSQL'
                    context ={
                        "form": form,
                        "resp": resp,
                        "MsSQL": True,
                        "result": printout,
                        "link": str1,
                        "feedback":"Feedback",
                        "contact":contact,
                    }
                    return render (request, "sql.html", context)

                elif 'MySQL' in response:
                    resp ='Found database type: MYSQL'
                    context ={
                        "form": form,
                        "resp": resp,
                        "MySQL": True,
                        "result": printout,
                        "link": str1,
                        "feedback":"Feedback",
                        "contact":contact,
                    }
                    return render (request, "sql.html", context)

                elif 'MariaDB' in response:
                    resp ='Found database type: MariaDB'
                    context ={
                        "form": form,
                        "resp": resp,
                        "MariaDB": True,
                        "result": printout,
                        "link": str1,
                        "feedback":"Feedback",
                        "contact":contact,
                    }
                    return render (request, "sql.html", context)

                else:
                    resp ='can not find the type of database used'
                    context ={
                        "form": form,
                        "resp": resp,
                        "notvulnerable": True,
                        "link": str1,
                        "feedback":"Feedback",
                        "contact":contact
                    }
    
                    return render(request, "sql.html", context)
                    
            else:
                printout =" is NOT vulnerable to SQL injection"
                
                context = {
                        "form": form,
                        'notvulnerable': True,
                        "feedback":"Feedback",
                        "contact":contact,
                        "link": str1,
                        "result": printout
                        }
                return render(request, "sql.html", context)
    return render(request, "sql.html", context)
# this method check for the form parameter
def formparameter(request):  
    form = urlForm(request.POST or None)
    contact = ContactForm()
    context = {
        "feedback":"Feedback",
        "contact":contact,
        "form": form,
    }
   
    if request.method == 'POST':
        search_id = request.POST.get('url', None)
        url = search_id

        if form.is_valid():
            from requests.auth import HTTPBasicAuth
            url = search_id
            req1 = requests.get(url)
            req = requests.get(url,auth=HTTPBasicAuth('1\'or\'1\'=\'1', '1\'or\'1\'=\'1')) # sql query is been sent to the login form
            

            
            if req1.text != req.text:
                url.split("/")[2:]
                array = url.split("/")[0:3]
                str1 = '/'.join(array)

                getresult = ' is NOT vulnerable'
                context ={
                    "form": form,
                    "notvulnerable": True,
                    "getresult": getresult,
                    "feedback":"Feedback",
                    "link": str1,
                    "contact":contact
                } 
                print('Not vulnerable')
                return render(request, "formparameter.html", context)
                

            elif "invalid" in req.text :
                url.split("/")[2:]
                array = url.split("/")[0:3]
                str1 = '/'.join(array)

                getresult = ' is not vulnerable'
                context ={
                    "form": form,
                    "notvulnerable": True,
                    "getresult": getresult,
                    "link": str1,
                    "feedback":"Feedback",
                    "contact":contact
                } 
                return render(request, "formparameter.html", context)
                

            elif "incorrect" in req.text :
                url.split("/")[2:]
                array = url.split("/")[0:3]
                str1 = '/'.join(array)

                getresult = ' is not vulnerable'
                context ={
                    "form": form,
                    "notvulnerable": True,
                    "getresult": getresult,
                    "link": str1,
                    "feedback":"Feedback",
                    "contact":contact
                } 
                return render(request, "formparameter.html", context)
                

            elif "Wrong" in req.text :
                url.split("/")[2:]
                array = url.split("/")[0:3]
                str1 = '/'.join(array)

                getresult = ' is not vulnerable'
                context ={
                    "form": form,
                    "notvulnerable": True,
                    "getresult": getresult,
                    "link": str1,
                    "feedback":"Feedback",
                    "contact":contact
                } 
                return render(request, "formparameter.html", context)
               

            elif "error login" in req.text :
                url.split("/")[2:]
                array = url.split("/")[0:3]
                str1 = '/'.join(array)

                getresult = ' is not vulnerable'
                context ={
                    "form": form,
                    "notvulnerable": True,
                    "getresult": getresult,
                    "link": str1,
                    "feedback":"Feedback",
                    "contact":contact
                } 
                return render(request, "formparameter.html", context)
                
            else:
                url.split("/")[2:]
                array = url.split("/")[0:3]
                str1 = '/'.join(array)

                getresult = ' is vulnerable'
                context ={
                    "form": form,
                    "vulnerable": True,
                    "getresult": getresult,
                    "link": str1,
                    "feedback":"Feedback",
                    "contact":contact
                } 
                return render(request, "formparameter.html", context)
                

	

    
    return render(request, "formparameter.html", context)

# the method for printing http header
def header(request):
    form = urlForm(request.POST or None)
    contact = ContactForm()
    context ={
        "form": form,
        "feedback":"Feedback",
        "contact":contact
    }
    if request.method == 'POST':
        search_id = request.POST.get('url', None)
    
    if form.is_valid():
        # the request module is been use to get the header flag
        head = requests.get(search_id).headers

        context = {
                "form": form,
                "head": head,
                'httpheader': True,   
                "feedback":"Feedback",
                "contact":contact                     
                }
        return render (request, "header.html", context)

    return render (request, "header.html", context)
# the method for xss
def xss(request):
    form = urlForm(request.POST or None)
    contact = ContactForm()

    context ={
        "form": form,
        "feedback":"Feedback",
        "contact":contact
    }
 

    if request.method == 'POST':
        search_id = request.POST.get('url', None)
        url = search_id
        url.split("/")[2:]
        array = url.split("/")[0:3]
        str1 = '/'.join(array)
# javascript code is been supply
        if form.is_valid():
            payloads = ['<script>alert(1);</script>', '<BODY ONLOAD=alert(1)>']
            for payload in payloads:
                req = requests.post(url+payload)
                if payload in req.text:
                    resp = " is vulnerable\r\n"
                    context ={
                    "form": form,
                    "getresult": resp,
                    "vulnerable": True,
                    "link": str1,
                    "feedback":"Feedback",
                    "contact":contact
                    }
                    print ("Parameter vulnerable\r\n")
                    print ("Attack string: "+payload)
                 
                    
                    return render(request, "xss.html", context)
                else:
                    resp = " is not vulnerable\r\n"
                    context ={
                    "form": form,
                    "getresult": resp,
                    "notvulnerable": True,
                    "link": str1,
                    "feedback":"Feedback",
                    "contact":contact
                    }
                    print ("Parameter not vulnerable\r\n")
                    
                    return render(request, "xss.html", context)
    return render(request, "xss.html", context)