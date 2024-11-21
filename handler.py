import os  
from azure.ai.documentintelligence import DocumentIntelligenceClient  
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest, ContentFormat  
from azure.core.credentials import AzureKeyCredential  
import base64  
from dotenv import load_dotenv  
  
# Load environment variables from .env file  
load_dotenv()  
  
# Get the endpoint and API key from environment variables  
endpoint = os.getenv("AZURE_ENDPOINT")  
api_key = os.getenv("AZURE_API_KEY")  
  
# Create the client  
document_intelligence_client = DocumentIntelligenceClient(endpoint=endpoint, credential=AzureKeyCredential(api_key))  
  
# Load the PDF document from the local machine  
file_path = "document.pdf"  
with open(file_path, "rb") as pdf_file:  
    pdf_content = pdf_file.read()  
  
# Encode the PDF content to base64  
encoded_pdf_content = base64.b64encode(pdf_content).decode('utf-8')  
  
# Create the AnalyzeDocumentRequest with bytes_source  
analyze_request = AnalyzeDocumentRequest(bytes_source=encoded_pdf_content)  
  
# Analyze the document and extract content in Markdown format  
poller = document_intelligence_client.begin_analyze_document(  
    model_id="prebuilt-layout",  
    analyze_request=analyze_request,  
    output_content_format=ContentFormat.MARKDOWN  
)  
  
# Wait for the operation to complete and get the result  
result = poller.result()  
  
# Extract the markdown content from the result  
markdown_content = result.content  
  
# Construct the output .md file path  
output_file_path = os.path.splitext(file_path)[0] + ".md"  
  
# Write the markdown content to the .md file  
with open(output_file_path, "w", encoding="utf-8") as md_file:  
    md_file.write(markdown_content)  
  
print(f"Markdown content saved to {output_file_path}")  