# src/director/report_director.py
from src.report.report_builders.abstract_report_builder import ReportBuilder

class ReportDirector:
    def __init__(self, builder:ReportBuilder):
        self.builder = builder

    def construct_report(self):
        self.builder.set_title("Annual Business Report")\
        .set_header("Business Overview 2024")\
        .set_body("This report covers the business performance for the year 2024.")\
        .set_footer("Confidential - For Internal Use Only")\
        .add_table("Table 1: Sales Data")\
        .add_table("Table 2: Revenue Data")\
        .add_chart("Chart 1: Sales Growth")
        return self.builder.get_report()
