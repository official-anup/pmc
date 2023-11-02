from django import forms
#from .models import Customer2
from .models import Query, UploadedFile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm,PasswordResetForm,SetPasswordForm
from django.utils.translation import gettext,gettext_lazy as _ 
from django.contrib.auth import password_validation
from TCPLapp.models import Customer2

    # /////////////////////////////////////////////////////////////register/////////////////////////////////////////////
class CustomerRegiForm(UserCreationForm):
    password1=forms.CharField(label="",widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Password","style":"border-top:none; border-left:none; border-right:none; border-bottom:2px solid #bbb; background-color:#f8f9fa;"}))
    
    password2=forms.CharField(label="",widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Re-enter password","style":"border-top:none; border-left:none; border-right:none; border-bottom:2px solid #bbb; background-color:#f8f9fa;"}))
    
    email=forms.EmailField(label="",widget=forms.EmailInput(attrs={"class":"form-control","placeholder":"abc@gmail.com","style":"border-top:none; border-left:none; border-right:none; border-bottom:2px solid #bbb; background-color:#f8f9fa;"}))
    
    class Meta:
        model=User 
        fields=["username","email","password1","password2"]
        labels = {
            "username": "",}
        widgets={"username":forms.TextInput(attrs={"class":"form-control","placeholder":"username","style":"border-top:none; border-left:none; border-right:none; border-bottom:2px solid #bbb; background-color:#f8f9fa;"})}
        
        #///////////////////////////////////////////////QUERY-FORM//////////////////////////////////////////////////////////
class QueryForm(forms.ModelForm):
    class Meta:
        model=Query
        fields=["gutno","villagename","ownername","Buildingtype","comment","upload_file"] #
        
        widgets={"gutno":forms.TextInput(attrs={"class":"form-control", "placeholder": "Enter Gut Number","style":"border-top:none; border-left:none; border-right:none; border-bottom:2px solid #bbb; background-color:#f8f9fa;"}),
                 
        "villagename":forms.TextInput(attrs={"class":"form-control", "placeholder": "Enter Village Name","style":"border-top:none; border-left:none; border-right:none; border-bottom:2px solid #bbb; background-color:#f8f9fa;"}),

        "ownername":forms.TextInput(attrs={"class":"form-control", "placeholder": "Enter Owner Name","style":"border-top:none; border-left:none; border-right:none; border-bottom:2px solid #bbb; background-color:#f8f9fa;"}),
        
        "Buildingtype":forms.Select(attrs={"class":"form-control","placeholder": "Select Option","style":"border-top:none; border-left:none; border-right:none; border-bottom:2px solid #bbb; background-color:#f8f9fa;"}),
        
        
        "comment":forms.Textarea(attrs={"class":"form-control","placeholder": "Enter your comment","style":"overflow-y:scroll; height:50px;","style":"border-top:none; border-left:none; border-right:none; border-bottom:2px solid #bbb; background-color:#f8f9fa;"}),
        
        "upload_file":forms.FileInput(attrs={"class":"form-control","placeholder": "Upload your file here","style":"border-top:none; border-left:none; border-right:none; border-bottom:2px solid #bbb; background-color:#f8f9fa;"}),
        
        }

            #////////////////////////////////////////////////////LOGIN//////////////////////////////////////////////////////////
        
class LoginForm(AuthenticationForm):
        username=UsernameField(widget=forms.TextInput(attrs={'autofocus':True,"class":"form-control", "placeholder":"User Name", "style":"border-top:none; border-left:none; border-right:none; border-bottom:2px solid #bbb; background-color:#f8f9fa;"}), label="")
        
        password=forms.CharField(strip=False,widget=forms.PasswordInput(attrs={'autocomplete':True,"class":"form-control","placeholder":"Password","style":"border-top:none; border-left:none; border-right:none; border-bottom:2px solid #bbb; background-color:#f8f9fa;"}), label="")

            #///////////////////////////////////////CHANGE PASSWORD////////////////////////////////////////////////////////////////////////

class ChangePassword(PasswordChangeForm):
    old_password=forms.CharField(label=_("Old Password"),strip=False,widget=forms.PasswordInput(attrs={"autocomplete":"current-password","autofocus":True,"class":"form-control","style":"border-top:none; border-left:none; border-right:none; border-bottom:2px solid #bbb; background-color:#f8f9fa;"}))
    
    new_password1=forms.CharField(label=_("new Password"),strip=False,widget=forms.PasswordInput(attrs={"autocomplete":"new-password","class":"form-control","style":"border-top:none; border-left:none; border-right:none; border-bottom:2px solid #bbb; background-color:#f8f9fa;"}),help_text=password_validation.password_validators_help_text_html())
    
    new_password2=forms.CharField(label=_("Confirm new Password"),strip=False,widget=forms.PasswordInput(attrs={"autocomplete":"new-password","class":"form-control","style":"border-top:none; border-left:none; border-right:none; border-bottom:2px solid #bbb; background-color:#f8f9fa;"}))
    
class MyPasswordResetForm(PasswordResetForm):
    email=forms.EmailField(label=_(""),max_length=250,widget=forms.EmailInput(attrs={"autocomplete":"emial","placeholder":"Enter your Email address","class":"form-control","style":"border-top:none; border-left:none; border-right:none; border-bottom:2px solid #bbb; background-color:#f8f9fa;"}))

class MyPasswordResetConfirm(SetPasswordForm):
    new_password1=forms.CharField(label=_("New Password"),strip=False,widget=forms.PasswordInput(attrs={"autocomplete":"new-password","class":"form-control","style":"border-top:none; border-left:none; border-right:none; border-bottom:2px solid #bbb; background-color:#f8f9fa;"}),help_text=password_validation.password_validators_help_text_html())
    
    new_password2=forms.CharField(label=_("Confirm new Password"),strip=False,widget=forms.PasswordInput(attrs={"autocomplete":"new-password","class":"form-control","style":"border-top:none; border-left:none; border-right:none; border-bottom:2px solid #bbb; background-color:#f8f9fa;"}))        



class CustomerProfileForms(forms.ModelForm):
    class Meta:
        model=Customer2
        fields=["fullname","mobileno","dob","address","city","pin_code","occupation","industry"] #
        
        widgets={"fullname":forms.TextInput(attrs={"class":"form-control", "placeholder": "Enter Full Name","style":"border-top:none; border-left:none; border-right:none; border-bottom:2px solid #bbb; background-color:#f8f9fa;"}),
                 
        "mobileno":forms.TextInput(attrs={"class":"form-control", "placeholder": "Enter Mobile Number","style":"border-top:none; border-left:none; border-right:none; border-bottom:2px solid #bbb; background-color:#f8f9fa;"}),

        "dob" :forms.DateInput(attrs={"class":"form-control",'type': 'date',"style":"border-top:none; border-left:none; border-right:none; border-bottom:2px solid #bbb; background-color:#f8f9fa;"}),

        "address":forms.TextInput(attrs={"class":"form-control","placeholder": "Enter Your address","style":"border-top:none; border-left:none; border-right:none; border-bottom:2px solid #bbb; background-color:#f8f9fa;"}),
        
        "city":forms.TextInput(attrs={"class":"form-control","placeholder": "Enter Your address","style":"border-top:none; border-left:none; border-right:none; border-bottom:2px solid #bbb; background-color:#f8f9fa;"}),
        
        "pin_code":forms.TextInput(attrs={"class":"form-control","placeholder": "Enter Your address","style":"border-top:none; border-left:none; border-right:none; border-bottom:2px solid #bbb; background-color:#f8f9fa;"}),
        
        "occupation":forms.Select(attrs={"class":"form-control","placeholder": "Select Option","style":"border-top:none; border-left:none; border-right:none; border-bottom:2px solid #bbb; background-color:#f8f9fa;"}),
        
       
        "industry": forms.Select(attrs={"class": "form-control","style":"border-top:none; border-left:none; border-right:none; border-bottom:2px solid #bbb; background-color:#f8f9fa;"}),

        
        
        }


