import ctypes

crypto_lib = ctypes.CDLL('./encryption.dylib')

crypto_lib.encrypt.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
crypto_lib.encrypt.restype = ctypes.c_char_p

crypto_lib.decrypt.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
crypto_lib.decrypt.restype = ctypes.c_char_p

def encrypt(text, key):
    return crypto_lib.encrypt(text.encode('utf-8'), key.encode('utf-8')).decode('utf-8')

def decrypt(text, key):
    return crypto_lib.decrypt(text.encode('utf-8'), key.encode('utf-8')).decode('utf-8')
