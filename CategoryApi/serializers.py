from rest_framework.serializers import ModelSerializer 
from .models import category

class categorySerializer(ModelSerializer):
    class Meta:
        model = category
        fields = '__all__' # this serialize all the fields in the model