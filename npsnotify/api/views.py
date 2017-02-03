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
        names = User.objects.filter(groups__name__in=groupl)
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
        jresp = "{type: \"" + resp + "\",name:" + request.user.name + "}"
        return Response(jresp, status=status.HTTP_200_OK)

class fetchold(APIView):
    a = notification.objects.all()[:5]
    b = "{}"
    for i in a:
        b += "{title: " + i.title + ", body: " + i.notif + ", time: " + i.created_date + "},"
    return Response(b, status=status.HTTP_200_OK)
