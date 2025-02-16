# PDF to Markdown Using Azure AI Document Intelligence

Automate the conversion of a PDF document into Markdown format using Azure AI Document Intelligence. This project demonstrates how to analyze a PDF using Azure services, and output Markdown content to a file.

## Prerequisites

Before getting started, ensure you have:

- An [Azure AI Document Intelligence](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/how-to-guides/create-document-intelligence-resource) resource provisioned in your Azure subscription.
- The API [endpoint and key](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/how-to-guides/create-document-intelligence-resource?view=doc-intel-4.0.0#get-endpoint-url-and-keys) for your Azure AI Document Intelligence resource.
- A PDF file to convert. Rename the file to `document.pdf` and place it in the project folder (alongside [`handler.py`](handler.py)).

## Setup Instructions

1. **Clone the repository:**

   ```sh
   git clone https://github.com/tayganr/pdf2markdown.git
   cd pdf2markdown
   ```

2. **Create and activate a Python virtual environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows use: venv\Scripts\activate
    ```

3. **Install the required Python packages:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Configure your environment variables:** Create a .env file in the project root with the following contents (replace with your actual values):

    ```sh
    AZURE_ENDPOINT=https://<your-resource>.cognitiveservices.azure.com/
    AZURE_API_KEY=<your-api-key>
    ```

5. **Add your PDF file:** Ensure your PDF file is named document.pdf and is located in the same folder as handler.py.

## Running the Code

Execute the Python script to convert your PDF to Markdown:

```sh
python handler.py
```

The script will:

- Read document.pdf.
- Convert its contents to a Base64-encoded string.
- Send the document to Azure AI Document Intelligence for analysis.
- Save the resulting Markdown content to document.md.


After execution, you should see a confirmation message in the terminal:

```sh
Markdown content saved to document.md
```

## Additional Information

- **Source Code:** The main conversion logic is located in handler.py.
- **Documentation:** For more details on the Azure AI Document Intelligence API, visit Microsoft's [documentation](https://learn.microsoft.com/en-us/python/api/overview/azure/ai-documentintelligence-readme).