import imaplib
import email
import os
import time
import schedule

# Function to authenticate account and connect to IMAP server
def connect_to_imap_server(username, password):
    # Connect to the IMAP server
    imap_server = imaplib.IMAP4_SSL("imap.gmail.com", 993)

    # Login to the account
    imap_server.login(username, password)

    # Select the mailbox (e.g. Inbox)
    imap_server.select("INBOX")

    return imap_server

# Function to archive an email
def archive_email(imap_server, email_id):
    imap_server.store(email_id, '+X-GM-LABELS', '\\Archive')
    imap_server.store(email_id, '+FLAGS', '\\Deleted')
    imap_server.expunge()

# Function to mark an email as read
def mark_email_as_read(imap_server, email_id):
    imap_server.store(email_id, '+FLAGS', '\\Seen')

# Function to delete an email
def delete_email(imap_server, email_id):
    imap_server.store(email_id, '+FLAGS', '\\Deleted')
    imap_server.expunge()

# Function to check if an email matches a set of rules
def check_email_rules(email_message):
    sender = email.utils.parseaddr(email_message['From'])[1]
    subject = email_message['Subject']
    content = email_message.get_payload()

    # Check if email matches a set of rules
    if sender == "example@example.com" and "important" in subject.lower():
        return True

    return False

# Function to process emails based on rules
def process_emails(imap_server):
    # Search for unread emails
    imap_server.select("INBOX")
    result, data = imap_server.search(None, "UNSEEN")

    # Loop through each email
    for email_id in data[0].split():
        # Fetch the email message
        result, email_data = imap_server.fetch(email_id, "(RFC822)")
        email_message = email.message_from_bytes(email_data[0][1])

        # Check if email matches a set of rules
        if check_email_rules(email_message):
            # Perform actions based on the email's content
            archive_email(imap_server, email_id)
        else:
            # Mark the email as read
            mark_email_as_read(imap_server, email_id)

# Function to schedule the email processing function
def schedule_email_processing(username, password):
    # Connect to the IMAP server
    imap_server = connect_to_imap_server(username, password)

    # Schedule the email processing function to run every hour
    schedule.every().hour.do(process_emails, imap_server)

    # Run the scheduled tasks indefinitely
    while True:
        schedule.run_pending()
        time.sleep(1)

# Call the schedule_email_processing function with your email account credentials
schedule_email_processing("your_email_address", "your_email_password")
