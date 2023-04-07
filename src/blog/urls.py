from django.urls import path
from .views import post_list, post_create, post_detail, post_update, post_delete, like

# app_name: to prevent confusion if there is same name in return redirects, 
#  since the urlpatterns path name can also be in another app:
app_name="blog"

urlpatterns = [
    path("", post_list, name="list"),
    path("create/", post_create, name="create"),
    path("<str:slug>", post_detail, name="detail"),
    path("<str:slug>/update/", post_update, name="update"),
    path("<str:slug>/delete/", post_delete, name="delete"),
    path("<str:slug>/like/", like, name="like"),
]