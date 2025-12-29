import os
 
DING_DIR = ".ding"

def init(path):
    abs_path = os.path.abspath(path)

    if not os.path.exists(abs_path):
        print(f"Error: path does not exist: {abs_path}")
        return

    if not os.path.isdir(abs_path):
        print(f"Error: not a directory: {abs_path}")
        return

    ding_path = os.path.join(abs_path, DING_DIR)

    if os.path.exists(ding_path):
        print("It is already a ding repository")
        return

    os.mkdir(ding_path)
    print(f"Initialized empty Ding repository in {ding_path}")
