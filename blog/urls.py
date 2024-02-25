
from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    # path('admin/', admin.site.urls),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),     
    
]