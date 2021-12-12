from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions


class HelloApiView(APIView):

    serializer_class= serializers.HelloSerializer

    def get(self,request,format=None):
        an_apiview=[
        "User https method (get,post,put,delete,patch)",
        "is similar  to tradintional Django view",
        "most control of ur application logic",
        "is mapped manually to urls",
        ]

        return Response({"message":"hello!","an_apiview":an_apiview})

    def post(self,request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message= f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
             serializer.errors,
             status=status.HTTP_400_BAD_REQUEST
            )
    def put(self,request,pk=None):
        return Response ({'method':'put'})

    def patch(self,request,plk=None):
        return Response ({'method':'patch'})
    def delete(self,request,pk=None):
        return Response ({'method':'delete'})

class HelloViewSet(viewsets.ViewSet):
    """ Test API ViewSet """
    serializer_class = serializers.HelloSerializer

    def list(self,request):
        """ Hello word message"""
        a_viewset = [
        'Uses action (list,create,retrieve)',
        'automatic',
        'emj ala test mate',
        ]

        return Response ({'message':'Hello','a_viewset': a_viewset})

    def create(self, request):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status  = status.HTTP_400_BAD_REQUEST
            )
    def retrieve(self,request,pk=None):
        return Response({'http_method':'GET'})

    def update(self,request,pk=None):
        return Response({'http_method':'put'})

    def partial_update(self,reuest,pk=None):
        return Response({'http_method':'partial_update'})

    def destroy(self,request,pk=None):
        return Response({'http_method':'destroy'})


class UserProfileViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends =(filters.SearchFilter,)
    search_fields = ('name','email',)
    
