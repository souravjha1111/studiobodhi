from django.http import response
from .serializers import blogSerializer, urlSerializer, contactSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import blogMOdel, urlModel, contactModel
from rest_framework.decorators import api_view
from django.shortcuts import render
from django.views.decorators.cache import never_cache
from django.http import HttpResponse


@api_view(['GET', 'POST'])
@never_cache
def get_post_pic(request):
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


class deletephotourl(APIView):
    def delete(self,request, pk):
        urlModel.objects.get(pk =pk).delete()
        return HttpResponse('')

##################################################################################################################################

@api_view(['GET', 'POST'])
@never_cache
def blogdata(request):
    if request.method == 'GET':
        orders = blogMOdel.objects.all()
        serializer = blogSerializer(orders,many = True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer  = blogSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response(serializer.data)
        
        else:
            return Response(serializer.errors)


class deleteblogdata(APIView):
    def delete(self,request, pk):
        blogMOdel.objects.get(pk =pk).delete()
        return HttpResponse('')

####################################################################3
@api_view(['GET', 'POST'])
@never_cache
def contactsave(request):
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


class deletecontactsave(APIView):
    def delete(self,request, pk):
        contactModel.objects.get(pk =pk).delete()
        return HttpResponse('')



# # class photourl(APIView):
# #     def post(self, request):
# #         serializer = urlSerializer(data=request.data)
# #         serializer.is_valid(raise_exception=True)
# #         serializer.save()
# #         return Response(serializer.data)


# #     def get(self, request):
# #         product = urlModel.objects.all()
# #         serializer = urlSerializer(product, many =True)
# #         return Response(serializer.data)


# class blogdata(APIView):
#     def post(self, request):
#         serializer = blogSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)


#     def get(self, request):
#         product = blogMOdel.objects.all()
#         serializer = blogSerializer(product, many =True)
#         return Response(serializer.data)


# class contactsave(APIView):
#     def post(self, request):
#         serializer = contactSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)


#     def get(self, request):
#         product = contactModel.objects.all()
#         serializer = contactSerializer(product, many =True)
#         return Response(serializer.data)


# class delphotourl(APIView):
#     def delete(self, request, pk):
#         # id = request.id
#         snippet = urlModel.get_object(pk =pk)
#         snippet.delete()
#         return {}


# class delblogdata(APIView):
#     def delete(self, request):
#         id = request.id
#         blogMOdel.objects.get(pk =id).delete()
#         return {}


# class delcontactData(APIView):
#     def delete(self, request):
#         id = request.id
#         snippet = contactModel.objects.get(pk =id)
#         snippet.delete()
#         return {}



# class blogdatadetails(APIView):
#     def get(self, request):
#         id =  request.id
#         product = blogMOdel.objects.get(pk=id)
#         serializer = blogSerializer(product, many =True)
#         return Response(serializer.data)

# ############################################################################






# # class getserializerproducts(APIView):
# #     def get(self, request, pk):
# #         product = ProductModel.objects.all()
# #         product = product.filter(serializer = pk)
# #         serializer = SellerProductSerializer(product, many =True)

# #         return Response(serializer.data)




# # class blogdata(APIView):
# #     def post(self, request):
# #         serializer = blogSerializer(data=request.data)
# #         serializer.is_valid(raise_exception=True)
# #         serializer.save()
# #         return Response(serializer.data)
    


# # class contactData(APIView):
# #     def post(self, request):
# #         serializer = contactSerializer(data=request.data)
# #         serializer.is_valid(raise_exception=True)
# #         serializer.save()
# #         return Response(serializer.data)
    
