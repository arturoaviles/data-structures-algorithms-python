import hashlib

thing_to_hash = "a"

encoded = thing_to_hash.encode("utf-8")

hash1 = hashlib.md5(encoded)
print(hash1.digest())
print(hash1.hexdigest())


hash2 = hashlib.sha512(encoded)
print(hash2.digest())
print(hash2.hexdigest())