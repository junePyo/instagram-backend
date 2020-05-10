import json
from django.shortcuts import redirect
from django.views import View
from django.http import JsonResponse
from user.models import Account
from features.models import Comment


def getComments(request):
    allComments = Comment.objects.values()
    return JsonResponse({'all comments': list(allComments)}, status=200)


# account_pk=None will make this parameter optional
def postComments(request, account_pk):
    data = json.loads(request.body)
    try:
        Comment.objects.create(
            account=Account.objects.get(pk=account_pk),
            text=data['text']
        )
        return redirect('features-comments')
    except KeyError:
        return JsonResponse({'message': 'INVALID_KEY'}, status=200)
