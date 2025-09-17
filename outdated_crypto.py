import hashlib, random

# ❌ Predictable randomness due to fixed seed
random.seed(1337)

def weak_hash(password: str) -> str:
    # ❌ MD5 is not safe for passwords; use bcrypt/argon2/scrypt with salt
    return hashlib.md5(password.encode()).hexdigest()

def insecure_token():
    # ❌ Predictable token derived from predictable randomness
    return str(random.randint(0, 10_000))

if __name__ == "__main__":
    print("Weak hash of 'password':", weak_hash("password"))
    print("Insecure token:", insecure_token())