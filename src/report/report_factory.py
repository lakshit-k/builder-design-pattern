# src/report/report_builder_factory.py

from .report_builders import *
from src.utility.constants import ReportBuilderEnum

class ReportBuilderFactory:
    report_mapper = {
        ReportBuilderEnum.HTML_REPORT_BUILDER.value:HTMLReportBuilder,
        ReportBuilderEnum.PDF_REPORT_BUILDER.value:PDFReportBuilder
    }


    @classmethod
    def get_builder(cls,report_type: str):
        if not cls.report_mapper.get(report_type):
            raise ValueError(f"Unknown report type: {report_type}")
        return cls.report_mapper[report_type]()