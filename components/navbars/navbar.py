from django_components import component


@component.register("navbar")
class Navbar(component.Component):
    template_name = "navbars/navbar.html"
