import os
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from datetime import date
import pandas as pd

SHEET_ID = "1Ca4MtFVamSX36fbONuR5OLF7XEJYqiiOzoxEoBTPp8Y"
SHEET_NAME = "Sheet1"
URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"
EMAIL_ADDRESS = os.environ.get("user_email")
EMAIL_PASSWORD = os.environ.get("user_pass_app")

def main():
    df = load_df(URL)
    if not df.empty:
        result = query_data_and_send_emails(df)
        print(result)
    else:
        print("No data to process.")

def load_df(url):
    parse_dates = ["due_date", "reminder_date"]
    try:
        df = pd.read_csv(url, parse_dates=parse_dates)
    except Exception as e:
        print(f"Error reading CSV: {e}")
        df = pd.DataFrame()
    return df

def query_data_and_send_emails(df):
    present = date.today()
    email_counter = 0
    for _, row in df.iterrows():
        if (present >= row["reminder_date"].date()) and (row["task_status"] == "not yet done"):
            send_email(
                subject=f"Automated Task Reminder [Task ID no.: {row['task_id']}]",
                receiver_email=row["email"],
                name=row["name"],
                due_date=row["due_date"].strftime("%B %d, %Y"),
                project_title=row["project_title"],
            )
            email_counter += 1
    return f"Total Emails Sent: {email_counter}"

def send_email(subject, receiver_email, name, due_date, project_title):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = formataddr(("CS50 Project", EMAIL_ADDRESS))
    msg["To"] = receiver_email
    msg["BCC"] = EMAIL_ADDRESS

    msg.add_alternative(
        f"""\
    <html>
        <body>
            <p>Dear {name},</p>
            <p>This is a friendly reminder to complete the following task:</p>
            <p>
                <strong style="color: blue;">Task:</strong> {project_title}<br>
                <strong style="color: blue;">Due Date:</strong> {due_date}
            </p>
            <p>Please do not reply to this email as it is automatically generated. If you have any questions or need assistance, please contact CS50 Project Manager.</p>
            <p>Thank you for your attention to this matter.</p>
        </body>
    </html>
    """,
        subtype="html"
    )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.sendmail(EMAIL_ADDRESS, receiver_email, msg.as_string())


if __name__=="__main__":
    main()

    