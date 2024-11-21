# coding: utf-8

import versioneer
import os

from typing import Dict
from file_handler import get_properties

from base_node_rpc.helpers import generate_protobuf_python_code, generate_python_code

DEFAULT_ARDUINO_BOARDS = []

PLATFORMIO_ENVS = ['teensy31']


def generate_all_python_code(lib_options: Dict) -> None:
    """
    Generate all Python (host) code, but do not compile device sketch or C++ Device code.
    """
    top = f"{'#' * 80} Generating All Python (host) Code {'#' * 80}"
    print(top)

    generate_protobuf_python_code(lib_options)
    generate_python_code(lib_options)

    print(f"{'#' * len(top)}")


def main():
    properties = get_properties(
        module_name="dropbot",
        package_name="dropbot",
        lib_name="Dropbot",
        prefix=os.getenv("CONDA_PREFIX"),
        source_dir=os.path.dirname(__file__)
    )

    top = '>' * 180
    print(top)

    generate_all_python_code(properties)

    print('<' * len(top))


if __name__ == '__main__':
    main()
