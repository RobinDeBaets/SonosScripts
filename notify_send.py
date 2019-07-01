import notify2


def clean_up_text(text):
    return text.replace("\\n", "\n").replace("\\t", "\t")


urgencies = {
    "low": notify2.URGENCY_LOW,
    "normal": notify2.URGENCY_NORMAL,
    "critical": notify2.URGENCY_CRITICAL
}
tmp_file = "/tmp/notify_send.py.address"


# Based on https://github.com/phuhl/notify-send.py
def send_notification(summary, body, urgency="normal", timeout=None, app_name="", notification_id=None, icon=None):
    summary = clean_up_text(summary)
    body = clean_up_text(body)
    notify2.init(app_name)
    if icon and body:
        notification = notify2.Notification(summary, message=body, icon=icon)
    elif icon:
        notification = notify2.Notification(summary, icon=icon)
    elif body:
        notification = notify2.Notification(summary, message=body)
    else:
        notification = notify2.Notification(summary)
    urgency = urgency.lower()
    if urgency in urgencies:
        notification.set_urgency(urgencies[urgency])
    else:
        print("urgency must be low|normal|critical")
        exit()
    if timeout:
        try:
            notification.set_timeout(int(timeout))
        except ValueError:
            print("expire-time must be integer")
            exit()
    if notification_id:
        try:
            notification.id = int(notification_id)
        except ValueError:
            print("replaces-id has to be an integer")
            exit()
    notification.show()
