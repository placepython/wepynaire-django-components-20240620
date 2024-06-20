from django_components import component


@component.register("modal")
class Modal(component.Component):
    template_name = "modals/modal.html"

    def get_context_data(
        self, modal_id, title, body, close_button_text="Close"
    ):
        return {
            "modal_id": modal_id,
            "title": title,
            "body": body,
            "close_button_text": close_button_text,
        }
