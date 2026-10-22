"""
Problem Statement:
Create a base class Report with a method generate().
Derive PDFReport, ExcelReport, and HTMLReport.
Override generate() in each class.
Write a function that accepts any report object and calls generate().
"""

class Report:
    def generate(self):
        print("Generating Report")


class PDFReport(Report):
    def generate(self):
        print("Generating PDF Report")


class ExcelReport(Report):
    def generate(self):
        print("Generating Excel Report")


class HTMLReport(Report):
    def generate(self):
        print("Generating HTML Report")


def create_report(report):
    report.generate()


create_report(PDFReport())
create_report(ExcelReport())
create_report(HTMLReport())