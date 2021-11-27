import notify2
from dbus import DBusException


def clean_up_text(text):
    return text.replace("\\n", "\n").replace("\\t", "\t")


urgencies = {
    "low": notify2.URGENCY_LOW,
    "normal": notify2.URGENCY_NORMAL,
    "critical": notify2.URGENCY_CRITICAL
}


# Based on https://github.com/phuhl/notify-send.py
def send_notification(summary, message="", icon="", urgency="normal", timeout=None, app_name="", notification_id=None):
    summary = clean_up_text(summary)
    message = clean_up_text(message)
    notify2.init(app_name)
    notification = notify2.Notification(summary, message, icon)
    urgency = urgency.lower()
    if urgency in urgencies:
        notification.set_urgency(urgencies[urgency])
    else:
        print("Urgency must be low|normal|critical")
        exit()
    if timeout:
        try:
            notification.set_timeout(int(timeout))
        except ValueError:
            print("Expire time must be integer")
            exit()
    if notification_id:
        try:
            notification.id = int(notification_id)
        except ValueError:
            print("Replace id has to be an integer")
            exit()
    try:
        notification.show()
    except DBusException as e:
        # Ignore DBus exceptions, mostly irrelevant
        print(e.get_dbus_message())
