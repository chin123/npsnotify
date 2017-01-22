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
        print("notification:", notif,"groups:", groupl)
        names = User.objects.all()
        emails = set()
        for i in names:
            f = 1
            for j in groupl:
                if i.groups.filter(name=j).exists() == 0:
                    f = 0
                    break
            if f:
                emails.add(i.email)
        print(emails)
        sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
        for i in emails:
            if i == '':
                continue
            from_email = Email("shishirnhg@gmail.com")
            subject = "Testing notify"
            to_email = Email(i)
            content = Content("text/plain", notif)
            mail = Mail(from_email, subject, to_email, content)
            response = sg.client.mail.send.post(request_body=mail.get())
            print(response.status_code)
            print(response.body)
            print(response.headers)
        n = notification(author=request.user,title="test",body=notif,groups=data["groups"])
        n.save()
        return Response("{}", status=status.HTTP_200_OK)	

class details(APIView):
    def get(self, request, *args, **kw):
        group = ['Teacher', 'Captain']
        resp = ""
        for i in group:
            if request.user.groups.filter(name=i).exists() == 0:
                resp = i
        jresp = "{type: \"" + resp + "\"}"
        return Response(jresp, status=status.HTTP_200_OK)

class getgroups(APIView):
    def get(self, request, *args, **kw):
        groups = Group.objects.all()
        gn = []
        for i in group:
            gn.append(i.name)
        return Response(json.dumps(gn), status=status.HTTP_200_OK)
