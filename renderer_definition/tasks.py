from celery import shared_task
from renderer_definition.models import Document, RenderedDocument


@shared_task(name='render_pdf', pydantic=True)
def render_pdf(document: Document, css: str) -> RenderedDocument:
    raise NotImplementedError()
