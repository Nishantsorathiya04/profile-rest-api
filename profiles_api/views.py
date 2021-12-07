from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):

    def get(self,request,format=None):
        an_apiview=[
        "User https method (get,post,put,delete,patch)",
        "is similar  to tradintional Django view",
        "most control of ur application logic",
        "is mapped manually to urls",
        ]

        return Response({"message":"hello!","an_apiview":an_apiview})
