from tokenize import Token
from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from .serializers import HelloWorldSerializer, SubscriberSerializer
from . models import Subscriber
from rest_framework.generics import ListAPIView,CreateAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView

from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token




# APIView 
class HelloWorldView(APIView):
    def get(self,request):
        return Response({'message':"hello world hai"}) #JsonResponse because we want to render our response as JSON.

    def post(self,request):
        serializer = HelloWorldSerializer(data =request.data)
        if serializer.is_valid():
            valid_data = serializer.data
            name = valid_data.get('name')
            age = valid_data.get('age')
            return Response({'message':'Hello ,{}.You are {}'.format(name,age)})
           
        else:
            return Response({"error":serializer.errors})


# FBV APIView -use a function based form of APIView
@api_view(['GET','POST'])
def HelloFBVAPIView(request):
    if request.method == 'GET':
        return Response({'message':'function based apiview '})
    else:
        name =request.data.get("name")
        if not name:
            return Response({'error':'no name passed'})        
        return Response({'message':"hello, {}:".format(name)})


# subscriberview:
# class SubscriberView(APIView):
#     def get(self,request):
#         all_subscribers = Subscriber.objects.all()
#         serialized_subscibers = SubscriberSerializer(all_subscribers,many=True)
#         return Response(serialized_subscibers.data)

#     def post(self,request):
#         serializer = SubscriberSerializer(data= request.data)
#         if serializer.is_valid():
#             subscriber_instance = Subscriber.objects.create(**serializer.data)
#             return Response({"message":"created subscriber {}".format({subscriber_instance.id})})
#         return Response({"errors":serializer.errors})

# # ListAPIView and CreateAPIView

# class SubscriberView(ListAPIView,CreateAPIView):
#     serializer_class = SubscriberSerializer
#     queryset = Subscriber.objects.all()

class SubscriberView(ListCreateAPIView):
    serializer_class = SubscriberSerializer
    queryset = Subscriber.objects.all()

class SubscriberRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = SubscriberSerializer
    queryset = Subscriber.objects.all()
    lookup_field= 'id'


# Viewsets and modelviewsets

class SubscriberViewSet(ModelViewSet):
    serializer_class = SubscriberSerializer
    queryset = Subscriber.objects.all()


# login
@api_view(["POST"])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user  = authenticate(username=username,password = password)
    if not user:
        return Response({"error":"Login failed."})

    token,_ = Token.objects.get_or_create(user = user)
    return Response({"token":token.key})

