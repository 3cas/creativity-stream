import os


STREAM_DIR = "./test_a"


def organize():
    for file_name in os.listdir(STREAM_DIR):
        file_path = os.path.join(STREAM_DIR, file_name)
        with open(file_path, "r") as f:
            lines = f.read().split("\n")
        
        for line in lines:
            line_split = line.strip().split()

            marker = line_split[0].replace(":", "")

            if marker == "lyr":
                pass

            if marker == "idkidk":
                pass

            else:
                pass # not a marker