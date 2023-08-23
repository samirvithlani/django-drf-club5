from django.shortcuts import render
from rest_framework import viewsets
from .models import Blog,Category
from .serializers import BlogSerializer,CategorySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView 
from rest_framework.mixins import CreateModelMixin,ListModelMixin,UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin
from .util.responseUtil import get_custom_response


# Create your views here.
class BlogApiVewSet(viewsets.ModelViewSet):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()  

class CategoryApiVewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    
class CreateBlog(GenericAPIView,CreateModelMixin):
    serializer_class = BlogSerializer
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class ListBlog(GenericAPIView,ListModelMixin):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()   
    
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
    def list(self, request, *args, **kwargs):
        queryset = Blog.objects.all().select_related('category')
        serializer = BlogSerializer(queryset, many=True)
        response_data = get_custom_response(serializer.data)
        return Response(response_data, status=status.HTTP_200_OK)
        
    
    

class UpdateBlog(GenericAPIView,UpdateModelMixin):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()   
    
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)    

class DeleteBlog(GenericAPIView,DestroyModelMixin):
    serializer_class = BlogSerializer
    #queryset = Blog.objects.all()   
    
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)    