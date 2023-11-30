import os
from django.conf import settings
from django.shortcuts import render,HttpResponse,redirect, get_object_or_404 ,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
from .models import Customer2, DownloadFile, Location, PmcMissingLinks, PuneAdminWards, Query, UploadedFile, VillageBoundary, Revenue1,FinalPlu,Payment

from urllib.parse import quote  # Import quote for URL encoding
import requests
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import check_password
from django.contrib.auth.views import LoginView
from .models import UploadedFile
from django.views import View
from django.core.files.storage import FileSystemStorage
from django.utils.decorators import method_decorator
from django.http import JsonResponse, HttpResponse
from django.contrib.gis.geos import Point
from django.contrib.gis.geos import LineString
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.serializers.geojson import Serializer as GeoJSONSerializer
from django.contrib.gis.db.models import Q
from django.contrib.auth.forms import AuthenticationForm
import json
import geopandas as gpd
from pyproj import CRS
import requests
from django.contrib import messages
from .forms import CustomerProfileForms,CustomerRegiForm, LoginForm, QueryForm

# WARD_DETAILS


from .models import *
import openpyxl
from django.core import serializers
from owslib.wms import WebMapService
# import matplotlib.pyplot as plt
from .models import SearchHistory
from django.utils import timezone
from io import BytesIO
import io
from django.contrib.auth import authenticate
# from .forms import uploadFileForm
from collections import OrderedDict
 
import re
###################### new code ##########################



from django.contrib.auth.views import LoginView
# from django.shortcuts import redirect

class CustomerRegistrationForm(View):
    def get(self,request):
        form=CustomerRegiForm()
        
        return render(request,'TCPLapp/customerregistration.html',{"form":form})
    
    def post(self,request):
        form=CustomerRegiForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request,'TCPLapp/customerregistration.html',{"form":form})


class CustomLoginView(LoginView):
    template_name = "TCPLapp/login.html"
    authentication_form = LoginForm  # Use Django's built-in AuthenticationForm


    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        # Authenticate the user using Django's built-in authentication
        user = authenticate(username=username, password=password)

        if user is not None:
            login(self.request, user)  # Log in the authenticated user
            # if username == 'superadmin':
            #     return redirect('superadmin')
            if username == 'shantaram':
                return redirect('shantaram')
            # else: 
            #     return redirect('user')

            # login(self.request, user)  # Log in the authenticated user

            # if username == 'admin123':
            #     return redirect('admin123')
            else:
                try:
                    customer = Customer2.objects.get(user=user)
                    return redirect('ward')
                except Customer2.DoesNotExist:
                    return redirect('ward')

        return super().form_valid(form)
  
  
# class CustomLoginView(LoginView):
#     template_name = "TCPLapp/login.html"
#     authentication_form = LoginForm  # Use Django's built-in AuthenticationForm   

#     def form_valid(self, form):
#         username = form.cleaned_data.get('username')
#         password = form.cleaned_data.get('password')
#         user = authenticate(username=username, password=password)

#         if user is not None:
#             login(self.request, user)
#             if username == 'admin':
#                 user_role = 'admin'
#             else:
#                 user_role = 'non_admin'

#             return redirect('ward', user_role=user_role)

#         return super().form_valid(form)

    
# def admin123(request):
#     data1=User.objects.all()
   
#     count=data1.count()                                                                               
    
#     context={'data1':data1,'count':count}
#     return render(request, 'TCPLapp/admin123.html',context)

# def superadmin(request):

#     return render(request, 'TCPLapp/superadmin.html')

def shantaram(request):

    return render(request, 'TCPLapp/shantaram.html')

# def user(request):

#     return render(request, 'TCPLapp/user.html')

def customer_details(request,id):
    data1= Customer2.objects.filter(user_id=id)
    print(data1,'qqqqqqqqqqqqqqqqqqqqqqqqqqqqqq')
    customer_details=[]
    
    for i in data1:
       
        user=i.user_id
        fullname=i.fullname
        mobileno=i.mobileno
        occupation=i.occupation
        industry=i.industry
                
        customer_data = {'user': user, 'fullname':fullname,'mobileno':mobileno,'occupation':occupation,'industry':industry}

        # print(customer_data,'anuppppp')
        customer_details.append(customer_data)
        
        # print(customer_details,'aaaaaaaaaaaaaaaaaaaaaaaaaaaa')
            
   
  
    return render(request, 'TCPLapp/customer_details.html',{'customer_details':customer_details})




#_____________ profile _____________________________
@method_decorator(login_required,name='dispatch')
class ProfileView(View):
    def get(self,request):
        form=CustomerProfileForms()
        return render(request,'TCPLapp/profile.html',{"form":form,"active":"btn-primary"})
    
    def post(self,request):
        form=CustomerProfileForms(request.POST)
        if form.is_valid():
            usr=request.user
            fullname=form.cleaned_data["fullname"]
            
            mobileno=form.cleaned_data["mobileno"]
            
            dob=form.cleaned_data["dob"]

            address=form.cleaned_data['address']

            city=form.cleaned_data["city"]
            
            pin_code=form.cleaned_data["pin_code"]         
            
            occupation=form.cleaned_data["occupation"]

            industry = form.cleaned_data["industry"]
            
            if Customer2.objects.filter(user=usr).exists():
                messages.warning(request, "Profile data already exists.")
                return redirect('profile')  # Redirect to the profile page or another suitable page
            
            reg=Customer2(user=usr,fullname=fullname,mobileno=mobileno,city=city,pin_code=pin_code,occupation=occupation,address=address,dob=dob,industry=industry)#
            
            
            reg.save()
            messages.success(request,"Congratulations !! Profile Updated Successfully")
       
            return render(request, 'TCPLapp/profile.html',{"form":form,"active":"btn-primary"})

#_______________user_details______________________
@login_required
def user_details(request):
    add=Customer2.objects.filter(user=request.user) 
    # print(add,'aaaaaa')#This is to get the current user,it solve the problem like to store user in login as a session.
    
    return render(request, 'TCPLapp/user_detailss.html',{"add":add,"active":"btn-primary"})
    

    

@login_required(login_url="login")
def changepassword(request):
    
    return render(request, 'TCPLapp/changepassword.html')

# @login_required(login_url="login")
def profilepage(request):
    return render(request, 'TCPLapp/profile.html')

########################################################


def basemap(request):
    return render(request, 'TCPLapp/basemap.html')


def index(request):
    return render(request, 'TCPLapp/index.html')
@login_required(login_url="login")

def logout(request):
    # Do not use "return render" here
    # return render(request, 'TCPLapp/login.html')
    return redirect("login")
@login_required(login_url="login")

def zoneDetail(request):
      return render(request, 'TCPLapp/zoneDetail.html')
@login_required(login_url="login")

def planSurvey(request):
      return render(request, 'TCPLapp/planSurvey.html')
  
@login_required(login_url="login") 
def mapCalculator(request):
      return render(request, 'TCPLapp/mapCalculator.html')
  
  
def upload_file_page(request):
      return render(request, 'TCPLapp/upload_file.html')
    
@login_required(login_url="login")
def before_payment(request):
      add=Customer2.objects.filter(user=request.user)
      return render(request, 'TCPLapp/before_payment.html',{"add":add})
    
@login_required(login_url="login")
def payment_done(request):
    user=request.user  
    cust=Customer2.objects.filter(user=user)
    pay=Payment(user=user).save()
    
    return redirect("upload_file")


@login_required
def upload_file_page(request):
    return render(request, 'TCPLapp/upload_file.html')

@login_required
# @staticmethod   
def upload_file(request):
        if request.method == 'POST' and 'file' in request.FILES:
            # Check if the user is authenticated
            if request.user.is_authenticated:
                uploaded_file = request.FILES['file']
                allowed_extensions = ['.jpg', '.jpeg', '.pdf', '.tif', '.tiff']

                if any(uploaded_file.name.lower().endswith(ext) for ext in allowed_extensions):
                    # Save the uploaded file using the model
                    uploaded_file_instance = UploadedFile(files1=uploaded_file, user_id1=request.user)
                    uploaded_file_instance.save()

                    message = 'File uploaded successfully!'
                else:
                    message = 'Invalid file format. Allowed formats: JPG, PDF, TIFF.'
            else:
                message = 'User is not authenticated.'
        else:
            message = ''
        return render(request, 'TCPLapp/upload_file.html', {'message': message})
    
    
@login_required(login_url="login")
def download_file(request):
    files = DownloadFile.objects.filter(user_id1=request.user)
    print(request.user,"...............")
    return render(request, "TCPLapp/user_details.html", {"files": files})    

@login_required(login_url="login")
def user_details(request):
    add=Customer2.objects.filter(user=request.user) 
    #This is to get the current user,it solve the problem like to store user in login as a session.
    
    file=UploadedFile.objects.filter(user_id1=request.user)
    
    files = DownloadFile.objects.filter(user_id1=request.user)
    
    return render(request, 'TCPLapp/user_detailss.html',{"add":add,"file":file,"files":files,"active":"btn-primary"})



    
##############################search_button orginal#######################################################################

pattern =r'(^(?P<village_name>[\w\s\(\)\.-]+),(?P<taluka_name>[\D\\w\s\(\)\.-]+)(?:,(?P<gut_numbers>\d+(?:,\d+)*))?$)|(?P<xy>\b\d+\.\d+\s*,\s*\d+\.\d+\b)'


def getInfoValues(request):
    selected_layer = request.GET.get('selected_layer')
    print(selected_layer,"______________________________________")
    if request.method == 'POST':
        selected_value = request.POST.get('radio_field')


                
    return JsonResponse(products1, safe=False)           
            

# ****************PDF TABLE***************************************

# def Out_table(request):
    
#     # response = request.GET.get("selected_value").split(",")
#     # villageName, talukaName, gutNumber = response[0], response[1], response[2:]
#     # gutnumber2=response[2:]
    
    
#     # products1 = Revenue1.objects.filter(taluka=talukaName, village_name_revenue=villageName, gut_number=str(gutNumber[0]))
#     # intersection_query = Q(geom__intersects=products1[0].geom)
    
    
#     # for product in products1[1:]:
#     #     intersection_query |= Q(geom__intersects=product.geom)
#     # plu = FinalPlu.objects.filter(intersection_query)
#     # data = []
#     # for Iplu in plu:
#     #     intersection_area = Iplu.geom.intersection(products1[0].geom).area
      
#     #     data.append(Iplu.broad_lu)
#     #     data.append(intersection_area)
        
#     # data1 = {
        
#     #     "Village_Name": villageName,
#     #     "Taluka_Name": talukaName,
#     #     "Gut_Number": gutNumber,
#     #     "selected_values": data
#     # }

   
    
#     # return JsonResponse(data1,safe=False) 

#     return JsonResponse(safe=False) 


# def Queryform(request):
class Queryform(View):
    def get(self,request):
        form=QueryForm()
        return render(request,'TCPLapp/Queryform.html',{"form":form,"active":"btn-primary"})
    
    def post(self,request):
        form=QueryForm(request.POST)
        if form.is_valid():
            usr=request.user
            gutno=form.cleaned_data["gutno"]
            villagename=form.cleaned_data["villagename"]
            ownername=form.cleaned_data["ownername"]
            Buildingtype=form.cleaned_data["Buildingtype"]
            comment=form.cleaned_data["comment"]
            upload_file=form.cleaned_data["upload_file"]            
            
            
            if Query.objects.filter(user=usr).exists():
                messages.warning(request, "Data already Updated.")
                return redirect('Queryform')  # Redirect to the profile page or another suitable page
            
            comment=form.cleaned_data["comment"]
            reg=Query(user=usr,gutno=gutno,villagename=villagename,ownername=ownername,Buildingtype=Buildingtype,comment=comment,upload_file=upload_file)#
            
            
            reg.save()
            messages.success(request,"Congratulations !! Information Updated Successfully")
       
            return render(request, 'TCPLapp/Queryform.html',{"form":form,"active":"btn-primary"})

    
    # return render (request,'TCPLapp/Queryform.html')



#############################################################changesearchdata##############################################################
# 

# Save BookMarks_____________________________

# @csrf_exempt
# @login_required
# def save_location(request):
#     if request.method == 'POST':
#         latitude = request.POST.get('latitude')
#         longitude = request.POST.get('longitude')
#         name = request.POST.get('name')
#         username = request.POST.get('username')

#         location = Location(user=request.user, name=name,
#                             latitude=latitude, longitude=longitude)
#         location.save()

#         return JsonResponse({'message': 'Location saved successfully.'})
#     else:
#         return JsonResponse({'message': 'Invalid request method.'})


# def get_locations(request):
#     locations = Location.objects.filter(user=request.user)
#     data = {
#         'locations': list(locations.values('id','name', 'latitude', 'longitude'))
#     }
#     return JsonResponse(data)

class SaveLocationView(View):
    def post(self, request, *args, **kwargs):
        user = request.user
        latitude = request.POST.get('lat')
        longitude = request.POST.get('lng')
        name = request.POST.get('name')

        BookmarkedLocation.objects.create(user=user, latitude=latitude, longitude=longitude, name=name)

        return JsonResponse({'status': 'success'})

@login_required(login_url='login')
def get_locations(request):
    user = request.user
    locations = BookmarkedLocation.objects.filter(user=user).values('id', 'name', 'latitude', 'longitude')
    return JsonResponse(list(locations), safe=False)



#delete_location
@csrf_exempt
@login_required
def delete_location(request):
    if request.method == 'POST':
        location_id = request.POST.get('locationId')
        try:
            location = Location.objects.get(id=location_id)
            if location.user == request.user:
                location.delete()
                return JsonResponse({'message': 'Location deleted successfully.'})
            else:
                return JsonResponse({'message': 'Unauthorized access.'}, status=401)
        except Location.DoesNotExist:
            return JsonResponse({'message': 'Location not found.'}, status=404)
    else:
        return JsonResponse({'message': 'Invalid request method.'}, status=400)
    
def locations(request):
    return render(request,"TCPLapp/search_location.html")    
 
 



def autocomplete(request):
    term = request.GET.get('term')
    if term is not None:
        products = PuneAdminWards.objects.filter(name__istartswith=term).values_list('name','wardnum')
        print(products,"pratibhaaaaaaaaaaaaaaaaaaaaaaaaa")
        products_list1 = list(set(products))
        print(products_list1,"ppppppppppppppppppppppppppppppppppppppppppppppppppppppppp")
        products_list = [','.join(t) for t in products_list1]
        print(products_list,"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
    return JsonResponse(products_list, safe=False)



def convert_To_Geojson(products1):
    coordinates_list = []
    for instance in  products1:
        
        print(coordinates_list,'1111111111111')
        geom_geojson = GEOSGeometry(json.dumps({"type": "MultiPolygon", "coordinates": [instance.geom.coords[0]]}))
        print(geom_geojson,'2222222222222')
        feature = {
        "type": "Feature",
        "geometry": json.loads(geom_geojson.geojson),
        "properties": {
            "name": instance.name,
            "wardnum": instance.wardnum,
                        } }
        coordinates_list.append(feature)

        geojson_data = {
                    "type": "FeatureCollection",
                    "features": coordinates_list
                            }
    print(geojson_data,"hhhhhhhhhhhhhhhhhhhh")
    return geojson_data
    

def searchOnClick(request):
    response = request.GET.get("selected_value").split(",")
    name, wardnum = response[0],response[1]
    products1 = PuneAdminWards.objects.filter(name=name,   wardnum= wardnum)
    print(products1,'33333333333333')
    geojson_gut = convert_To_Geojson(products1)
    print(products1,'33333333333333')
    
    # intersection_query = Q(geom__intersects=products1[0].geom)
    # for product in products1[1:]:
    #     intersection_query |= Q(geom__intersects=product.geom)
    # plu = DhankawdiRoad.objects.filter(intersection_query)
    # for Iplu in plu:
    #     intersection_area = Iplu.geom.intersection(products1[0].geom).area
    
   
    return JsonResponse(geojson_gut, safe=False)


# ////////////////////////////select by location/////////




def select_by_location(request):
    if request.method == 'GET':
        source_layer_name = request.GET.get("selected_value")
        target_layer_name = request.GET.get('targetLayer')
        select_type = request.GET.get('selectTypeValue')

        print("Selected Values:", source_layer_name, target_layer_name, select_type)

        # Encode the source_layer_name and target_layer_name to ensure proper URL formatting
        encoded_source_layer_name = quote(source_layer_name)
        encoded_target_layer_name = quote(target_layer_name)

        # Define WFS URLs for source and target layers with properly encoded names
        wfs_url_source = "https://portal.geopulsea.com/geoserver/PMC/wfs?request=GetFeature&typeName={}&outputFormat=application/json".format(encoded_source_layer_name)
        wfs_url_target = "https://portal.geopulsea.com/geoserver/PMC/wfs?request=GetFeature&typeName={}&outputFormat=application/json".format(encoded_target_layer_name)

        gdf_source = gpd.read_file(wfs_url_source)
        gdf_target = gpd.read_file(wfs_url_target)

        # print("Columns of source layer:", gdf_source.columns)

        query_condition = 'Admin Ward 14 Dhankawadi'

        result = gdf_source[gdf_source['name'] == query_condition]

        selected_data = gpd.sjoin(gdf_target, result, how='inner', op='intersects')

        selected_data_geojson = selected_data.to_json()
        # print(selected_data_geojson)

        return JsonResponse(selected_data_geojson, safe=False)
    else:
        return JsonResponse({'error': 'Invalid request method'})


   


# //////////////////trial////////////////////////


def trial(request):
    
    return render(request, 'TCPLapp/trial.html')


def ward(request):
    
    return render(request, 'TCPLapp/ward.html')

def ward2(request):
    return render(request, 'TCPLapp/ward2.html')



def ward3(request):
    
    return render(request, 'TCPLapp/ward3.html')

# WARD_VIEWS

# @login_required(login_url="login")
# def ward_table(request):
# ############### for PMC_Missing_Link_Buffer ###########
    # url1 = "http://localhost:8080/geoserver/zone/wfs"
    # params = {
    #     "service": "WFS",
    #     "version": "2.0.0",
    #     "request": "GetFeature",
    #     "typeName": "zone:PMC_Missing_Links",
    #     "outputFormat": "application/json"
    # }

#     response = requests.get(url1, params=params)

#     if response.status_code == 200:
#         data1 = response.json()['features'][:10]  # Get the first 10 features
#         # print(data1)
#         PMC_Missing_Links = [feature['properties'] for feature in data1]
        
        
# ############### for PMC_Missing_Links ###########
    # url2 = "http://localhost:8080/geoserver/zone/wfs"
    # params = {
    #     "service": "WFS",
    #     "version": "2.0.0",
    #     "request": "GetFeature",
    #     "typeName": "zone:missinglink",
    #     "outputFormat": "application/json"
    # }

#     response2 = requests.get(url2, params=params)

#     if response2.status_code == 200:
#         data2 = response2.json()['features'][:10]  # Get the first 10 features
#         # print(data2)
#         missinglink = [feature['properties'] for feature in data2]
        
# ################### PMCroads  ################################
    # url3 = "http://localhost:8080/geoserver/zone/wfs"
    # params = {
    #     "service": "WFS",
    #     "version": "2.0.0",
    #     "request": "GetFeature",
    #     "typeName": "zone:PMCroads",
    #     "outputFormat": "application/json"
    # }

#     response3 = requests.get(url3, params=params)

#     if response3.status_code == 200:
#         data3 = response3.json()['features'][:10]  # Get the first 10 features
#         # print(data3)
#         PMCroads = [feature['properties'] for feature in data3]
        
        
# ################### DP_Roads  ################################
    # url4 = "http://localhost:8080/geoserver/zone/wfs"
    # params = {
    #     "service": "WFS",
    #     "version": "2.0.0",
    #     "request": "GetFeature",
    #     "typeName": "zone:DP_Roads",
    #     "outputFormat": "application/json"
    # }

#     response4 = requests.get(url4, params=params)

#     if response4.status_code == 200:
#         data4 = response4.json()['features'][:10]  # Get the first 10 features
#         # print(data4)
#         DP_Roads = [feature['properties'] for feature in data4]
# ###################################################
#         return render(request, 'TCPLapp/ward.html', {'properties': PMC_Missing_Links,"missinglink":missinglink,"PMCroads":PMCroads,"DP_Roads":DP_Roads})
#     # return render(request, 'TCPLapp/ward.html')


from django.shortcuts import render
import requests

from django.shortcuts import render
import requests

def display_layers(request):
    # GeoServer parameters
    geoserver_url = 'http://localhost:8080/geoserver/'
    username = 'admin'
    password = 'geoserver'
    workspace_name = 'zone'

    # Get layers URL for the specified workspace
    layers_url = f"{geoserver_url}workspaces/{workspace_name}/layers.json"

    try:
        # Use 'with' statement to automatically close the response
        with requests.get(layers_url, auth=(username, password)) as response:
            response.raise_for_status()  # Raise an error for bad responses

            layers_data = response.json().get('layers', {}).get('layer', [])

            if layers_data:
                layer_names = [layer['name'] for layer in layers_data]
                return render(
                    request,
                    'display_layers.html',
                    {'geoserver_url': geoserver_url, 'workspace_name': workspace_name, 'layer_names': layer_names}
                )
            else:
                return render(request, 'display_layers.html', {'error_message': 'No layers found.'})

    except requests.exceptions.RequestException as e:
        return render(request, 'display_layers.html', {'error_message': f"Failed to fetch layers. Error: {e}"})

# ////////////////////////////////////////////////////

def save_search_data(request):
    if request.method == 'POST':
        data = request.POST.get('query')
        username = request.user.username

        # Save search data to the database
        SearchHistory.objects.create(user=request.user, query=data, timestamp=timezone.now())

        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

def search_history(request):
    return render(request, 'search_history/search_history.html')