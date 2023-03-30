# Schedule Email Script (Inbox-Hero)

This is a Python script that allows you to schedule an email to be sent at a specific time.

## Installation

To install the script, you can follow these steps:

1. Clone the repository: `git clone https://github.com/yourusername/schedule-email-script.git`
2. Install the required libraries: `pip install -r requirements.txt`

## Usage

To use the script, you need to do the following:

1. Open `config.py` and enter your email account credentials.
2. Replace the placeholder code in the `send_email` function with the actual code to send an email.
3. In the `schedule_email` function, modify the time value in `schedule.every().day.at("9:00").do(send_email)` to the desired time you want the email to be sent.
4. Run the script: `python schedule_email.py`

The script will run indefinitely, checking for any scheduled tasks and running them at the appropriate time. When it's time for the email to be sent, the `send_email` function will be called and the email will be sent.

## Contributing

Contributions to the script are welcome. If you want to make any major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
