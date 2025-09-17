import os, sys

def search_files(term: str):
    # ❌ os.system with unsanitized input allows command injection
    cmd = "grep -R " + term + " ."
    print("Running:", cmd)
    os.system(cmd)

if __name__ == "__main__":
    term = sys.argv[1] if len(sys.argv) > 1 else "TODO"
    search_files(term)