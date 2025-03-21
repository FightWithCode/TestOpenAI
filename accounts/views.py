from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User

class SignupView(APIView):

    """
    This APIs creates a new user in the database.
    Request:
        --first_name: str
        --last_name: str
        --username: str
        --email: str
        --password: str
        {
            "first_name": "Rahul",
            "last_name": "Sharma",
            "email": "email@g.co",
            "password": "123"
        }
    """

    # authentication_classes = 
    # permission_classes = 
    
    def post(self, request):
        print(request.data)
        return Response({})