from django import forms
from Gallery.models import *

class Add_Image_Form(forms.ModelForm):
    class Meta:
        model=Image
        exclude=('tags',)
        widgets={
            "title":forms.TextInput(attrs={"class":"form-control","id":"title","placeholder":"Enter Title","required":""}),
            #"tags":forms.TextInput(attrs={"class":"form-control","id":"tags","placeholder":"Enter Tags","required":""}),
            "image":forms.FileInput(attrs={"class":"form-control","id":"image","placeholder":"Upload File","required":""}),
            "description":forms.TextInput(attrs={"class":"form-control","id":"description","placeholder":"Enter Desc.","required":""})
        }