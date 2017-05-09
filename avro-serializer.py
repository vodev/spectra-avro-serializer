import avro.schema
from avro.datafile import DataFileWriter
from avro.io import DatumReader, DatumWriter
import os
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("""
        Expected 2 arguments
        Usage: python3 avro-serializer.py path/to/spectra/root/dir path/to/output/avro/dir
        """)
        exit(1)
    context_directory = sys.argv[1]
    path_directory = sys.argv[2]
    print("Checking context directory existence")
    if not os.path.isdir(context_directory):
        print("Context directory does not exist")
        exit(2)
    print("Creating path directory if necessary")
    os.makedirs(path_directory, exist_ok=True)
    print("Checking permissions")
    if not os.access(path_directory, os.W_OK):
        print("Missing write persmissions!")
        exit(3)
    print("Parsing Avro schema")
    schema = avro.schema.Parse(open("fits-files.avsc", "r").read())
    print("Starting walk procedure...")
    avro_counter = 0
    for (path, dn, filenames) in os.walk(context_directory):
        if len(filenames) == 0:
            continue
        avro_counter += 1
        avro_output = os.path.join(path_directory, os.path.basename(path) + ".avro")
        writer = DataFileWriter(open(avro_output, "wb"), DatumWriter(), schema, codec="deflate")
        print("Writing files to {}...".format(avro_output))
        for f in filenames:
            p = os.path.join(path, f)
            with open(p, "rb") as ff:
                content = ff.read()
            writer.append({"name": f, "content": content})
        writer.close()
        print("   Total {} files written into .avro file".format(len(filenames)))
    print("Walk procedure completed. Total {} .avro files created".format(avro_counter))
