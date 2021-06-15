from maildir2mbox import convert
from pathlib import Path

# MAILDIR_PATH = "/media/jerzy/LuksPartition/maildir2mboxtestdata/maildir_test"
# MBOX_PATH = "/media/jerzy/LuksPartition/maildir2mboxtestdata/mbox_test"

MAILDIR_PATH = "/media/jerzy/LuksPartition/maildir_2012-2014/256GBKingston/mikolaj.ostrowski"
MBOX_PATH = "/media/jerzy/LuksPartition/maildir_2012-2014/mboxes"

convert(Path(MAILDIR_PATH), Path(MBOX_PATH), True, True, test=True)
