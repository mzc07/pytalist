import pathlib

def validate_file(archivo_csv:pathlib.Path=None):
    if archivo_csv is None:
        raise FileNotFoundError('Error: No se proporciono un archivo.')

    if not archivo_csv.is_file():
        raise FileNotFoundError(f'Error: Archivo no encontrado en la ruta: {archivo_csv.resolve()}')

    if archivo_csv.suffix.lower() != '.csv':
        raise ValueError(f'Error: El archivo {archivo_csv.name} no es un archivo válido')

    return True