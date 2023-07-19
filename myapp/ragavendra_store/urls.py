from django.urls import path
from django.conf import settings
from django.conf.urls.static import static 
from ragavendra_store.views import home,createAccount,Updatepassword,editprofile,orders,logout
urlpatterns = [
    path('',home,name="login"),
    path('forgotpassword/',Updatepassword, name='forgotpassword'),
    path('orders/',orders, name='orders'),
    path('register/',createAccount, name='register'),
    path('profile/',editprofile,name="profile"),
    path('logout/',logout,name="logout"),
    # path('4a6a2ee7-4431-4e22-9913-73930326f7f9',whatswebhook, name='whats_web_hook'),
    
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)