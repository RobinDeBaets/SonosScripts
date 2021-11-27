import subprocess

TERMINAL_NOTIFIER_PATH = "/opt/homebrew/bin/terminal-notifier"

def send_notification(summary, message="", icon="", urgency="normal", timeout=None, app_name="", notification_id=1234):
    subprocess.call([TERMINAL_NOTIFIER_PATH, "-title", summary, "-message", message, "-group", str(notification_id), "-ignoreDnD"])