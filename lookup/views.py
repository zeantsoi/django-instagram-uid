import json

from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render, redirect
from instagram.client import InstagramAPI

import django_instagram_uid.settings as settings

def index(request, access_token_error=None, username_error=None): 
	if request.method == 'POST':
		if request.POST['access_token']:
			access_token = request.POST['access_token']
		else:
			access_token = settings.INSTAGRAM_ACCESS_TOKEN
		
		api = InstagramAPI(access_token=access_token)

		if request.POST['username']:
			try:
				users = api.user_search(request.POST['username'])
			except:
				if request.POST['access_token']:
					access_token_error = "The Access Token entered is invalid"
				else:
					access_token_error = "The Access Token in settings.py is invalid"

		try:
			user = users[0]
			attributes = {
				'id': user.id,
				'bio': user.bio,
				'full_name': user.full_name,
				'profile_picture': user.profile_picture,
				'username': user.username,
				'website': user.website,
			}
			attributes = dict((k,v) for k,v in attributes.items() if v)
		except:
			username_error = "The username entered is not valid"

		if request.is_ajax():
			if (access_token_error or username_error):
				if access_token_error:
					error = access_token_error
				elif username_error:
					error = username_error

				return HttpResponse(json.dumps({"error":(error)}), mimetype="application/json")
			else:
				
				return HttpResponse(json.dumps(attributes), mimetype="application/json")
		else:
			context = {}
			if access_token_error:
				context.update({'error':access_token_error})
			elif username_error:
				context.update({'error':username_error})
			else:
				context = attributes
			return render(request, 'index.html', context)
	else:
		return render(request, 'index.html')