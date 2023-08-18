from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
# from ragavendra_store.models import Orders
from ragavendra_store.models import Orders
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import requests
import json
from twilio.rest import Client
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from .models import User_info
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.utils.encoding import force_bytes, force_str
from django.urls import reverse
from django.core.mail import EmailMessage


# Create your views here.
def home(request):
    if request.method=='POST':
        username = request.POST.get('username',"")
        password = request.POST.get('pass',"")
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user )
            return HttpResponseRedirect('/orders/') 
        else:
            messages.error(request, 'Invalid username or password')
    return render(request ,"static_pages/home.html")

def createAccount(request):
    if request.method=='POST':
        fname = request.POST.get('fname',"")
        lname = request.POST.get('lname',"")
        email = request.POST.get('email',"")
        username = request.POST.get('username',"")
        password = request.POST.get('password',"")

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('/register/')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            return redirect('/register/') 
        oUser_info = User.objects.create_user(username=username,password=password,first_name=fname,last_name=lname,email=email)
        oUser_info.save()
        return HttpResponseRedirect('/') 
            
    return render(request ,"static_pages/create-account.html")
               
               
@login_required
def orders(request):
    tracking_id = ''
    if request.method=='POST':
        name = request.POST.get('Name',"")
        whatsapp_No = request.POST.get('WhatsappNo',"")
        contact_no = request.POST.get('ContactNo',"")
        address = request.POST.get('Address',"")
        streetname = request.POST.get('streetname',"")
        city = request.POST.get('City',"")
        courier = request.POST.get('Courier',"")
        state = request.POST.get('State',"")
        postalcode = request.POST.get('Postalcode',"")
        state = request.POST.get('State',"")
        Transactionid  = request.POST.get('TransactionNo',"")
        No_of_items = request.POST.get('No_of_items',"")
        tracking_id = Transactionid
        # up_file = request.FILES['image_file']
        # upload_file = settings.MEDIA_URL[1:] + "//img//" + str(up_file.name)
        for item in range(int(No_of_items)):
            size =  "size"+str(item)
            color = "item_Color"+str(item) 
            image = "image_file"+str(item)
            Color = request.POST.get(color,"")
            Size = request.POST.get(size,"")
            up_file = request.FILES[image]
            upload_file = settings.MEDIA_URL[1:] + "//img//" + str(up_file.name)
            
            user_item = Orders.objects.filter(user=request.user)
            oOrder_info = Orders(Name=name,WhatsappNo=whatsapp_No,ContactNo=contact_no,Address=address, street_name=streetname,city=city,state=state,postal_code=postalcode,Courier=courier,TransactionId=Transactionid,No_Of_Items=No_of_items,item_color=Color, item_size=Size, file=up_file,user=request.user)
            oOrder_info.save()
            message = f'welcome {request.user} thank for order raghavendra textiles '
        # send_whatsapp_message(message=message,whatsapp_no=whatsapp_No)
        return HttpResponseRedirect('/orders/')
    unique_orders = []
    orders_list = Orders.objects.filter(user=request.user).values_list('TransactionId', flat=True).distinct()
    for transaction_id in orders_list:
        order = Orders.objects.filter(user=request.user, TransactionId=transaction_id).first()
        unique_orders.append(order)
    view_orders_list = Orders.objects.all()
    oUser_INFO = User_info.objects.filter(userid = request.user.id)
    oUser = User_info.objects.filter(userid = request.user.id).first()
    profile_data = User_info.objects.filter(userid=request.user.id).values()
    profile_json = json.dumps(list(profile_data))
    return render(request ,"static_pages/orders.html" ,{"orders_list":unique_orders,"view_orders_list":view_orders_list,'profile':oUser_INFO,"profile_json": profile_json,'active_user':oUser})


# def Updatepassword(request):
#     if request.method=='POST':
#         username = request.POST.get('Username',"")
#         password = request.POST.get('password',"")
#         re_password = request.POST.get('re-password',"")
#         user_item = User.objects.filter(username = username)
#         for user in user_item:
#             if user is None:
#                 messages.error(request, 'user not found')
#             elif password != re_password:
#                 messages.error(request, 'password does not match')
#             else:
#                 hashed_password = make_password(password, hasher='pbkdf2_sha256')
#                 user.password=hashed_password
#                 user.save()
#                 return redirect('/') 
        
#     return render(request ,"static_pages/forgotpassword.html")

def Updatepassword(request):
    if request.method=='POST':
        username = request.POST.get('Username',"")
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, 'User not found.')
        else:
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            url = 'http://127.0.0.1:8000'
            reset_link = url + reverse('password_reset_confirm', kwargs={'uidb64': uid, 'token': token})
            
            email_subject = 'Password Reset Request'
            email_message = render_to_string('static_pages/reset_password_email.html', {
                'user': user,
                'reset_link': reset_link,
              
            })
            
            send_mail(email_subject, email_message, 'manideep723@gmail.com', [user.email])
            send_mail.content_subtype = 'html'
           
            messages.success(request, 'Password reset link sent to your email.')
         
        
        
       
        
    return render(request ,"static_pages/forgotpassword.html")



@login_required
def editprofile(request):
    user_item = User.objects.filter(username = request.user)
    for item in user_item:
        if request.method == 'POST':
            userId = item.id
            phonenumber = item.username
            firstname = item.first_name
            lastname = item.last_name
            email = item.email
            city = request.POST.get('city',"")
            state = request.POST.get('state',"")
            zip = request.POST.get('zip',"")
            address = request.POST.get('address',"")
            reciepent_name = request.POST.get('reciepent_name',"")
            address_type = request.POST.get('address_type',"")
            if User_info.objects.filter(Reciepentname=reciepent_name, phonenumber=phonenumber).exists():
                messages.error(request, 'profile address allreddy exists.') 
                return redirect('/profile/') 
            else:
                profile_info = User_info(phonenumber=phonenumber,Address_type=address_type,address=address,city=city,state=state,zip_code=zip,firstname=firstname,lastname=lastname,email=email,Reciepentname=reciepent_name, userid=userId) 
                profile_info.save()
                messages.info(request, 'sucessfully create profile address')
                return redirect('/orders/') 
        oUser_data =User_info.objects.filter(userid=request.user.id)
            
    
    return render(request ,"static_pages/profile.html",{'user_data':item,'oUser_data':oUser_data})


# @login_required
# def editprofile(request):
#     user_item = User.objects.filter(username=request.user).first()

#     if request.method == 'POST':
#         userId = user_item.id
#         phonenumber = user_item.username
#         firstname = user_item.first_name
#         lastname = user_item.last_name
#         email = user_item.email
#         city = request.POST.get('city', "")
#         state = request.POST.get('state', "")
#         zip_code = request.POST.get('zip', "")
#         address = request.POST.get('address', "")
#         address_type = request.POST.get('address_type', "")

#         if User_info.objects.filter(Address_type=address_type, phonenumber=phonenumber).exists():
#             messages.error(request, 'Profile address already exists.')
#             return redirect('/profile/')
#         else:
#             profile_info = User_info(
#                 user=user_item,
#                 phonenumber=phonenumber,
#                 Address_type=address_type,
#                 address=address,
#                 city=city,
#                 state=state,
#                 zip_code=zip_code,
#                 firstname=firstname,
#                 lastname=lastname,
#                 email=email,
#                 userid=userId
#             )
#             profile_info.save()
#             messages.info(request, 'Successfully created profile address')
#             return redirect('/orders/')

#     user_info = User_info.objects.filter(user=user_item)
    
#     context = {
#         'user_data': user_item,
#         'user_info': user_info,
#     }
    
#     return render(request, "static_pages/profile.html", context)


   

    

    




def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")


from django.shortcuts import render

def page_not_found_view(request, exception):
    return render(request, 'static_pages/404.html', status=404)
    
   
        



# def register(request):
#     if request.method == 'POST':
#         user_form = createAccount(request.POST)
#         profile_form = ProfileForm(request.POST)
#         if user_form.is_valid() and profile_form.is_valid():
#             user = user_form.save()
#             profile = profile_form.save(commit=False)
#             profile.user = user
#             profile.save()
#             return redirect('registration_success')  # Redirect to success page
#     else:
#         user_form = UserForm()
#         profile_form = ProfileForm()
#     return render(request, 'registration.html', {'user_form': user_form, 'profile_form': profile_form})


# def send_whatsapp_message(whatsapp_no,message):
#     whatsapp_no = "+91"+ str(whatsapp_no)
#     message = message
#     headers = {"Authorization": settings.WHATSUP_TOKEN}
#     payload = {
#             "messaging_product": "whatsapp",
#             "recipient_type": "individual",
#             "to": whatsapp_no,
#             "type": "text",
#             "text": {"body": message}
#         }
#     response = requests.post(settings.WHATSUP_URL, headers=headers, json=payload)
#     ans = response.json()
#     return  "success"
    
 

# def Sendwhatsappmessage ( whatsapp_No,message):
#     headers={"Authorization":settings.WHATSUP_TOKEN}
#     payload={"messaging_product":"whatsapp",
#              "recipient_type": "individual",
#              "to":whatsapp_No,
#              "type":"text",
#              "text":{"body":message}
#              }
#     response = requests.post(settings.WHATS_URL,headers=headers,json=payload)
#     ans = response.json()
# @csrf_exempt
# def whatswebhook(request):
#     if request.method == 'GET':
#         VERFIY_TOKEN = "8f08d35c-d4a3-4ce0-bec8-db786e9a100f"
#         mode = request.GET['hub.mode']
#         token = request.GET['hub.verify_token']
#         challenge = request.GET['hub.challenge']

#         if mode == 'subscribe' and token == VERFIY_TOKEN:
#             return HttpResponseRedirect(challenge, status =200)
#         else:
#             return HttpResponseRedirect('error',status=403)
    

    if request.method == 'POST':
        data = json.loads(request.body)
        return HttpResponseRedirect ('success' ,status=200)
    

# def send_whatsapp_message(whatsapp_no,message):
     
#      account_sid = 'ACfc60d1654dbf6d92b0eb377745fa65da'
#      auth_token = '23b1dacf7c707bad168e259044b0fb3c'
#      client = Client(account_sid, auth_token)

#      message = client.messages.create(
#      from_='whatsapp:+14155238886',
#      body=message,
#      to="whatsapp:+919154224347"

#      ) 
    
#      return  "success"



