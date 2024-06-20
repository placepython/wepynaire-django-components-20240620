from django.urls import path

from .search_table import SearchTable

app_name = "search_table"

urlpatterns = [
    path("search", SearchTable.as_view(), name="search"),
]
