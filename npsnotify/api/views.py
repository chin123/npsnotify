from django.shortcuts import render
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
import sendgrid
import os
from sendgrid.helpers.mail import *
from django.contrib.auth.models import User
from django.contrib.auth.models import Group 
from api.models import notification

# Create your views here.
class sendmsg(APIView):
    def post(self, request, *args, **kw):
        data = json.loads(request.body.decode())
        notif = data["notification"]
        groupl = data["groups"].split(',')
        title = data["title"]
        print("notification:", notif,"groups:", groupl)
        names_classes = set(User.objects.filter(groups__name__in=groupl))
        if data["subgroups"] != "null":
            names_subgroup = set(User.objects.filter(groups__name=data["subgroups"]))
            names = set(names_classes).intersection(names_subgroup)
        else:
            names = names_classes
        emails = set()
        for i in names:
            emails.add(i.email)
        print(emails)
        sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
        for i in emails:
            if i == '':
                continue
            from_email = Email("shishirnhg@gmail.com")
            subject = "Message from notify: " + title
            to_email = Email(i)
            content = Content("text/plain", notif)
            mail = Mail(from_email, subject, to_email, content)
            response = sg.client.mail.send.post(request_body=mail.get())
            print(response.status_code)
            print(response.body)
            print(response.headers)
        n = notification(author=request.user,title=title,body=notif,groups=data["groups"])
        n.save()
        return Response("{}", status=status.HTTP_200_OK)	

class details(APIView):
    def get(self, request, *args, **kw):
        group = ['Teacher', 'Captain']
        resp = ""
        for i in group:
            if request.user.groups.filter(name=i).exists() == 0:
                resp = i
        jresp = {'type': resp, 'name': request.user.username};
        c = json.dumps(jresp)
        d = json.loads(c)
        return Response(d, status=status.HTTP_200_OK)

class fetchold(APIView):
    def get(self,request, *args, **kw):
        a = notification.objects.filter(author=request.user);
        a = a[len(a) - 6:]
        a = a[::-1]
        b = [] 
        for i in a:
            b.append({'title': i.title, 'body':  i.body, 'time': str(i.created_date)})
        c = json.dumps(b);
        d = json.loads(c);
        return Response(d, status=status.HTTP_200_OK)
