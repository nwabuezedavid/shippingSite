from dataclasses import field
import imp
from msilib.schema import Class
from rest_framework import serializers
from . models import *


class CustomerchattingApi(serializers.ModelSerializer):
    class Meta:
        model = chattingcustmer
        fields ='__all__'
class CustomerchattingApiGenerateId(serializers.ModelSerializer):
    class Meta:
        model = GenerateId
        fields ='__all__'
class CustomerchattingApimessagechat(serializers.ModelSerializer):
    class Meta:
        model = messagechat
        fields ='__all__'
