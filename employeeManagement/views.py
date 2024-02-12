from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UserSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from rest_framework.decorators import authentication_classes,permission_classes
from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from api.utils import get_url_patterns
 

@api_view(['POST'])
def login(request):
    user = get_object_or_404(User,username = request.data['username'])
    if not user.check_password(request.data['password']):
        return Response({'details':'NOt found'},status=status.HTTP_404_NOT_FOUND)
    token,created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)
    return Response({"token":token.key,"user":serializer.data})

@api_view(['POST'])
def logout(request):
    # Get the user's token from the request headers
    auth_token = request.META.get('HTTP_AUTHORIZATION').split(' ')[1]

    # Delete the token associated with the user
    try:
        token = Token.objects.get(key=auth_token)
        token.delete()
        return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)
    except Token.DoesNotExist:
        return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def signup(request):
    serializer =UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({"token":token.key,"user":serializer.data})
    return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)




@api_view(['GET'])
def getRoutes(request):

    routes = [
        {'POST' : '/signup/'},
        {'POST' : '/login/'},
        {'POST' : '/logout/'},
        # api end points for crud on employee database
        {'GET' : '/api/employees/'},
        {'GET' : '/api/employees/<int:pk>/'},
        {'POST' : '/api/employees/create/'},
        {'PUT' : '/api/employees/<int:pk>/update/'},
        {'DELETE' : '/api/employees/<int:pk>/delete/'},
    ]
    return Response(routes)
