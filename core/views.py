from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm, UserCreationForm
from django.contrib.auth import update_session_auth_hash, login, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect

from social_django.models import UserSocialAuth

import requests
from stravalib.client import Client

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@login_required
def home(request):

    page = request.GET.get('page')

    # get access token
    social = request.user.social_auth.get(provider='strava')
    token = social.extra_data['access_token']

    # get activity details
    client = Client()
    client.access_token = token
    activities = []
    for activity in client.get_activities(after="2010-01-01T00:00:00Z"):
        activities.insert(0, 
            { 
                "id": activity.id,
                "name": activity.name,
                "link": "https://www.strava.com/activities/{}".format(activity.id),
                "date": activity.start_date_local,
                "athlete_count": activity.athlete_count,
            }
        )

    paginator = Paginator(activities, 20) # Show n results per page
    try:
        activities = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        activities = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        activities = paginator.page(paginator.num_pages)

    return render(request, 'core/home.html', context={'activities': activities})