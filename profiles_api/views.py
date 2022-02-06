from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    # Test Api view

    def get(self,req,format=None):
        an_apiview = [
            'Aayush',
            'Shah',
            'SDE at Amazon',
        ]

        return Response({'message' : 'Hello', 'an_apiview':an_apiview})

     