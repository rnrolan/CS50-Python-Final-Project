# Automated Task Email Reminder
#### Video Demo: https://youtu.be/eFQmpuGHYTM

## Project Overview

This project focuses on developing an automated task reminder system using Python. The objective is to streamline task management by sending email reminders based on data retrieved from Google Sheets document. This system aims to ensure tasks are completed on time, thereby enhancing organization and efficiency. It employs pandas for data processing and smtplib for email functionality, showcasing the practical use of Python in automation.

## Files Description

### `project.py`

This is the core script of the project, coordinating the task reminder operations. Key functions include:

- **`main()`**: Acts as the script's main entry point, responsible for loading task data from Google Sheets and initiating the reminder process if data is available.
- **`load_df(url)`**: Loads task data from a specified Google Sheets URL into a pandas DataFrame and manages any errors during the process.
- **`query_data_and_send_emails(df)`**: Iterates through the DataFrame, checking if reminders need to be sent based on current dates and task statuses, and then sends the emails. It also tracks the number of emails sent.
- **`send_email(subject, receiver_email, name, due_date, project_title)`**: Creates and sends an email using smtplib, with the content formatted in HTML for better readability.

### `requirements.txt`

This file lists the Python libraries and dependencies needed for the project, enabling users to install the necessary packages using `pip install -r requirements.txt`.

## Design Choices

### Data Handling

Pandas was selected for data handling due to its robust and flexible capabilities. It simplifies loading data from CSV files, date parsing, and efficient data filtering and iteration.

### Email Sending

Smtplib was chosen for email sending due to its simplicity and reliability. As a part of Python's standard library, it requires no additional installations and provides essential functionalities for SMTP email sending.

### Google Sheets Integration

Integrating with Google Sheets provides a dynamic and accessible way to manage task data. Using a CSV export URL ensures that the latest data is always used without requiring direct interaction with the Google Sheets API, simplifying the implementation.

### Error Handling

The `load_df(url)` function includes error handling to manage potential issues during CSV file loading. This ensures that the program can handle cases where the data source might be unavailable or incorrectly formatted, enhancing the robustness of the solution.

## Future Enhancements

While the current implementation meets the basic requirements of an automated task reminder system, there are several areas for potential improvement:

- **Customizable Email Templates**: Adding support for customizable email templates would allow for more personalized and professional-looking reminders.
- **Integration with Other Task Management Tools**: Expanding the system to integrate with popular task management tools like Trello, Asana, or Jira could provide more versatility and user adoption.
- **User-Friendly Interface**: Developing a web-based or desktop GUI would make it easier for non-technical users to manage and configure the reminder system.
- **Enhanced Logging and Reporting**: Implementing more detailed logging and reporting features would help users track email sending status and history, providing better insights into the system's performance.

## Conclusion

This automated task reminder system demonstrates the practical application of Python for automating repetitive tasks, improving efficiency, and ensuring timely task completion. By leveraging pandas for data handling and smtplib for email sending, the project offers a robust and reliable solution for managing task reminders. The design choices made prioritize simplicity, reliability, and ease of use, making the system accessible and effective for various use cases.
