# HUGE THANKS TO !j0 (https://github.com/j0912345) for helping me extraordinarily with patching the save file!
def patchSaveFile(choice:str,path:str):
    if path.endswith(".list") or path.endswith(".pack") or path.endswith(".so") or path.endswith(".csv"):
        raise Exception("Not a save file")

    location_bytes = bytes("battlecats", "ascii")
    if choice != "jp":
        location_bytes = bytes("battlecats"+choice, "ascii")
    checksum_length = 32

    stream = io.open(path, mode='r+b')
    file_data_len = os.path.getsize(path) - checksum_length
    file_len = file_data_len + 32
    user_save_data_without_checksum = stream.read(file_data_len)
    #test = checksum_length - len(location_bytes)
    data_to_get_checksum_of = (location_bytes + user_save_data_without_checksum)
    save_hash = hashlib.md5(data_to_get_checksum_of).hexdigest()

    stream.seek(file_data_len)
    stream.write(bytes(save_hash, "ascii"))
    stream.close()
