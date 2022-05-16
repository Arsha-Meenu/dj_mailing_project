from rest_framework import serializers

from .models import Subscriber


class HelloWorldSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 6,required = True)
    age = serializers.IntegerField(required =False,min_value = 10,default= 10)
    

# Serializer class  
# class SubscriberSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length = 6,required = True)
#     age = serializers.IntegerField()
#     email = serializers.EmailField()
   
 #ModelSerializer class  
class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = "__all__"