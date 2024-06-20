from django_components import component


@component.register("slide")
class Slide(component.Component):
    template = """
        <div class="slider-slide swiper-slide">
            {% slot "side-content" default %}{% endslot %}
        </div>
    """

    class Media:
        css = "slider/slide.css"
