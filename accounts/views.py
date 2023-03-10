from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from django.db.utils import DatabaseError
from django.contrib.auth.mixins import UserPassesTestMixin


# Create your views here.
class SignupView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self,request,format=None):
        data = self.request.data
        name = data['name']
        email = data['email']
        password = data['password']
        password2 = data['password2']

        try:

            if password == password2:
                if User.objects.filter(email=email).exists():
                    return Response({'Error':"User with Email Already Exist"})
                else:
                    if len(password) < 6 :
                        return Response({'Error':"Password Length should be greater than 6"})
                    else:
                        user = User.objects.create_user(email=email,name=name,password=password)
                        user.save()
                        return Response({'Success':"User Created SuccessFully"})
            else:
                return Response({'Error':"Passwords do not match"})
        except DatabaseError as ex:
            return Response({'Error':"User with Email Already Exist"})


class MakeAdmin(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self,request,*args,**kwargs):
        data = self.request.data
        email = data['email']
        try:
            if self.request.user.is_superuser:
                user = User.objects.get(email=email)
                user.is_superuser = True
                user.is_staff = True
                user.save()
                return Response({'SUCCESS','User was made as Admin'})
            else:
                return Response({'FORBIDDEN','You Have to be an  Admin'})
        except Exception as e:
            print(e)
            return Response({"ERROR","User with Email Doesn't Exists"})
