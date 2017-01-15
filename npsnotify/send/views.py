from django.shortcuts import render
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json

# Create your views here.
class sendmsg(APIView):
	def post(self, request, *args, **kw):
		notif = request.POST.get('notification', None)
		sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
		from_email = Email("chinmaya.mahesh@gmail.com")
		subject = "Testing notify"
		to_email = Email("chinmaya.mahesh@gmail.com")
		content = Content("text/plain", notif)
		mail = Mail(from_email, subject, to_email, content)
		response = sg.client.mail.send.post(request_body=mail.get())
		print(response.status_code)
		print(response.body)
		print(response.headers)
		return Response("{}", status=status.HTTP_200_OK)
		
