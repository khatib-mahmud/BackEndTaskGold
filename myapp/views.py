
from django.contrib import messages
from django.shortcuts import redirect, render
from myapp.filters import MobileFilter
from myapp.forms import MobileForm
from myapp.models import Mobile

def home(request):
    
    return render(request, 'index.html', {})

def mobile_list(request):
    mobile_list = Mobile.objects.order_by('Brand_Name')
    
    myFilter = MobileFilter(request.GET,queryset=mobile_list)  
    mobile_list = myFilter.qs
      
    return render(request, 'mobile_list.html', {'mobiles':mobile_list, 'myFilter':myFilter})
    

def addmobile(request):
    form = MobileForm()
    if request.method == "POST":
        

        JAN_Code = request.POST.get('JAN_Code')
        
        if Mobile.objects.filter(JAN_Code=JAN_Code).exists():
            messages.warning(request, "Code already exist")
            return redirect('addmobile')
        form = MobileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mobile_list') 
    
    return render(request, 'addmobile.html', {'form':form,})

def mobileinfo(request,id):
    mobile = Mobile.objects.get(pk=id)
    return render(request, 'mobileinfo.html', {'mobile':mobile})
    


def mobiledelete(request,id):
    
    mobile = Mobile.objects.get(pk=id)
    if request.method == "POST":
        mobile.delete()
        # messages.success("Mobile has been deleted")
        return redirect('mobile_list')
    
    return render(request, 'mobiledelete.html', {'mobile':mobile})
    
    
    