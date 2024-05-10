"""
DLL Reverse Proxy Generator.

This script generates a function forwarding header for proxy DLL generation.
It is expected that DUMPBIN.EXE is in the path.
Forked from https://www.codeproject.com/Articles/17863/Using-Pragmas-to-Create-a-Proxy-DLL by Aaron Dobie, KPMG
Updates added by ZephrFish, updated to Python3, added functions to streamline things and updated readme to reflect
"""

import logging
import argparse
import os
import subprocess
import sys

def setup_logging():
    """ Set up the logging configuration. """
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)-8s %(message)s', datefmt='%d-%b-%y %H:%M:%S')

def parse_arguments():
    """ Parse command line arguments. """
    parser = argparse.ArgumentParser(description="DLL Reverse Proxy Generator")
    parser.add_argument("-o", "--output-dir", dest="odir", default=".", metavar="DIR", help="Specify output directory.")
    parser.add_argument("dll_names", nargs='+', help="DLL(s) to process.")
    return parser.parse_args()

def generate_proxy_header(dll_path, output_dir):
    """ Generate proxy header from the DLL specified. """
    base_name = os.path.splitext(os.path.split(dll_path)[1])[0]
    output_name = os.path.join(output_dir, f"{base_name}_fwd.h")

    logging.info(f"Processing '{dll_path}'.")
    logging.info(f"Generating '{output_name}'.")

    with open(output_name, "w") as f_out:
        # Run dumpbin and process output.
        process = subprocess.Popen(f"dumpbin -exports {dll_path}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate()

        if stderr:
            logging.error(stderr)

        permission = False
        for line in stdout.splitlines():
            line = line.strip()
            if line.lower().startswith("ordinal"):
                permission = True
                continue
            if line.lower().startswith("summary"):
                permission = False
            if permission and "forwarded to " not in line.lower():
                try:
                    src_export = line.split()[-1].replace(")", "")
                    f_out.write(f'#pragma comment(linker, "/export:{src_export}={dll_path}.{src_export}")\n')
                except IndexError:
                    logging.warning(f"Failed to process line: {line}")

def main():
    setup_logging()
    args = parse_arguments()

    for dll_name in args.dll_names:
        generate_proxy_header(dll_name, args.odir)

    logging.info("All done, go hijack those DLLs.")

if __name__ == "__main__":
    main()
