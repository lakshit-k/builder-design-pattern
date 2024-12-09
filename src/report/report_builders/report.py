# src/report/report.py

class Report:
    def __init__(self):
        self.title = None
        self.document_type = None
        self.header = None
        self.body = None
        self.footer = None
        self.tables = []
        self.charts = []

    def __str__(self):
        return f"Report: {self.title}\nDocumentType: {self.document_type}\nHeader: {self.header}\nBody: {self.body}\nFooter: {self.footer}\nTables: {self.tables}\nCharts: {self.charts}"
