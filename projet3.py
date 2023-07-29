def bytes_to_list(file_path):
    with open(file_path, "rb") as f:
        global binary_data
        binary_data = f.read()

    # Bytes to lists
    byte_list = list(binary_data)
    return byte_list


def add_corruption(byte_list):
    # Add corruption
    byte_list[:3] = [222, 196, 43]
    return byte_list


def restore_original(byte_list):
    # Remove corruption
    byte_list[:3] = [octet for octet in binary_data[:3]]
    return byte_list


def list_to_bytes(byte_list):
    # Lists to bytes
    byte_data = bytes(byte_list)
    return byte_data










reponse = input("Entrez le mot de passe pour accéder à l'image.")

while reponse == "yagds38":

    pass 

else:
    file_path = "6.png"

    byte_list = bytes_to_list(file_path)
    global byte_list_corrupted
    byte_list_corrupted = add_corruption(byte_list)
    byte_data_corrupted = list_to_bytes(byte_list_corrupted)

    # Écrire les données corrompues
    with open(file_path, "wb") as k:
        k.write(byte_data_corrupted)

    reponse = input("MAUVAIS MOT DE PASSE. Entrez le mot de passe pour accéder à l'image.")

    # Je ne suis pas sûr de l'intention derrière cette condition "elif".
    # Supposons qu'elle fasse partie du bloc "else" et ne soit pas une condition séparée.
    # Si ce n'est pas le cas, veuillez fournir plus de contexte pour une meilleure assistance.

    # Récupérer les données d'origine
    restored_byte_list = restore_original(byte_list_corrupted)
    byte_data_restored = list_to_bytes(restored_byte_list)

    # Écrire les données d'origine
    with open(file_path, "wb") as f:
        f.write(byte_data_restored)
