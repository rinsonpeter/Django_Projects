from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from .forms import User_from,Profile_form,Password_form,Signinform,Forgetpasswordform,Edit_profileform
from django.contrib.auth.models import User
from .models import Profile_model
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.tokens import default_token_generator


class Sign_up(TemplateView):
    context={}
    template_name = 'social/signup.html'

    def get(self,request,**kwargs):
        self.context['user_form']=User_from
        self.context['profile_form']=Profile_form
        return render(request,self.template_name,self.context)
    def post(self,request,**kwargs):
        user_form=User_from(request.POST)
        profile_form=Profile_form(request.POST,request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            try:
                email=user_form.cleaned_data.get('email')
                res=User.objects.get(email=email)
                messages.error(request, 'email id taken,try another!')
                return redirect('signup')
            except:
                user=user_form.save()
                new_profile=profile_form.save(commit=False)
                new_profile.profile=user
                new_profile.save()
                tokens=default_token_generator.make_token(user)
                # email

                id=user.id
                name=user.username
                phone=new_profile.phone
                emailadress=user.email
                host=request.get_host()
                email=user_form.cleaned_data.get('email')
                subject = 'Log In Authentication'
                html_message = render_to_string('social/email_page.html',
                 {'context':id,'host':host,'name':name,'phone':phone,'email':emailadress,'token':tokens})
                plain_message = strip_tags(html_message)
                from_email = 'mctraining1993@gmail.com'
                to = email

                mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)
        else:
            self.context['user_form'] = user_form
            self.context['profile_form'] = profile_form
            return render(request, self.template_name, self.context)
        return redirect('signup')

class email_page(TemplateView):

    def get(self, request, *args, **kwargs):
        return render(request,'social/email_page.html')

class Verification(TemplateView):
    context={}
    template_name = 'social/verification.html'

    def get(self, request, **kwargs):
        self.context['form']=Password_form
        return render(request,self.template_name,self.context)
    def post(self, request, **kwargs):
        tokens=kwargs.get('token')
        id=kwargs.get('id')
        user=User.objects.get(id=id)
        form=Password_form(request.POST)
        if form.is_valid() and default_token_generator.check_token(user,tokens):
            password=form.cleaned_data.get('password1')
            user.set_password(password)
            user.save()
            login(request,user)
            return redirect('home')
        else:
            self.context['form']=form
            return render(request,self.template_name,self.context)

class Signin(TemplateView):
    template_name = 'social/login.html'
    form_class=Signinform

    def get(self,request,**kwargs):
        context={}
        context['form']=self.form_class
        return render(request,self.template_name,context)

    def post(self,request,**kwargs):
        context={}
        form=self.form_class(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            pwd = form.cleaned_data.get('password')
            try:
                username=User.objects.get(email=email).username
            except:
                messages.error(request, 'Email not Resgistered')
                return redirect('signin')

            user = authenticate(request, username=username, password=pwd)
            if user:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Password not correct')
                context['form'] = form
                return render(request, self.template_name, context)

        context['form'] = form
        return render(request, self.template_name, context)

class Forgot_password(TemplateView):
    context={}
    form_class=Forgetpasswordform
    template_name = 'social/forgot.html'

    def get(self, request, *args, **kwargs):
        self.context['form']=self.form_class
        return render(request,self.template_name,self.context)

    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            email=form.cleaned_data.get('email')
            try:
                user=User.objects.get(email=email)
            except:
                messages.error(request, 'Email not Resgistered')
                return redirect('forgot')

            #email
            tokens=default_token_generator.make_token(user)
            id = user.id
            name = user.username
            phone=Profile_model.objects.get(profile=user).phone
            emailadress = user.email
            host = request.get_host()
            email = email
            subject = 'Password Reset'
            html_message = render_to_string('social/email_page.html', {'context': id, 'host': host,'name':name,'phone':phone,'email':emailadress,'token':tokens})
            plain_message = strip_tags(html_message)
            from_email = 'mctraining1993@gmail.com'
            to = email

            mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)

        self.context['form'] = form
        return render(request, self.template_name, self.context)

class Signout(TemplateView):

    def get(self, request, *args, **kwargs):
        logout(self.request)
        return redirect('signin')

class Home(LoginRequiredMixin,TemplateView):
    login_url = '/social/signin'
    context={}
    template_name = 'social/home.html'

    def get(self, request, *args, **kwargs):
        user=request.user
        profile_info = Profile_model.objects.get(profile=user)
        self.context['profile'] = profile_info
        self.context['current_user'] = user
        tokens=default_token_generator.make_token(user)
        self.context['token']=tokens
        return render(request, self.template_name, self.context)

class Edit_profile(TemplateView):
    context={}
    template_name = 'social/edit_profile.html'
    form_class=Edit_profileform

    def get(self, request, *args, **kwargs):
        form=self.form_class
        self.context['form']=form
        return render(request,self.template_name,self.context)

    def post(self,request, *args, **kwargs):
        form=self.form_class(request.POST,request.FILES)
        if form.is_valid():
            image=form.cleaned_data.get('profile_pic')
            profile_edit=Profile_model.objects.get(profile=request.user)
            profile_edit.profile_pic=image
            profile_edit.save()
            return redirect('home')
        return redirect('home')
