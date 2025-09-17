import pickle

def load_user(data: bytes):
    # ❌ Never unpickle untrusted data!
    return pickle.loads(data)

if __name__ == "__main__":
    # Example: this is still unsafe even if you think you trust the source
    demo = pickle.dumps({"role": "admin"})
    print(load_user(demo))