CodeStringExporter takes a folder of projects and exports minified code files in parts for upload to OmniAi agents.


How it works

1 - Clone repos you wish to document to a /projects folder in project root.
2 - Check and adjust vars to crawl the files in a manner that suits your projects:
    - ALLOWED_EXTENSIONS
    - ALLOWED_BASE_FILES
    - EXCLUDED_DIRECTORIES
    - MAX_FILE_SIZE

3 - Run python script
4 - Create OmniAi Agent and use the files in /output as attachments on the agent. Provide a detailed description to the agent on how it should behave for your needs, explanation, documentation etc.