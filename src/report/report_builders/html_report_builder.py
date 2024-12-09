# src/report/html_report_builder.py

from .abstract_report_builder import ReportBuilder
from .report import Report

class HTMLReportBuilder(ReportBuilder):
    def __init__(self):
        self.report = Report()
        self.report.document_type = "html"
        
    def set_title(self, title: str):
        self.report.title = title
        return self

    def set_header(self, header: str):
        self.report.header = header
        return self

    def set_body(self, body: str):
        self.report.body = body
        return self

    def set_footer(self, footer: str):
        self.report.footer = footer
        return self

    def add_table(self, table: str):
        self.report.tables.append(table)
        return self

    def add_chart(self, chart: str):
        self.report.charts.append(chart)
        return self

    def get_report(self):
        return self.report
