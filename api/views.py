from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView



# clase Redirect
class RedirectViewSet(APIView):

    def post(self, request, pk="", bnc=""):

        # serializer = PagosSerializers(data=request.data)
        # if serializer.is_valid():
        #     # serializer.save()
        #     return Response(serializer.data)
        return Response(request.data)
