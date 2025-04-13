from celery import shared_task
from renderer_definition.models import Document


@shared_task(name='render_pdf')
def render_pdf(document: Document, css: str):
    raise NotImplementedError()
