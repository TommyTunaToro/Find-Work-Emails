import pandas as pd
import smtplib
import dns.resolver
from tqdm import tqdm
import time
import argparse
import concurrent.futures


# Caching MX records to avoid redundant DNS lookups
mx_cache = {}

def smtp_check(email):
    domain = email.split('@')[1]
    if domain in mx_cache:
        mx_record = mx_cache[domain]
    else:
        try:
            mx_records = dns.resolver.resolve(domain, 'MX')
            mx_record = str(mx_records[0].exchange)
            mx_cache[domain] = mx_record
        except Exception as e:
            return False
    
    try:
        server = smtplib.SMTP(timeout=10)
        server.set_debuglevel(0)
        server.connect(mx_record)
        server.helo(server.local_hostname)
        server.mail('you@example.com')
        code, message = server.rcpt(email)
        server.quit()
        return code == 250
    except Exception as e:
        return False

def generate_emails(row, name_col, domain_col):
    email_formats = []
    if ' ' in row[name_col]:
        first_name, last_name = row[name_col].split(' ', 1)
        domain = row[domain_col]
        first_name = ''.join(filter(str.isalpha, first_name)).lower()
        last_name = ''.join(filter(str.isalpha, last_name)).lower()
        
        guesses = [
            f"{first_name}.{last_name}@{domain}",
            f"{first_name[0]}{last_name}@{domain}",
            f"{first_name[0]}{last_name[0]}@{domain}",
            f"{first_name}@{domain}",
            f"{last_name}@{domain}",
        ]
        email_formats.extend(guesses)
    return email_formats

def process_emails(file_path, name_col, domain_col):
    df = pd.read_csv(file_path)

    progress_bar = tqdm(total=df.shape[0] * 5)  # assuming 5 guesses per row

    def process_row(row):
        email_list = generate_emails(row, name_col, domain_col)
        for email in email_list:
            result = smtp_check(email)
            if result:
                if 'email' not in df.columns:
                    df['email'] = ''
                df.at[row.name, 'email'] += email + ','  # Using row.name to access the index
            progress_bar.update(1)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(process_row, [row for _, row in df.iterrows()])

    progress_bar.close()
    df.to_csv('updated_with_emails_sync.csv', index=False)

# Main execution
if __name__ == "__main__":
    # Initialize the argument parser
    parser = argparse.ArgumentParser(description='Email Verifier Script')
    parser.add_argument('--file', help='Path to the CSV file', required=True)
    parser.add_argument('--namecol', help='Column name for full names', required=True)
    parser.add_argument('--domaincol', help='Column name for company domain', required=True)

    # Parse the arguments
    args = parser.parse_args()

    # Assigning args values to variables
    file_path = args.file
    name_col = args.namecol
    domain_col = args.domaincol

    # Timing the script execution
    start_time = time.time()
    process_emails(file_path, name_col, domain_col)
    end_time = time.time()

    # Print out execution time
    print(f"Execution time: {end_time - start_time} seconds")
