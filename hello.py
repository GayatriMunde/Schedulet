from api2pdf import Api2Pdf

a2p_client = Api2Pdf('5b0b86cb-c711-4868-9108-ef34071b9989')

api_response = a2p_client.LibreOffice.pdf_to_html('http://www.api2pdf.com/wp-content/uploads/2021/01/1a082b03-2bd6-4703-989d-0443a88e3b0f-4.pdf')

print(api_response.result)