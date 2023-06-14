from django.urls import path
from . import views
from apartment.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_ROOT, MEDIA_URL
from django.conf.urls.static import static
urlpatterns=[
    path('signup',views.signup,name='signup'),
    path('login',views.Login,name='login'),
    path('',views.Home,name='home'),
    path('logout',views.Logoutpage,name='logout'),
    path('email',views.send_template_email,name='email'),
    path('contact',views.Contact,name='contact'),
    path('about',views.About,name='about'),
    path('booking',views.Booking,name='booking'),


]

if DEBUG:
    urlpatterns += static(STATIC_URL,document_root=STATIC_ROOT)
    urlpatterns += static(MEDIA_URL,document_root=MEDIA_ROOT)

