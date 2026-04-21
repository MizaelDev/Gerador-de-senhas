import secrets
import string

def generate_password(length: int = 16, use_symbols: bool = True) -> str:
    chars = string.ascii_letters + string.digits
    if use_symbols:
        chars += "!@#$%&*"

    # secrets é mais seguro que random para criptografia
    return "".join(secrets.choice(chars) for _ in range(length))

def calculate_entropy(password: str) -> float:
    import math
    charset = 0
    if any(c.islower() for c in password): charset += 26
    if any(c.isupper() for c in password): charset += 26
    if any(c.isdigit() for c in password): charset += 10
    if any(c in "!@#$%&*" for c in password): charset += 7

    if charset == 0:
        return 0.0
    return len(password) * math.log2(charset)