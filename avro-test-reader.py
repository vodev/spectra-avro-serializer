from avro.datafile import DataFileReader
from avro.io import DatumReader

import os
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("You must specify .avro file as the first argument")
        exit(1)
    avro_path = sys.argv[1]
    if not os.path.isfile(avro_path):
        print("Specified file does not exist")
        exit(2)
    reader = DataFileReader(open(avro_path, "rb"), DatumReader())
    for f in reader:
        print(f)
    reader.close()
