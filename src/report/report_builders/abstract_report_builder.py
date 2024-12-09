# src/report/report_builder.py

from abc import ABC, abstractmethod
from .report import Report

class ReportBuilder(ABC):
    @abstractmethod
    def set_title(self, title: str):
        pass

    @abstractmethod
    def set_header(self, header: str):
        pass

    @abstractmethod
    def set_body(self, body: str):
        pass

    @abstractmethod
    def set_footer(self, footer: str):
        pass

    @abstractmethod
    def add_table(self, table: str):
        pass

    @abstractmethod
    def add_chart(self, chart: str):
        pass

    @abstractmethod
    def get_report(self):
        pass
