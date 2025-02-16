import os
import base64
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest, DocumentContentFormat
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv

load_dotenv()

endpoint = os.getenv("AZURE_ENDPOINT")
api_key = os.getenv("AZURE_API_KEY")

document_intelligence_client = DocumentIntelligenceClient(endpoint=endpoint, credential=AzureKeyCredential(api_key))

file_path = "document.pdf"
with open(file_path, "rb") as pdf_file:
    pdf_content = pdf_file.read()

encoded_pdf_content = base64.b64encode(pdf_content).decode('utf-8')
analyze_request = AnalyzeDocumentRequest(bytes_source=encoded_pdf_content)

poller = document_intelligence_client.begin_analyze_document(
    model_id="prebuilt-layout",
    body=analyze_request,
    output_content_format=DocumentContentFormat.MARKDOWN
)

result = poller.result()
markdown_content = result.content
output_file_path = os.path.splitext(file_path)[0] + ".md"

with open(output_file_path, "w", encoding="utf-8") as md_file:
    md_file.write(markdown_content)

print(f"Markdown content saved to {output_file_path}")