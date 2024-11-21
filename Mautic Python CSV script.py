import pandas as pd
import os

# Ruta base donde están los archivos CSV (modifica esta ruta según tu entorno)
base_path = r"/path/to/your/csv/files"

# Lista de nombres de archivos CSV a procesar
file_names = [
    "sample_file_1.csv",
    "sample_file_2.csv",
    "sample_file_3.csv"
]

# Crear una lista para consolidar los datos
consolidated_data = []

# Columnas posibles para nombres y correos electrónicos
possible_name_columns = ['name', 'nombre', 'first_name', 'last_name', 'first', 'last']
possible_email_columns = ['email', 'correo', 'mail']

# Función para intentar leer un archivo CSV con varias codificaciones
def read_csv_with_encoding(file_path, encodings=['utf-8', 'utf-16', 'latin-1']):
    for encoding in encodings:
        try:
            return pd.read_csv(file_path, encoding=encoding)
        except Exception:
            continue
    raise ValueError(f"Unable to read the file: {file_path} with available encodings.")

# Procesar cada archivo
for file_name in file_names:
    file_path = os.path.join(base_path, file_name)
    try:
        # Leer el archivo con la función que prueba varias codificaciones
        df = read_csv_with_encoding(file_path)
        
        # Identificar columnas relevantes
        name_column = next((col for col in df.columns if col.lower() in possible_name_columns), None)
        email_column = next((col for col in df.columns if col.lower() in possible_email_columns), None)
        
        if name_column and email_column:
            # Seleccionar las columnas relevantes y renombrarlas
            temp_df = df[[name_column, email_column]].rename(columns={name_column: 'nombre', email_column: 'email'})
            consolidated_data.append(temp_df)
    except Exception as e:
        print(f"Error processing {file_name}: {e}")

# Unir todos los datos
final_df = pd.concat(consolidated_data, ignore_index=True)

# Eliminar duplicados por correo electrónico
final_df = final_df.drop_duplicates(subset=['email'])

# Guardar el archivo consolidado
output_path = os.path.join(base_path, "mautic_contacts_final.csv")
final_df.to_csv(output_path, index=False)

print(f"File '{output_path}' created successfully with {len(final_df)} contacts.")
