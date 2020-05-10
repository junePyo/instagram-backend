import json
from django.shortcuts import redirect
from django.views import View
from django.http import JsonResponse
from django.db import IntegrityError
from django.core import serializers
from user.models import Account
from features.models import Comment

# when the user logs out
# redirects to log in view


def logout(request):
    return redirect('user-login')

# get user profile


def profile(request, account_pk):
    commentsList = []
    account = Account.objects.get(pk=account_pk)
    commentsList.append(list(account.comment_set.values('text')))
    # commentsList = serializers.serialize(
    #    "json", account.comment_set.values('text'))
    # return all comments written by the user
    return JsonResponse({f'all comments written by {account}': commentsList}, status=200)

# returns the home page view of Instagram


def mainView(request):
    return JsonResponse({'message': 'Welcome'}, status=200)


class LoginView(View):
    # display fields that need to be filled to log in
    def get(self, request):
        # if the user has logged in
        email = request.session.get('email', False)
        if (email):
            del(request.session['email'])
            return redirect('user-main')
        # if the user hasn't logged in, display fields
        else:
            fields = ["email", "password"]
            return JsonResponse(fields, safe=False, status=200)

    # log in
    def post(self, request):
        data = json.loads(request.body)
        try:
            user = Account.objects.get(email=data['email'])
            request.session['email'] = user.email
            if user.password == data['password']:
                # redirect back to get view of the login page
                return redirect(request.path)
        except KeyError:
            return JsonResponse({'message': 'INVALID_KEY'}, status=400)


class RegisterView(View):
    # display fields that need to be filled to sign up
    def get(self, request):
        fields = ["username", "phone", "email", "password"]
        return JsonResponse(fields, safe=False, status=200)

    # signing up
    def post(self, request):
        data = json.loads(request.body)
        try:
            Account.objects.create(
                username=data['username'],
                phone=data['phone'],
                email=data['email'],
                password=data['password'],
            )
            # if registered successfully, redirect to login page
            return redirect('user-login')
        except IntegrityError:
            return JsonResponse({'message': 'EXISTING_VALUE'}, status=400)
        except KeyError:
            return JsonResponse({'message': 'INVALID_KEY'}, status=400)
