import json

from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import RequestContext, loader
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
			attributes = {}
			attributes['id'] = users[0].id or None
			attributes['bio'] = users[0].bio or None
			attributes['full_name'] = users[0].full_name or None
			attributes['profile_picture'] = users[0].profile_picture or None
			attributes['username'] = users[0].username or None
			attributes['website'] = users[0].website or None
		except:
			username_error = "The username entered is not valid"

		if request.is_ajax:
			if (access_token_error or username_error):
				if access_token_error:
					error = access_token_error
				elif username_error:
					error = username_error

				return HttpResponse(json.dumps({"error":(error)}), mimetype="application/json")
			else:
				return HttpResponse(json.dumps(attributes), mimetype="application/json")
		else:
			t = loader.get_template('index.html')
			c = RequestContext(request, {'foo': 'bar'})
			return HttpResponse(t.render(c))
	else:
		t = loader.get_template('index.html')
		c = RequestContext(request, {'foo': 'bar'})
		return HttpResponse(t.render(c))
