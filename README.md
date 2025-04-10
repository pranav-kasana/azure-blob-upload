# Azure Blob Upload with Python

This simple Python project uploads a local file to an Azure Blob Storage container using the Azure SDK and environment variables for secure configuration.

---

## 📁 Folder Structure

Day1/ ├── upload_file.py # Main Python script to upload a file ├── sample.txt # Sample file to upload ├── .env # Contains your Azure Storage access key (ignored by Git) ├── .gitignore # Excludes .env from Git tracking

yaml
Copy
Edit

---

## ⚙️ Requirements

- Python 3.x
- Azure Storage Account and Blob Container (e.g., `saoneantra` and `test`)
- Python libraries:
  - `azure-storage-blob`
  - `python-dotenv`

---

## 📦 Install Dependencies

```bash
pip install azure-storage-blob python-dotenv
🔐 Setup .env File
Create a .env file in the project directory with this content:

env
Copy
Edit
ACCOUNT_KEY=your_actual_azure_key_here
✅ This file is ignored by Git via .gitignore to keep your secrets safe.

🚀 Run the Script
bash
Copy
Edit
python upload_file.py
Your sample.txt will be uploaded to the test container in your Azure Storage account.

✅ Best Practices
Never hard-code secrets like access keys in your scripts

Use .env files and .gitignore to separate code from config

Keep your GitHub repo clean and secure

📌 Author
Pranav Reddy
Project: Azure Blob Upload Script
GitHub: @pranav-kasana

yaml
Copy
Edit

---

## 📥 How to Use It

1. Create a new file in your folder:
   - Name: `README.md`
   - Paste the content above
2. Save it in your `Day1` folder
3. Then push it to GitHub with:

```bash
git add README.md
git commit -m "Added project README"
git push
