import sys
import os


def find_messages(maildir_path, mbox_path):

    ids1 = []
    paths1 = {}
    for (r, s, f) in os.walk(maildir_path):
        for i in f:
            path = os.path.join(r,i)
            with open(path, 'rb') as read_obj:
                for line in read_obj:
                    if line.startswith(b"Message-ID"):
                        ids1.append(line)
                        paths1[line] = path
                        # print(line)

    ids2 = []

    for (r, s, f) in os.walk(mbox_path):
        for i in f:
            path = os.path.join(r,i)
            with open(path, 'rb') as read_obj:
                for line in read_obj:
                    if line.startswith(b"Message-ID"):
                        ids2.append(line)


    for item in set(ids1)-set(ids2):
        print(f"{paths1[item]} {item}")
        pass


if __name__ == "__main__":
    find_messages(sys.argv[1], sys.argv[2])
