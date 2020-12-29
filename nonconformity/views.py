from django.http import HttpResponse
from django.shortcuts import render


def nonconformity_tracking(request):
    return HttpResponse("You can see overview of all nonconformity")


def nonconformity_reporting(request):
    return HttpResponse("You can create and edit your nonconformity")


def new_employee(request):
    return HttpResponse("You can create new employees here")


def all_employee(request):
    return HttpResponse("You will be able to see all the employees here")
