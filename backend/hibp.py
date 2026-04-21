import hashlib
import requests

def check_password(password: str) -> int:
    """
    Retorna quantas vezes a senha foi encontrada em vazamentos.
    Retorna 0 se não foi encontrada.
    """
    sha1 = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    prefix = sha1[:5]
    suffix = sha1[5:]

    response = requests.get(
        f"https://api.pwnedpasswords.com/range/{prefix}",
        headers={"Add-Padding": "true"}  
    )
    response.raise_for_status()

    
    for line in response.text.splitlines():
        hash_suffix, count = line.split(":")
        if hash_suffix == suffix:
            return int(count)

    return 0