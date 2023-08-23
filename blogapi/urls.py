from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from .views import BlogApiVewSet,CategoryApiVewSet
from .views import CreateBlog,ListBlog

router = routers.DefaultRouter()
router.register('blog', BlogApiVewSet)
router.register('category', CategoryApiVewSet)

urlpatterns = [
    
    path('api/', include(router.urls)),
    path('create/', CreateBlog.as_view(), name='create'),
    path('list/', ListBlog.as_view(), name='list'), 
    path('update/<int:pk>/', BlogApiVewSet.as_view({'put': 'update'}), name='update'),
    path('delete/<int:pk>/', BlogApiVewSet.as_view({'delete': 'destroy'}), name='delete'),
]
