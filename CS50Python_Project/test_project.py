import pytest
from unittest.mock import patch, MagicMock
import pandas as pd
from project import load_df, query_data_and_send_emails, send_email
import os

URL = "https://docs.google.com/spreadsheets/d/1Ca4MtFVamSX36fbONuR5OLF7XEJYqiiOzoxEoBTPp8Y/gviz/tq?tqx=out:csv&sheet=Sheet1"

@pytest.fixture
def mock_df():
    return pd.DataFrame({
        "task_id": [123, 234],
        "email": ["test1@example.com", "test2@example.com"],
        "name": ["John Doe", "Jane Doe"],
        "due_date": pd.to_datetime(["2024-07-03", "2024-07-02"]),
        "reminder_date": pd.to_datetime(["2024-07-01", "2024-07-01"]),
        "task_status": ["not yet done", "done"],
        "project_title": ["python1", "python2"]
    })

@patch("pandas.read_csv")
def test_load_df(mock_read_csv, mock_df):
    mock_read_csv.return_value = mock_df
    
    df = load_df(URL)
    mock_read_csv.assert_called_once_with(URL, parse_dates=["due_date", "reminder_date"])
    assert not df.empty
    assert list(df.columns) == ["task_id", "email", "name", "due_date", "reminder_date", "task_status", "project_title"]

@patch("project.send_email")
def test_query_data_and_send_emails(mock_send_email, mock_df):
    result = query_data_and_send_emails(mock_df)
    mock_send_email.assert_called_once_with(
        subject="Automated Task Reminder [Task ID no.: 123]",
        receiver_email="test1@example.com",
        name="John Doe",
        due_date="July 03, 2024",
        project_title="python1"
    )
    assert result == "Total Emails Sent: 1"

@patch("smtplib.SMTP_SSL")
@patch("email.message.EmailMessage", return_value=MagicMock())
def test_send_email(mock_email_msg, mock_smtp):
    send_email(
        subject="Test Subject",
        receiver_email="test@example.com",
        name="John Doe",
        due_date="Jun 30, 2024",
        project_title="python1"
    )
    mock_smtp.assert_called_once_with("smtp.gmail.com", 465)
    mock_smtp_instance = mock_smtp.return_value.__enter__.return_value
    mock_smtp_instance.login.assert_called_once_with(os.environ.get("user_email"), os.environ.get("user_pass_app"))
    mock_smtp_instance.sendmail.assert_called_once()