from django.conf import settings
from django.contrib import admin
from django.contrib.auth import views as auth_view 

from django.urls import path
from .views import CustomLoginView,upload_file,upload_file_page,UploadedFile,customer_details,login,CustomerRegistrationForm,shantaram,CustomerRegistrationForm,ProfileView,basemap,user_details,login_required,logout,LoginForm,LoginView,index,zoneDetail,planSurvey,mapCalculator,autocomplete,searchOnClick,convert_To_Geojson,save_location,get_locations,delete_location,before_payment,payment_done,locations,getInfoValues
from django.conf.urls.static import static

from TCPLapp import views
from .forms import Customer2,CustomerProfileForms,CustomerRegiForm,MyPasswordResetForm,MyPasswordResetConfirm,ChangePassword
# from TCPLapp.forms import LoginForm,MyPasswordResetConfirm,MyPasswordResetForm,ChangePassword




urlpatterns = [
# path("admin/", admin.site.urls),
#path('', auth_view.LoginView.as_view(template_name="TCPLapp/login.html",authentication_form=LoginForm),name="login"),

path('', CustomLoginView.as_view(),name="login"),

path('registration/', CustomerRegistrationForm.as_view(),name="customerregistration"),
  
path('profile/', ProfileView.as_view(), name='profile'),

path('basemap/', basemap, name='basemap'),
   
path('user_details/', user_details, name='user_details'),

#change password
path('changepassword/',auth_view.PasswordChangeView.as_view(template_name="TCPLapp/changepassword.html",form_class=ChangePassword,success_url="/changepassworddone/"),name="changepassword"),
     
path('changepassworddone/',auth_view.PasswordChangeView.as_view(template_name="TCPLapp/changepassworddone.html"),name="changepassworddone"),


#forgot password
path("password-reset/",auth_view.PasswordResetView.as_view(template_name="TCPLapp/password_reset.html",form_class=MyPasswordResetForm),name="password_reset"),
    
path("password-reset/done/",auth_view.PasswordResetDoneView.as_view(template_name="TCPLapp/password_reset_done.html"),name="password_reset_done"),
    
path("password-reset-confirm/<uidb64>/<token>/",auth_view.PasswordResetConfirmView.as_view(template_name="TCPLapp/password_reset_confirm.html",form_class=MyPasswordResetConfirm),name="password_reset_confirm"),

path("password-reset-complete/",auth_view.PasswordResetCompleteView.as_view(template_name="TCPLapp/password_reset_complete.html"),name="password_reset_complete"),
    
#admin
# path('admin123/', admin123,name='admin123'),

path('customer_details/<int:id>',customer_details,name='customer_details'),
     
#    path('user/', views.user,name='user'),
   
#    path('profile/', views.ProfileView.as_view(), name='profile'),
   
   
   
    
    
    #path('main/', views.main,name='main'),
    
    
    
    # path('user_details/<int:id>/', views.user_details,name='user_details'),
    
path('logout/',logout,name='logout'),
    
    # #path('coordinates/',views.coordinates,name='coordinates'),
    
path('index/', index,name='index'),
    
path('zoneDetail/', zoneDetail,name='zoneDetail'),

path('planSurvey/', planSurvey,name='planSurvey'),
    
path('mapCalculator/', mapCalculator,name='mapCalculator'),
    
path('upload_file_page/',upload_file_page, name='upload_file_page'),
   
path('upload_file/', upload_file, name='upload_file'),

#search urls
path('autocomplete/', autocomplete, name='autocomplete'),
    
path('searchOnClick/', searchOnClick, name='searchOnClick'),
    
# path('Out_table/',Out_table, name='Out_table'),
#bookmark   
path('save-location/',save_location, name='save_location'),
    
path('get-locations/',get_locations, name='get_locations'),
    
path('delete-location/',delete_location, name='delete_location'),

#payment

path('before_payment/',before_payment, name='before_payment'),    
path('paymentdone/',payment_done, name='paymentdone'),

#search coordinates

#path('Search_coordinates/', views.Search_coordinates, name='Search_coordinates'),

#path('selected_data/', views.selected_data, name='selected_data'),

path('locations/', locations, name='locations'),

path('getInfoValues/', getInfoValues, name='getInfoValues'),

path('user_details/', user_details, name='user_details'),

# path('Queryform/',views.Queryform , name='Queryform'),
path('Queryform/', views.Queryform.as_view(),name="Queryform"),


# path('ward/', views.ward_table, name='ward'),
path('ward/', views.ward, name='ward'),


# path('ward/<str:user_role>/', views.ward_view, name='ward'),
path('select_by_location/', views.select_by_location, name='select_by_location'),

    
#admin
# path('Index/', superadmin,name='superadmin'),
path('shantaram/', shantaram,name='shantaram'),

# path('Index/', user,name='user'),
    
   # path('fetch_searchdata/<int:id>/',views.fetch_searchdata, name='fetch_searchdata')
   

path('trial/', views.trial, name='trial'),

    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
