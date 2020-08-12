from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.http import JsonResponse, Http404, HttpResponseRedirect, HttpResponse
from django.db.models import Q, Avg, Sum, F
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import TemplateView, DetailView
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.core import serializers
from django.utils import timezone
from django.contrib.auth.models import User
# icontains query from a list
# https://thepythonguru.com/python-builtin-functions/reduce/
# https://stackoverflow.com/questions/4824759/django-query-using-contains-each-value-in-a-list
from functools import reduce
# https://docs.python.org/3/library/operator.html
# https://www.geeksforgeeks.org/reduce-in-python/
import operator
from itertools import chain
# for filtering exact salary
from decimal import Decimal

# datetime convertion
import pytz
import datetime
import time
from django.conf import settings
from django.db.models import Value
from django.db.models.functions import Concat
import json
import os

from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, Border, Side, PatternFill, Color, Protection, colors, GradientFill
from openpyxl.utils import get_column_letter
import csv
import xlwt 
from cryptography.fernet import Fernet
import base64
import logging
import traceback
import xlrd 
from django.forms import modelformset_factory, inlineformset_factory
from django.forms import modelformset_factory, inlineformset_factory
from datetime import date

# Create your views here.
# ==============================================================
# BUSINESS SIDE START
# ==============================================================

def index(request):
    template_name = "business_side/index.html"

    return render(request, template_name)

def about_us(request):
    template_name = "business_side/about_us.html"

    return render(request, template_name)

def projects(request):
    template_name = "business_side/projects.html"

    return render(request, template_name)

def blogs(request):
    template_name = "business_side/blogs.html"

    return render(request, template_name)

def testimony(request):
    template_name = "business_side/testimony.html"

    return render(request, template_name)

def contact(request):
    template_name = "business_side/contact.html"

    return render(request, template_name)


def services_electrical_system(request):
    template_name = "business_side/services/electrical_system.html"


    return render(request, template_name)
 
def services_solar_power_system(request):
    template_name = "business_side/services/solar_power_system.html"

    
    return render(request, template_name)


def services_airconditioning_system(request):
    template_name = "business_side/services/airconditioning_system.html"

    
    return render(request, template_name)

def services_automatic_fire_supression_system(request):
    template_name = "business_side/services/automatic_fire_supression_system.html"

    
    return render(request, template_name)

def services_fire_detection_and_alarm_system(request):
    template_name = "business_side/services/fire_detection_and_alarm_system.html"

    
    return render(request, template_name)
    
def services_structured_cabling_for_network_and_telephone_system(request):
    template_name = "business_side/services/structured_cabling_for_network_and_telephone_system.html"

    
    return render(request, template_name)

def services_cctv_system(request):
    template_name = "business_side/services/cctv_system.html" 
    return render(request, template_name)

def services_fshhqa(request):
    template_name = "business_side/services/fshhqa.html" 
    return render(request, template_name)



    

# ==============================================================
# BUSINESS SIDE END
# ==============================================================