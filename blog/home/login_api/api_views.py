from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from home.models import BlogModel, Profile, Comment


class LoginView(APIView):

    def post(self,  request):
        response = {}
        response['status'] = 500
        response['message'] = 'Something went worng'

        try:
            data = request.data

            if data.get('username') is None:
                response['message'] = 'key username not found'
                raise Exception('key username not found')

            if data.get('password') is None:
                response['message'] = 'key password not found'
                raise Exception('key password not found')

            check_user = User.objects.filter(
                username=data.get('username')).first

            if check_user is None:
                response['message'] = 'Invalid Username'
                raise Exception('Invalid Username')

            user_obj = authenticate(username=data.get(
                'username'), password=data.get('password'))

            if user_obj:
                login(request, user_obj)
                response['status'] = 200
                response['message'] = 'welcome'
            else:
                response['message'] = 'Invalid Username'
                raise Exception('Invalid Username')

        except Exception as e:
            print(e)

        return Response(response)


LoginView = LoginView.as_view()
