from django.urls import path

from .views import (
    PostCreateApi,
    PostUpdateApi,
    PostDeleteApi,
    PostListApi,
    ActiveLinkView,
    RecentLinkView,
)

app_name = "link"

urlpatterns = [
    path("create/", PostCreateApi.as_view(), name="api_create"),
    path("update/<int:pk>", PostUpdateApi.as_view(), name="api_update"),
    path("delete/<int:pk>", PostDeleteApi.as_view(), name="api_delete"),
    path("", PostListApi.as_view(), name="api_list"),
    path("active/", ActiveLinkView.as_view(), name="active_link"),
    path("recent/", RecentLinkView.as_view(), name="recent_link"),
]
