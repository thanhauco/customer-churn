def assign_variant(uid):
    return 'A' if hash(uid) % 2 == 0 else 'B'