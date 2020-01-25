from django.shortcuts import render

from eventex.subscriptions.forms import SubscriptionForm


def subscribe(request):
    """return HttpResponse("Python Subscribe Test")"""
    """return render(request, 'subscriptions/subscription_form.html')"""
    context = {'form': SubscriptionForm()}
    return render(request, 'subscriptions/subscription_form.html', context)
