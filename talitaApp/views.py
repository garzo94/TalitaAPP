from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #I did not create any form so I use this for login
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import UserRegistrationForm
from .models import Profile, Image
#### reset passwords ###

from django.contrib.auth.models import User

#### pdf ###
from django.http import FileResponse 
import io
from reportlab.pdfgen import canvas 
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Paragraph, SimpleDocTemplate, Frame
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
##html2pdf######
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa









# Create your views here.


@login_required(login_url='/account/login')
def dashboard(request):

    #getting categories from user
    categories = Image.objects.filter(user_id=request.user.id).values('category').distinct()
    
 
    category =  request.GET.get('category')# eesto lo recibo desde la url del template ?cagegory={{category}}
    
    
    if request.GET.get('search'): 
        search = request.GET.get('search')
        
        images = Image.objects.filter(nameimage__icontains=search,user=request.user.id)
        print('##', images)
        

    else:
        
        images = Image.objects.filter(user_id=request.user.id,category=category)
  
    
           

    return render(request,'account/dashboard.html', {'categories': categories,'images':images, 'category':category})

def login_request(request):

   
    
    
    if request.method == 'POST':
        form =  AuthenticationForm(request, data = request.POST)
        print('que pedo')
        if form.is_valid():
            password =  form.cleaned_data.get('password')
            username = form.cleaned_data.get('username')
            user = authenticate(username=username, password=password)
            print(user)
            if user is not None:
                print('que pedo')
                login(request, user)
                
                return redirect("talitaApp:dashboard")
            else:
                messages.error(request, "Password y username son inválidos")
        else:
            messages.error(request, "Password y username son inválidos")
    form =AuthenticationForm()
    return render(request, "account/login.html", context={'form': form})

def logout_request(request):
    logout(request)
    
    return redirect("talitaApp:login")

def register(request):
    
    if request.method == 'POST':
        
        user_form = UserRegistrationForm(request.POST)
       
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password For security reasons, instead of
            #saving the raw password entered by the user, you use the set_password() method
            #of the user model that handles hashing.
            new_user.set_password(
            user_form.cleaned_data['password'])
            # Save the User object
            
            new_user.save()
            # Create the user profile
            
            return render(request,
            'account/register_done.html',
            {'new_user': new_user})
        else: 
             return render(request,
            'account/register.html',
            {'user_form': user_form}) 
        
          
        
    else:
        user_form = UserRegistrationForm()
        return render(request,'account/register.html',{'user_form': user_form})

def pdf(request):
    category =  request.GET.get('category')
    
    #retrieving images by category
    images = Image.objects.all().filter(user_id = request.user.id, category=category)
    

    
    

    #xhtml2pdf
    template_path= 'account/pdf_template.html'
    context = {
        'user':request.user,
        'images':images,
        'category': category
    }
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    #create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)

    
    return response

def edit(request, pk):
    photo = Image.objects.get(id=pk)
    
    
    if request.method == 'POST':
        data = request.POST
        photo.nameimage = data.get('nameimage')
        photo.save()

        category =  Image.objects.get(id=pk).category
        categories = Image.objects.filter(user_id=request.user.id).values('category').distinct()
        images = Image.objects.filter(user_id=request.user.id,category=category) 

        return render(request,'account/dashboard.html', {'categories': categories,'images':images, 'category':category})
    return render(request, 'account/edit.html',{'photo':photo})

def add(request):
    
    categories = Image.objects.filter(user_id=request.user.id).values('category').distinct()
    user = Profile.objects.get(user_id=request.user.id)
   
    if request.method == 'POST':
        data = request.POST
        imgs = request.FILES.getlist('images')

        

        if data.get('category') == '' and data.get('select') == 'none':
            context = {'error': 'Selecciona una categoria o crea una nueva.'}
            return render(request, 'account/add.html', context)

        elif data.get('category') != '' and data.get('select') != 'none':
            context = {'error': 'Si seleccionas una categoria no puedes crear una al mismo tiempo'}
            return render(request, 'account/add.html', context)

        elif data.get('select') != 'none':
            category = Image.objects.get(category__exact = data.get('select' ))
           
        elif data.get('category') != '':
            category = data.get('category')

        for img in imgs:
            print(img)
            Image.objects.create(
                    user= user,
                    category=category,
                    image=img,
                    nameimage= str(img)           
                )
        # return redirect("talitaApp:dashboard")
        return HttpResponse('<h1>que pedo wwe </h1>')
        

        
        
    return render(request, 'account/add.html', {'categories': categories})

def delete(request, pk):

    category =  Image.objects.get(id=pk).category
    print('###',category)

    card = Image.objects.get(id=pk)
    card.delete()


    categories = Image.objects.filter(user_id=request.user.id).values('category').distinct()
    
    
 
    

    images = Image.objects.filter(user_id=request.user.id,category=category) 
    
    return render(request,'account/dashboard.html', {'categories': categories,'images':images, 'category':category})
    

    