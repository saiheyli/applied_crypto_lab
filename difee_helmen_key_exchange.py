import secrets

def demo():
    # Publicly agreed parameters (small for demo only)
    # In real use, p should be a large prime (2048+ bits).
    p = 23        # prime modulus (small for demonstration)
    g = 5         # generator

    print(f"Public parameters: p = {p}, g = {g}\n")

    # Alice picks a private key a (secret)
    a = secrets.randbelow(p-2) + 1   # 1 <= a <= p-2
    A = pow(g, a, p)                 # Alice's public value
    print(f"Alice private a = {a}")
    print(f"Alice public A = g^a mod p = {A}\n")

    # Bob picks a private key b (secret)
    b = secrets.randbelow(p-2) + 1
    B = pow(g, b, p)                 # Bob's public value
    print(f"Bob private b = {b}")
    print(f"Bob public B = g^b mod p = {B}\n")

    # Exchange (A and B are exchanged over the network)
    # Alice computes shared secret: s = B^a mod p
    s_alice = pow(B, a, p)
    # Bob computes shared secret: s = A^b mod p
    s_bob = pow(A, b, p)

    print(f"Alice's computed shared secret: {s_alice}")
    print(f"Bob's computed shared secret:   {s_bob}")

    assert s_alice == s_bob, "Shared secrets do not match!"
    print("\nShared secret established successfully.")

if __name__ == "__main__":
    demo()
