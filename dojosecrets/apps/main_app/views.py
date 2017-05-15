from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from .models import Secret
from ..logreg.models import User
from django.db.models import Count
# Create your views here.

def secrets(request):
    # var count = 5
    first_5 = []
    count = 0
    order_byTime = Secret.objects.all().order_by('-created_at')

    if len(order_byTime) >= 5:
        while count < 5 :
            print count
            first_5.append(order_byTime[count])
            count = count + 1

    print first_5

    context = {
        "Secrets": first_5,
        "all_secrets": order_byTime,
        "user": User.objects.filter(id = request.session['user_id'])
    }

    return render(request,'main_app/index.html',context)


def addSecret(request):
    response_from_models = Secret.objects.validateSecret(request.POST,request.session['user_id'])

    if response_from_models['status']:
        print "successfully added secret", response_from_models['secret']
        return redirect('main:secrets')
    else:
        print "failed to add secret"
        return redirect('logreg:index')


def addLike(request,id):
    secret_id = id
    response_from_models = Secret.objects.validateLike(request.session['user_id'], secret_id)

    if response_from_models['status']:
        print "successfully added like"
        return redirect('main:secrets')
    else:
        print "failed to add like"
        return redirect('main:secrets')


def allsecrets(request):

    context = {
        "Secrets":Secret.objects.annotate(num_likes = Count("likes")).order_by("-num_likes")
    }

    return render(request,'main_app/allsecrets.html',context)


def deletesecret(request,id):
    Secret.objects.get(id = id).delete()
    return redirect('main:secrets')
