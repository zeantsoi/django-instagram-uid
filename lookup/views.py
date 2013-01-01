import json

from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render, redirect
from instagram.client import InstagramAPI

import django_instagram_uid.settings as settings

def index(request, access_token_error=None, username_error=None): 

	# Verify that the request is a POST
	if request.method == 'POST':
		
		# If the access_token argument is empty, use the access token from setting.py; otherwise use the access_token argument
		if request.POST['access_token']:
			access_token = request.POST['access_token']
		else:
			access_token = settings.INSTAGRAM_ACCESS_TOKEN
		
		# Initialize Instagram library with access_token
		api = InstagramAPI(access_token=access_token)

		if request.POST['username']:
			# Find users matching username (should only be one)
			try:
				users = api.user_search(request.POST['username'])

			# Rescue exception if access_token is incorrect
			except:
				if request.POST['access_token']:
					access_token_error = "The Access Token entered is invalid"
				else:
					access_token_error = "The Access Token in settings.py is invalid"

		try:
			# Map attributes of the first and only user in the users list
			user = users[0]
			attributes = {
				'id': user.id,
				'bio': user.bio,
				'full_name': user.full_name,
				'profile_picture': user.profile_picture,
				'username': user.username,
				'website': user.website,
			}

			# If any value in the attributes dict is blank, then remove the key value pair from the dict
			attributes = dict((k,v) for k,v in attributes.items() if v)
		
		# If users array is empty, then no matching users were found
		except:
			username_error = "The username entered is not valid"

		if request.is_ajax():
			
			# If an exception occured, determine which error message should be displayed
			if (access_token_error or username_error):
				if access_token_error:
					error = access_token_error
				elif username_error:
					error = username_error

				# Return error message to template
				return HttpResponse(json.dumps({"error":(error)}), mimetype="application/json")
			
			# If lookup request is successful, return attributes to template
			else:
				return HttpResponse(json.dumps(attributes), mimetype="application/json")
		# If POST request isn't AJAX, manually assign view context
		else:
			context = {}
			
			# If an exception occured, assign an error to the context, otherwise assign the attributes dict to the context
			if access_token_error:
				context.update({'error':access_token_error})
			elif username_error:
				context.update({'error':username_error})
			else:
				context = attributes

			# Return view context to template
			return render(request, 'index.html', context)
	
	# If request isn't POST, then display the template
	else:
		return render(request, 'index.html')