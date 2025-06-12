from weasyprint import HTML

def create_pdf(html_content: str):
    return HTML(string=html_content).write_pdf()
