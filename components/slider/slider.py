from django_components import component


@component.register("slider")
class Slider(component.Component):
    template_name = "slider/slider.html"

    class Media:
        js = "slider/slider.js"
