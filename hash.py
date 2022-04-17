import hmac
import hashlib
import binascii

def get_hash_code(msg, key):
    key = binascii.unhexlify(key)
    msg = msg.encode()
    return hmac.new(key, msg, hashlib.sha256).hexdigest().upper()

def check_integrity_msg(msg, key, code_rev):
    if code_rev == get_hash_code(msg, key):
        return True
    else:
        return False

if __name__ == "__main__":
    print(get_hash_code("PYTHON | language", "5D2E44719232EA78CD2B32"))