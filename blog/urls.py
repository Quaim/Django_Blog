from . import views
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    # path('admin/', admin.site.urls),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    
]