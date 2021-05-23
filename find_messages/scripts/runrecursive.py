from maildir2mbox import convert
from pathlib import Path

MAILDIR_PATH = "/media/jerzy/LuksPartition/maildir2mboxtestdata/maildir_temp"
MBOX_PATH = "/media/jerzy/LuksPartition/maildir2mboxtestdata/mbox_temp"

convert(Path(MAILDIR_PATH), Path(MBOX_PATH), True, True)
