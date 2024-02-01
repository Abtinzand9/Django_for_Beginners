from django.urls import path
from . import views

urlpatterns = [
    path("",views.BlogListView.as_view(),name='home'),
    path("post/<int:pk>",views.BlogDeatailView.as_view(),name="post_detail"),
    path("post/create",views.BlogCreateView.as_view(),name='new')
]
