from django.shortcuts import render
from django_components import component

from example.models import WePynaire


@component.register("search-table")
class SearchTable(component.Component):
    template_name = "search_table/search_table.html"

    def get_context_data(self, title_level="h3"):
        self.wepynaires = WePynaire.objects.order_by("start_datetime")
        return {
            "wepynaires": self.wepynaires,
            "title_level": title_level,
        }

    def get(self, request):
        # Répond à la requête HTMX pour le tri
        search = request.GET.get("search")
        print(search)
        wepynaires = WePynaire.objects.filter(
            title__icontains=search
        ).order_by("start_datetime")
        return render(
            request,
            "search_table/search_table.html#wepynaires",
            context={"wepynaires": wepynaires},
        )
