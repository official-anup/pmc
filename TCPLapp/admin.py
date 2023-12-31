from django.contrib import admin
from .models import DownloadFile, Payment, Query, UploadedFile,Customer2

@admin.register(Customer2)
class RegistrationAdmin(admin.ModelAdmin):  
    list_display = ["id","user", "dob","fullname", "mobileno","occupation","industry"]

    
@admin.register(UploadedFile)
class UploadedFileAdmin(admin.ModelAdmin):
    list_display = ["id","user_id1","files1"]

@admin.register(Query)
class QueryAdmin(admin.ModelAdmin):
    list_display = ["id","user","gutno","villagename","ownername","Buildingtype","comment","upload_file"]

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ["id","user","ammount"]

@admin.register(DownloadFile)
class DownloadFileAdmin(admin.ModelAdmin):
    list_display = ["id","user_id1","files1"]
    
  
    
 