from django.urls import path
from .views import post_list, post_create

# app_name: to prevent confusion if there is same name in return redirects, 
#  since the urlpatterns path name can also be in another app:
app_name="blog"

urlpatterns = [
    path("", post_list, name="list"),
    path("create/", post_create, name="create")
]