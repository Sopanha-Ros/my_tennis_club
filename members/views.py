from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from members.form import Input_financedata_info

from .models import Member

from io import BytesIO
import base64
import warnings
warnings.simplefilter("ignore", UserWarning)

def members(request):
    
    # member1 = Member(firstname='Tobias', lastname='Refsnes')
    # member2 = Member(firstname='Linus', lastname='Refsnes')
    # member3 = Member(firstname='Lene', lastname='Refsnes')
    # member4 = Member(firstname='Stale', lastname='Refsnes')
    # member5 = Member(firstname='Jane', lastname='Doe')
    # members_list = [member1, member2, member3, member4, member5]
    # for x in members_list:
    #   x.save()
    
    
    # return HttpResponse("Hello world!")
    # template = loader.get_template('myfirst.html')

    mymembers = Member.objects.all().values()
    name = "panha"
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
        'y' : name
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def testing(request):
  template = loader.get_template('templates.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
  return HttpResponse(template.render(context, request))

#Test Drop down menu
# def dropdown(request):
#   template = loader.get_template('dropdown.html')
#   return HttpResponse(template.render())
