from hash_functions import *
import random

ripemd160 = gen_ripemd160_with_variable_scope_protector_to_not_pollute_global_namespace()
sha256 = gen_sha256_with_variable_scope_protector_to_not_pollute_global_namespace()

class Curve:
    def __init__(self, p, a, b):
        self.p = p
        self.a = a
        self.b = b

    def __str__(self):
        return f'Curve:\n  p:{str(self.p)}\n  a:{str(self.a)}\n  b:{str(self.b)}'

bitcoin_curve = Curve(
    p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F,
    a = 0x0000000000000000000000000000000000000000000000000000000000000000,
    b = 0x0000000000000000000000000000000000000000000000000000000000000007,
)

class Point:
    def __init__(self, curve, x, y):
        self.curve = curve
        self.x = x
        self.y = y

    @classmethod
    def extended_euclidean_algorithm(cls, a, b):
        old_r, r = a, b
        old_s, s = 1, 0
        old_t, t = 0, 1
        while r != 0:
            quotient = old_r // r
            old_r, r = r, old_r - quotient * r
            old_s, s = s, old_s - quotient * s
            old_t, t = t, old_t - quotient * t
        return old_r, old_s, old_t
    
    @classmethod
    def inv(cls, n, p):
        gcd, x, y = cls.extended_euclidean_algorithm(n, p)
        return x % p
    
    def encode(self, compressed, hash160=False):
        if compressed:
            prefix = b'\x02' if self.y % 2 == 0 else b'\x03'
            pkb = prefix + self.x.to_bytes(32, 'big')
        else:
            pkb = b'\x04' + self.x.to_bytes(32, 'big') + self.y.to_bytes(32, 'big')
        return ripemd160(sha256(pkb)) if hash160 else pkb
    
    def address(self, compressed=True, net='main') -> str:
        pkb_hash = self.encode(compressed=compressed, hash160=True)
        version = {'main': b'\x00', 'test': b'\x6f'}
        ver_pkb_hash = version[net] + pkb_hash
        checksum = sha256(sha256(ver_pkb_hash))[:4]
        byte_address = ver_pkb_hash + checksum
        b58check_address = b58encode(byte_address)
        return b58check_address
    
    def __add__(self, other):
        if self.x is None and self.y is None and self.curve is None:
            return other
        if other.x is None and other.y is None and other.curve is None:
            return self
        if self.x == other.x and self.y != other.y:
            return Point(None, None, None)
        if self.x == other.x:
            m = (3 * self.x**2 + self.curve.a) * self.inv(2 * self.y, self.curve.p)
        else:
            m = (self.y - other.y) * self.inv(self.x - other.x, self.curve.p)
        rx = (m**2 - self.x - other.x) % self.curve.p
        ry = (-(m*(rx - self.x) + self.y)) % self.curve.p
        return Point(self.curve, rx, ry)
    
    def __rmul__(self, k: int):
        assert isinstance(k, int) and k >= 0
        result = Point(None, None, None)
        append = self
        while k:
            if k & 1:
                result += append
            append += append
            k >>= 1
        return result
    
    def __eq__(self, other):
        return self.curve.p == other.curve.p and self.curve.a == other.curve.a and self.curve.b == other.curve.b and self.x == other.x and self.y == other.y
    
    def __str__(self):
        return f'Point:\n  x:{str(self.x)}\n  y{str(self.y)}'

G = Point(
    bitcoin_curve,
    x = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798,
    y = 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8,
)

class Generator:
    def __init__(self, G, n):
        self.G = G
        self.n =n

bitcoin_gen = Generator(
    G = G,
    n = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141,
)

def generate_random_key(start):
    key = random.randint(start, bitcoin_gen.n)
    return key

def address(secret_key):
    public_key_point = secret_key * G
    return public_key_point.address()

def generate_wallet_from(secret):
    key = secret
    if isinstance(secret, str):
        key = int.from_bytes(bytes(secret, 'utf-8'), 'big')
    addr = address(key)
    return key, addr

def generate_wallet(start=1):
    key = generate_random_key(start)
    addr = address(key)
    return key, addr