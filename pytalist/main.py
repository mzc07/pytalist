import argparse
import pathlib
from pytalist.validate import validate_file, validate_content


def build_parser():
    parser_global = argparse.ArgumentParser(
        prog="pytalist", description="CSV analyzer tool", epilog="version: 0.1"
    )

    parser_global.add_argument(
        "csv_file",
        type=pathlib.Path,
        help="Archivo utilizado para el flow del proyecto",
    )

    parser_global.add_argument(
        "--output", action="store", default="results.txt", help="Salida del archivo"
    )

    return parser_global


def main():
    parser = build_parser()
    argumentos_usuario = parser.parse_args()

    if validate_file(argumentos_usuario.csv_file):
        print(f"Validacion exitosa, {argumentos_usuario.csv_file.name} es un archivo")
        print(validate_content(argumentos_usuario.csv_file))


if __name__ == "__main__":
    main()
