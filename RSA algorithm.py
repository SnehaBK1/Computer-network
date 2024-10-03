import random

def gcd(a, b):
    """Compute the greatest common divisor of a and b."""
    while b != 0:
        a, b = b, a % b
    return a

def modinv(a, m):
    """Compute the modular inverse of a modulo m."""
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_prime():
    """Generate a random prime number."""
    while True:
        num = random.randint(2**7, 2**8)  # Generate a number between 128 and 256
        if is_prime(num):
            return num

def generate_keypair():
    """Generate RSA public and private keys."""
    p = generate_prime()
    q = generate_prime()
    
    while p == q:  # Ensure p and q are distinct
        q = generate_prime()

    n = p * q
    phi = (p - 1) * (q - 1)

    e = 65537  # Commonly used prime for e
    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)

    d = modinv(e, phi)
    
    return (e, n), (d, n)

def encrypt(public_key, plaintext):
    """Encrypt the plaintext using the public key."""
    e, n = public_key
    cipher = [pow(ord(char), e, n) for char in plaintext]
    return cipher

def decrypt(private_key, ciphertext):
    """Decrypt the ciphertext using the private key."""
    d, n = private_key
    plain = ''.join(chr(pow(char, d, n)) for char in ciphertext)
    return plain

# Example usage
if __name__ == "__main__":
    public_key, private_key = generate_keypair()
    
    print("Public Key:", public_key)
    print("Private Key:", private_key)

    message =input('enter the message:')
    
    ciphertext = encrypt(public_key, message)
    print("Ciphertext:", ciphertext)

    decrypted_message = decrypt(private_key, ciphertext)
    print("Decrypted Message:", decrypted_message)