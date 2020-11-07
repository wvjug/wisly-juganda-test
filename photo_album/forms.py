from django.forms import ModelForm

from cloudinary.forms import CloudinaryJsFileField, CloudinaryUnsignedJsFileField, CloudinaryFileField
# Next two lines are only used for generating the upload preset sample name
from cloudinary.compat import to_bytes
import cloudinary, hashlib

from .models import Photo

class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'
    # Modify the sample project’s image upload form to: 
    image = CloudinaryFileField(options = { 
        'crop': 'limit', 'width': 500, 'height': 500, # a. Automatically limit image size to 500x500 pixels on upload 
        'tags': "directly_uploaded" # b. Tag uploaded images (doesn’t matter which tag)
        })


class PhotoDirectForm(PhotoForm):
    image = CloudinaryJsFileField()

class PhotoUnsignedDirectForm(PhotoForm):
    upload_preset_name = "sample_" + hashlib.sha1(to_bytes(cloudinary.config().api_key + cloudinary.config().api_secret)).hexdigest()[0:10]
    image = CloudinaryUnsignedJsFileField(upload_preset_name)
