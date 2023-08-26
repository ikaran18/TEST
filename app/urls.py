from django.urls import path,include
from .views import * 

urlpatterns = [
    path("",Home.as_view(),name='home'),
    path("blogdetail/<int:pk>",BlogDetailView.as_view(),name='blogdetail'),
    path("addblog/",AddBlog.as_view(),name='addblog'),
    path("editblog/<int:pk>",EditBlog.as_view(),name='edit'),
    path("deleteblog/<int:pk>",DeleteBlog.as_view(),name='delete'),
    # path("blogdetail/<int:pk>/comment",AddComment.as_view(),name='addcomment'),
    path('comment/create/<int:pk>', CommentCreateView.as_view(), name='addcomment'),

   
]