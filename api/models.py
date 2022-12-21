from django.db import models


#
class ShippingData_address(models.Model):
    addressType=models.CharField(max_length=90)
    receiverName=models.CharField(max_length=90)
    addressId=models.CharField(max_length=90)
    postalCode=models.CharField(max_length=90)
    city=models.CharField(max_length=90)
    state=models.CharField(max_length=90)
    country=models.CharField(max_length=90)
    street=models.CharField(max_length=150)

    def __str__(self):
        return self.addressId


#
class Items(models.Model):

    uniqueId=models.CharField(max_length=90)
    itemsid=models.CharField(max_length=90)
    productId=models.CharField(max_length=90)
    name=models.CharField(max_length=90)
    refId=models.CharField(max_length=90)
    price=models.IntegerField()
    imageUrl=models.CharField(max_length=200)
    detailUrl=models.CharField(max_length=200)
    costPrice=models.IntegerField()

    def __str__(self):
        return self.uniqueId


#
class ClientProfileData(models.Model):

    email=models.CharField(max_length=90)
    firstName=models.CharField(max_length=90)
    lastName=models.CharField(max_length=90)
    documentType=models.CharField(max_length=90)
    document=models.CharField(max_length=90)
    phone=models.CharField(max_length=90)

    def __str__(self):
        return self.firstName


#
class Orders(models.Model):

    creationDate=models.CharField(max_length=90)
    orderId=models.CharField(max_length=90)
    totalValue=models.CharField(max_length=90)
    paymentNames=models.CharField(max_length=90)
    status=models.CharField(max_length=90)
    statusDescription=models.CharField(max_length=90)
    origin=models.CharField(max_length=90)
    totalItems=models.CharField(max_length=90)
    currencyCode=models.CharField(max_length=90)
    hostname=models.CharField(max_length=150)

    def __str__(self):
        return self.orderId

#
class OrdersDetails(models.Model):
    orderId=models.CharField(max_length=90)
    sellerOrderId=models.CharField(max_length=90)
    origin=models.CharField(max_length=90)
    status=models.CharField(max_length=90)
    statusDescription=models.CharField(max_length=90)
    value=models.CharField(max_length=90)
    creationDate=models.CharField(max_length=90)
    orderGroup=models.CharField(max_length=90)
    items=models.ForeignKey(Items, null=False, blank=True, on_delete=models.CASCADE, default=0)
    clientProfileData=models.ForeignKey(ClientProfileData, null=False, blank=True, on_delete=models.CASCADE, default=0)
    shippingData=models.ForeignKey(ShippingData_address, null=False, blank=True, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return self.orderId
