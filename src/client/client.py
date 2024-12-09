# src/client/client.py

from src.report.report_factory import ReportBuilderFactory
from src.director.report_director import ReportDirector

# Create a PDF Report using the Factory
pdf_builder = ReportBuilderFactory.get_builder("pdf")
report_director = ReportDirector(pdf_builder)
pdf_report = report_director.construct_report()
print(pdf_report)

# Create an HTML Report using the Factory
html_builder = ReportBuilderFactory.get_builder("html")
report_director = ReportDirector(html_builder)
html_report = report_director.construct_report()
print(html_report)
