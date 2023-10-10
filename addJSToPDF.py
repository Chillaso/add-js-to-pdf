import PyPDF2

def add_javascript_to_pdf(input_pdf, output_pdf, js_code):
    with open(input_pdf, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        writer = PyPDF2.PdfWriter()
        
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            writer.add_page(page)
        
        writer.add_js(js_code)
        
        with open(output_pdf, "wb") as output_file:
            writer.write(output_file)
# Uso:
js_code = """
this.print({bUI: true, bSilent: false, bShrinkToFit: true});
"""

add_javascript_to_pdf("/home/chillaso/Downloads/proyecto.pdf", "test.pdf", js_code)

