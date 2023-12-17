from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, permissions

from .models import Product
from .serializer import ProductSerializer


def index(request):
    return HttpResponse(request)


class UpdateProduct(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = Product.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.name = request.data.get("name")
        instance.price = request.data.get("price")
        instance.category = request.data.get("category")
        instance.save()

        serializer = self.get_serializer(instance)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = Product.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        serializer = ProductSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


@api_view(['GET'])
def getData(request):
    if request.user.is_authenticated:
        app = Product.objects.all()
        serializer = ProductSerializer(app, many=True)
        return Response(serializer.data)
    return Response('authentication error')


@api_view(['POST'])
def postData(request):
    if request.user.is_authenticated:
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    return Response('error')
