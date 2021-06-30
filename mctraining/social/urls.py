from django.urls import path
from .views import Sign_up,Verification,Signin,Home,Signout,Forgot_password,Edit_profile

urlpatterns = [
    path('signup',Sign_up.as_view(),name='signup'),
    path('verification/<int:id>/<str:token>',Verification.as_view(),name='verification'),
    path('signin',Signin.as_view(),name='signin'),
    path('home',Home.as_view(),name='home'),
    path('signout',Signout.as_view(),name='signout'),
    path('forgot_password',Forgot_password.as_view(),name='forgot'),
    path('Edit_profile',Edit_profile.as_view(),name='edit'),
]