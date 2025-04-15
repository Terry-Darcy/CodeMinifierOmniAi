# **CodeStringExporter**

`CodeStringExporter` is a tool that takes a folder of projects and **exports minified code files** in parts for upload to OmniAI agents.

---

## **How It Works**

Follow these steps to use `CodeStringExporter` effectively:

### **Step 1: Clone Repositories**
1. Clone the repositories you wish to document into the `/projects` folder located in the root of this project.
   - Example:
     ```
     /project-root
       ├── projects/
       │   ├── repo1/
       │   ├── repo2/
       │   └── ...
     ```

---

### **Step 2: Adjust Configuration for File Crawling**
Customize the configuration variables to suit your project's structure and requirements. These variables control which files and directories the script will process:

- **`ALLOWED_EXTENSIONS`**:  
  Specify the file extensions that should be included in the export (e.g., `.js`, `.py`, `.html`, etc.).  
  Example:
  ```python
  ALLOWED_EXTENSIONS = ['.py', '.js', '.html']
  ```

- **`ALLOWED_BASE_FILES`**:  
  Define specific base file names (e.g., `README.md`, `main.py`) that should always be included in the export.  
  Example:
  ```python
  ALLOWED_BASE_FILES = ['README.md', 'main.py']
  ```

- **`EXCLUDED_DIRECTORIES`**:  
  Provide a list of directories to exclude from the file crawl (e.g., `node_modules`, `.git`, etc.).  
  Example:
  ```python
  EXCLUDED_DIRECTORIES = ['node_modules', '.git', '__pycache__']
  ```

- **`MAX_FILE_SIZE`**:  
  Set the maximum allowed file size (in bytes) for processing files. Files larger than this size will be skipped.  
  Example:
  ```python
  MAX_FILE_SIZE = 200000  # 200KB
  ```

---

### **Step 3: Run the Script**
1. Run the Python script to process the repositories in the `/projects` folder:
   ```bash
   python your_script_name.py
   ```
2. The script will crawl the repositories, minify the code files, and export the processed files to the `/output` folder.

---

### **Step 4: Create and Configure OmniAI Agent**
1. Create an **OmniAI Agent**.
2. Upload the files generated in the `/output` folder as **attachments** to the agent.
3. Provide the agent with a detailed description of its intended behavior. Include:
   - Instructions on how the agent should use the attached files.
   - Any necessary explanations or documentation for the agent's functionality.

---

## **Example Folder Structure**

Before running the script, your project directory might look like this:

```
/project-root
  ├── projects/
  │   ├── repo1/
  │   │   ├── file1.py
  │   │   ├── file2.js
  │   │   └── ...
  │   ├── repo2/
  │   │   ├── index.html
  │   │   ├── app.js
  │   │   └── ...
  │   └── ...
  ├── output/
  ├── your_script_name.py
  └── ...
```

After running the script, the `/output` folder will contain the processed files, ready for upload.

---

## **Tips for Success**
- Ensure that the repositories in the `/projects` folder are cloned correctly.
- Adjust the configuration variables to avoid processing unnecessary files or directories.
- Provide detailed and precise instructions to the OmniAI agent to ensure it behaves as intended.

