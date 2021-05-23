from find_messages.find_message_id import find_messages

MAILDIR_PATH = "/media/jerzy/LuksPartition/maildir2mboxtestdata/maildir_temp"
MBOX_PATH = "/media/jerzy/LuksPartition/maildir2mboxtestdata/mbox_temp.sbd"

find_messages(MAILDIR_PATH, MBOX_PATH)
