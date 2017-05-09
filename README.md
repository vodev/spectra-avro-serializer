Spectra Avro Serializer
=======================

This tool utilizes Apache Avro serializing format to merge multiple small astronomical spectra files to a single file with `.avro` extension. It was specifically created for the purposes of converting the LAMOST-DR1 spectra archive containing millions of spectra files in FITS format into a smaller amount of bigger `.avro` files. Avro files effectively solves the Small files problem in the HDFS.

Requirements
------------

In order to install `avro` Python package to your environment, follow installation instructions from the [official Avro documentation](https://avro.apache.org/docs/1.8.1/gettingstartedpython.html).

Usage
-----

The tool consists of a serializer Python source and the example reader. The serializer can be started by executing the following command:
```bash
python3 avro-serializer.py path/to/spectra/root/dir path/to/output/avro/dir
```
It converts every non-empty directory inside `path/to/spectra/root/dir` directory into an `.avro` file with the same name in the `path/to/output/avro/dir` directory.

The test reader can be used by executing the following command:
```bash
python3 avro-test-reader.py path/to/avro/file
```

It prints the content of the passed `.avro` file to the standard output stream.


