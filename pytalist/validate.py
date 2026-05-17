import pathlib
import csv

def validate_file(archivo_csv: pathlib.Path = None) -> bool:
    if archivo_csv is None:
        raise FileNotFoundError("Error: No se proporcionó un archivo.")
        
    if not archivo_csv.is_file():
        raise FileNotFoundError(f"Error: Archivo no encontrado en la ruta: {archivo_csv.resolve()}")
        
    if archivo_csv.suffix.lower() != '.csv':
        raise ValueError(f"Error: El archivo {archivo_csv.name} no es un formato válido. Debe ser .csv")
        
    return True

def validate_content(archivo_csv: pathlib.Path):
    with open(archivo_csv, newline='', encoding='utf-8') as file:
        read_file = csv.DictReader(file)
        index_file = next(read_file, None)
        if index_file is None:
            raise ValueError('Error: El Archivo CSV esta vacio')

        headers_file = index_file.keys()
        for header in headers_file:
            print(header)
