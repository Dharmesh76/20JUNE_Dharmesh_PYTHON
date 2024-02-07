from rest_framework import serializers
from .models import *

class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model=BookModel
        fields='__all__'
        