from find_messages.find_message_id import find_messages

# MAILDIR_PATH = "/media/jerzy/LuksPartition/maildir2mboxtestdata/maildir_test"
# MBOX_PATH = "/media/jerzy/LuksPartition/maildir2mboxtestdata/mbox_test.sbd"


MAILDIR_PATH = "/media/jerzy/LuksPartition/maildir_2012-2014/256GBKingston/"
MBOX_PATH = "/media/jerzy/LuksPartition/maildir_2012-2014/mbox.sbd"

find_messages(MAILDIR_PATH, MBOX_PATH)
