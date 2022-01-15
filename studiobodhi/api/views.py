from django.http import response
from .serializers import blogSerializer, urlSerializer, contactSerializer
from rest_framework.response import Response
from .models import blogMOdel, urlModel, contactModel
from rest_framework.decorators import api_view
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_exempt


@api_view(['GET', 'POST', 'DELETE'])
@csrf_exempt
def get_post_pic(request, pk):
    if request.method == 'GET':
        orders = urlModel.objects.all()
        serializer = urlSerializer(orders,many = True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer  = urlSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    elif request.method == 'DELETE':
        urlModel.objects.get(pk=pk).delete()
        return Response(status = 200)



@api_view(['GET', 'POST', 'DELETE'])
@csrf_exempt
def blogdata(request, pk):
    if request.method == 'GET':
        orders = blogMOdel.objects.values_list('id', 'title','blogphoto')
        serializer = blogSerializer(orders,many = True)
        return Response(orders)
    if request.method == 'POST':
        serializer  = blogSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    elif request.method == 'DELETE':
        blogMOdel.objects.get(pk=pk).delete()
        return Response(status = 200)



@api_view(['GET', 'POST', 'DELETE'])
@csrf_exempt
def data(request, pk):
    if request.method == 'GET':
        orders = blogMOdel.objects.get(pk = pk)
        serializer = blogSerializer(orders)
        return Response(serializer.data)



@api_view(['GET', 'POST', 'DELETE'])
@csrf_exempt
def contactsave(request, pk):
    if request.method == 'GET':
        orders = contactModel.objects.all()
        serializer = contactSerializer(orders,many = True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer  = contactSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    elif request.method == 'DELETE':
        contactModel.objects.get(pk=pk).delete()
        return Response(status = 200)
