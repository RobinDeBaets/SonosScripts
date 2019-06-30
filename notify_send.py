from multiprocessing.connection import Listener, Client

import notify2


def clean_up_text(text):
    return text.replace("\\n", "\n").replace("\\t", "\t")


urgencies = {
    "low": notify2.URGENCY_LOW,
    "normal": notify2.URGENCY_NORMAL,
    "critical": notify2.URGENCY_CRITICAL
}


# Based on https://github.com/phuhl/notify-send.py
def send_notification(summary, body, urgency="normal", timeout=None, app_name="", category=None, hints=None,
                      replaces_process=None, replaces_id=None, icon=None):
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

    if category:
        notification.set_category(category)

    if hints:
        for hint in hints:
            try:
                [hint_type, key, value] = hint.split(':')
                if hint_type == "boolean":
                    if (value == "True") or (value == "true"):
                        notification.set_hint(key, True)
                    elif (value == "False") or (value == "false"):
                        notification.set_hint(key, False)
                    else:
                        print("valid types for boolean are: True|true|False|false")
                        exit()
                elif hint_type == "int":
                    notification.set_hint(key, int(value))
                elif hint_type == "byte":
                    notification.set_hint_byte(key, int(value))
                else:
                    print("Valid types are int, double, string, boolean and byte")
            except ValueError:
                print("hint has to be in the format TYPE:KEY:VALUE")
                exit()

    if replaces_id is not None:
        try:
            notification.id = int(replaces_id)
        except ValueError:
            print("replaces-id has to be an integer")
            exit()

    if replaces_process:
        try:
            with open("/tmp/notify_send.py.address", "r") as pidf:
                conn = Client(pidf.read())
                conn.send([notification, replaces_process])
                conn.close()
        except:
            listener = Listener()
            with open("/tmp/notify_send.py.address", "w") as pidf:
                pidf.write(listener.address)
            replaces_processes = {}
            notification.show()
            replaces_processes[replaces_process] = notification.id
            while True:
                conn = listener.accept()
                [notification, replaces_process] = conn.recv()
                if replaces_process in replaces_processes:
                    notification.id = replaces_processes[replaces_process]
                notification.show()
                replaces_processes[replaces_process] = notification.id
                conn.close()
    else:
        notification.show()
        print(notification.id)
