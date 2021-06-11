from decimal import Context
from django.contrib.auth.forms import PasswordResetForm

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from account.tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage

from account.forms import MyForgotPassForm, RegistrationForm, MyPasswordResetForm, UserLoginForm
from account.models import Account

def register_view(request):
    """ 
        register here... send email verification link..
    """
    template_name='account/registration.html'
    context={}
    form=RegistrationForm()
    context['form']=form
    if request.method=='POST':
        form=RegistrationForm(data=request.POST,
                              files=request.FILES) 
        if form.is_valid():
            print("isvalid")
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            print("user.PK value",user.pk)
            print(urlsafe_base64_encode(force_bytes(user.pk)))
            print(account_activation_token.make_token(user))

            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            print("email sent success")
            return redirect("regconfirm")
        else:
            print("email sent failed")
            print("invalid else POST method")
            context['form']=form
            return render(request,'account/registration.html',context)

    return render(request,template_name,context)

def activate(request, uidb64, token):
    template_name='account/reset_pass.html'
    form=MyPasswordResetForm()
    context={'form':form}
    print("inside activate method")
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = Account.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        print("inside val")
        if request.method=='POST':
            form=MyPasswordResetForm(request.POST)
            if form.is_valid():
                print("inside valid")
                pswd=request.POST.get('Confirm_Password')
                print("password creeated:  ",pswd)
                user.set_password(pswd)
                user.is_active = True
                user.save()
                login(request, user)
                return redirect("home")
            else:
                context['form']=form    
                return render(request,'account/reset_pass.html',context)        
                
    return render(request,'account/reset_pass.html',context)       

def regconfirm(request):
    """ email verify redirects here for 
        password set up , then to login
        page
    """
    template_name='account/reg_confirm.html'

    return render(request,template_name)

@login_required(login_url ='user_login')
def home(request):
    """login with email and Password
    """
    template_name='account/homepage.html'
    context={}
    return render(request,template_name,context)

def user_login(request):
    """login with email and Password
    """
    print("insde login view")

    form=UserLoginForm()
    template_name='account/user_login.html'
    context={}
    context['form']=form

    if request.method=="POST":
        form=UserLoginForm(request.POST)
        if form.is_valid():
            email=request.POST.get("email")
            password=request.POST.get("password")
            print("inside request.POST",email,password)
            user=authenticate(request,email=email,password=password)
            if user is not None:
                login(request,user)
                return redirect("home")
        else:
            context['form']=form
            return render(request,template_name,context)        

    print("else case login")
    return render(request,template_name,context)    

def logoutview(request):
    logout(request)
    return redirect("user_login")

def forgotPasswordView(request):
    template_name='account/forgotpass.html'
    form=MyForgotPassForm()
    context={}
    context['form']=form
    if request.method=="POST":
        form=MyForgotPassForm(request.POST)
        print("inside post")
        print(form.errors)
        if form.is_valid():
            print("inside is valid forgot")
            to_email = form.cleaned_data.get('email')
            print("to email : ",to_email)
            user=Account.objects.get(email=to_email)
            current_site = get_current_site(request)
            mail_subject="Reset Password"

            message=render_to_string('pass_reset_email.html',{
                'user':user,
                'domain':current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            print("forgot pass email send")
            return redirect("forgotConfirm")
        else:
            print("email send failed forgot")
            context['form']=form
            return render(request,template_name,context)

    return render(request,template_name,context)
   
def forgotConfirm(request):
    """ forgot Password template 
        Please check your email for password reset link
    """
    template_name="account/forgotConfirm.html"

    return render(request,template_name)
