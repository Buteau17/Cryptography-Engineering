import random
from sympy.ntheory import isprime


def generate_prime_key(bits=512):
    prime = random.getrandbits(bits)
    while not isprime(prime):
        prime = random.getrandbits(bits)
    return prime


def generate_credential():
    return random.getrandbits(128)  # 128-bit random number

# Simple secret sharing - split the credential into 'n' parts
def split_credential(credential, n=3):
    shares = []
    total = 0
    for _ in range(n-1):
        part = random.randint(1, credential)
        shares.append(part)
        total += part
    shares.append(credential - total)  # ensure sum of parts equals the original credential
    return shares

# Example usage
if __name__ == "__main__":
    # Key setup
    public_key = generate_prime_key()
    
    # Generate a credential for a voter
    voter_credential = generate_credential()
    
    # Split the credential into parts for three tellers
    credential_shares = split_credential(voter_credential, n=3)
    
    print("Public Key:", public_key)
    print("Voter Credential (Secret):", voter_credential)
    print("Credential Shares:", credential_shares)
