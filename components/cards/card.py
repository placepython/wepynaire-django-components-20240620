from django_components import component


@component.register("card")
class Card(component.Component):
    template_name = "cards/card.html"
