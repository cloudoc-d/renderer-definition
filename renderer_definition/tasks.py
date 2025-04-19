from celery import shared_task, Task
from abc import ABC, abstractmethod

class BaseRenderTask(Task):
    name = 'render_pdf'

    @abstractmethod
    def run(self, document: dict) -> dict:
        """
        :param document: Structure corresponds to models.Document
        :return: Structure corresponds to models.RenderedDocument
        """
        raise NotImplementedError()


render_pdf_task = BaseRenderTask()
