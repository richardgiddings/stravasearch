from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm, UserCreationForm
from django.contrib.auth import update_session_auth_hash, login, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect

from social_django.models import UserSocialAuth

import requests
from stravalib.client import Client

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from datetime import datetime

@login_required
def home(request):

    from_date = request.GET.get('from_date')
    to_date = request.GET.get('to_date')

    activities = []
      
    if from_date or to_date:
        if from_date:
            from_datetime = datetime.strptime(from_date + " 00:00:00", "%d/%m/%Y %H:%M:%S")
        if to_date:
            to_datetime = datetime.strptime(to_date + " 23:59:59", "%d/%m/%Y %H:%M:%S")

        page = request.GET.get('page')

        # get access token
        social = request.user.social_auth.get(provider='strava')
        token = social.extra_data['access_token']

        # get activity details
        client = Client()
        client.access_token = token

        if from_date and to_date:
            query = client.get_activities(before=to_datetime, after=from_datetime)
        elif from_date: 
            query = client.get_activities(after=from_datetime)
        else: # to_date
            query = client.get_activities(before=to_datetime)

        for activity in query:
            if from_date and not to_date:
                index = 0
            else:
                index = len(activities)

            activities.insert(index,
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

    return render(request, 'core/home.html', 
                            context={
                                'activities': activities,
                                'from_date': from_date,
                                'to_date': to_date,
                            })