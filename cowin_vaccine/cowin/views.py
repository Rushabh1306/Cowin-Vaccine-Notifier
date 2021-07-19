from django.http.response import HttpResponse
from django.shortcuts import render
from .utils import forPincode
from .models import StatesList, DistrictList

# Create your views here.
def indexView(request):
    states = StatesList.objects.all()
    districts = DistrictList.objects.all()
    context={}
    context['states'] = states
    context['districts'] = districts
    data = None
    if request.method=='POST':
        print("Post method")
        if request.POST['pin']:
            data = forPincode(int(request.POST['pin']))
        if request.POST['dist']:
            print('District')
    context['data']=data
    print(data)
    return render(request,'index.html',context)