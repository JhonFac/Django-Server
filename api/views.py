from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Orders, OrdersDetails
from .serializers import OrdersSerializers, OrdersDetailsSerializers

# 
class OdersViewSet(APIView):

    # 
    def get(self, request):
        return Response(OrdersSerializers(Orders.objects.all(), many=True).data)


# 
class OderViewSet(APIView):

    # 
    def get(self, request, idOrder):
        return Response(OrdersSerializers(Orders.objects.filter(orderId=idOrder), many=True).data)


class OdersDetailsViewSet(APIView):

    # 
    def get(self, request):
        return Response(OrdersDetailsSerializers(OrdersDetails.objects.all(), many=True).data)


class OderDetailsViewSet(APIView):

    # 
    def get(self, request,idOrder):
        return Response(OrdersDetailsSerializers(OrdersDetails.objects.filter(orderId=idOrder), many=True).data)

