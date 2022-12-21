from rest_framework import serializers

from .models import Orders, OrdersDetails, Items, ShippingData_address, ClientProfileData


class OrdersSerializers(serializers.ModelSerializer):

    class Meta:
        model = Orders
        fields = "__all__"


class ItemsSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Items
        fields = "__all__"


class ShippingData_addressSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = ShippingData_address
        fields = "__all__"


class ClientProfileDataSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = ClientProfileData
        fields = "__all__"


class OrdersDetailsSerializers(serializers.ModelSerializer):
    items= ItemsSerializers()
    clientProfileData= ClientProfileDataSerializers()
    shippingData= ShippingData_addressSerializers()

    class Meta:
        model = OrdersDetails
        # fields = "__all__"
        fields = ('orderId','sellerOrderId','origin','status','statusDescription','value','creationDate','orderGroup','items','clientProfileData','shippingData',)
        # exclude = ('items','clientProfileData','shippingData',)





