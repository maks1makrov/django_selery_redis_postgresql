from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from book.tasks import sleep_task


# @cache_page(5)
def hello(request):
    sleep_task.delay(5, request.user.id)
    return HttpResponse("hello world")

def check(request):
    if request.user.is_authenticated:
        return HttpResponse(f"you have {request.user.tables.count()}")
    else:
        return HttpResponse('you must be authenticated')