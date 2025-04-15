from celery import shared_task, Task
from abc import ABC, abstractmethod
from renderer_definition.models import Document, RenderedDocument

class BaseRenderTask(Task):
    name = 'render_pdf'

    @abstractmethod
    def run(self, document: Document, css: str) -> RenderedDocument:
        raise NotImplementedError()


render_pdf_task = BaseRenderTask()
