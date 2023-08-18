from django.urls import path
from django.conf import settings
from django.conf.urls.static import static 
from django.contrib.auth import views as auth_views
from ragavendra_store.views import home,createAccount,Updatepassword,editprofile,orders,logout,page_not_found_view
urlpatterns = [
    path('',home,name="login"),
    path('forgotpassword/',Updatepassword, name='forgotpassword'),
    path('orders/',orders, name='orders'),
    path('register/',createAccount, name='register'),
    path('profile/',editprofile,name="profile"),
    path('logout/',logout,name="logout"),
    path('not_found/',page_not_found_view, name='not_found'),
    path('password_reset/',auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done',auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    # path('4a6a2ee7-4431-4e22-9913-73930326f7f9',whatswebhook, name='whats_web_hook'),
    
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
