# 📧 Find Work Emails


## 🔥 Overview
Find-Work-Emails is a simple Python script designed to validate email addresses using SMTP protocol and DNS lookups. It reads from a CSV file containing names and domains, generates possible email format guesses based on common patterns, and checks each one for validity by performing an SMTP check.

## ⚙️ Features
- **MX Record Caching**: Reduces redundant DNS lookups by caching MX records.
- **Multi-threading**: Utilizes Python's concurrent.futures for faster processing.
- **Command-Line Interface**: Easy to use with arguments for file path, name column, and domain column.
- **Progress Tracking**: Includes a progress bar for real-time feedback.

## 😄 Prerequisites
Before running this script, ensure that you have the following prerequisites installed:
- Python 3.6 or higher
- pandas
- dnspython

## 💻 Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/email-verifier.git
    ```
2. Navigate to the cloned directory:
    ```bash
    cd email-verifier
    ```
3. Install the required packages:
    ```bash
    pip install pandas dnspython tqdm
    ```

## 🎆 Usage
To use the Email Verifier, you'll need a CSV file with columns for full names and company domains. Then, run the script with the following command:

```bash
python email_verifier.py --file "path/to/your/csvfile.csv" --namecol "Column Name for Full Names" --domaincol "Column Name for Company Domain"
