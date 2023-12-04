import hashlib

def encrypt_password(password):
    # Using SHA-256 to hash the password
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password
