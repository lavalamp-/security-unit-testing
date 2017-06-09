"""sectesting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from streetart import views

urlpatterns = [

    # Admin

    url(r"^admin/", admin.site.urls),

    # Posts

    url(r"^$", views.PostListView.as_view(), name="post-list"),
    url(r"^my-posts/?$", views.MyPostsListView.as_view(), name="my-posts"),
    url(r"^new-post/?$", views.CreatePostView.as_view(), name="new-post"),
    url(r"^view-post/(?P<pk>[-\w]+)/?", views.PostDetailView.as_view(), name="view-post"),
    url(r"^edit-post/(?P<pk>[-\w]+)/?", views.EditPostView.as_view(), name="edit-post"),
    url(r"^delete-post/(?P<pk>[-\w]+)/?", views.DeletePostView.as_view(), name="delete-post"),
    url(r"^post-successful/(?P<pk>[-\w]+)/?", views.SuccessfulPostDetailView.as_view(), name="post-successful"),

    # Authentication

    url(r"^login/?$", auth_views.login, {"template_name": "pages/login.html"}, name="login"),
    url(r"^logout/?$", auth_views.logout, {"template_name": "pages/logout.html"}, name="logout"),
    url(r"^register/?$", views.CreateUserView.as_view(), name="register"),
    url(r"^register-success/?$", views.CreateUserSuccessView.as_view(), name="register-success"),

    # Error Handling

    url(r"^error-details/?$", views.ErrorDetailsView.as_view(), name="error-info"),

]
