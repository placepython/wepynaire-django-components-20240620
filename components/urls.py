from django.urls import include, path

app_name = "components"

urlpatterns = [
    path("search-table/", include("components.search_table.urls")),
]
