#two.py

import one

print("TOP LEVEL IN TWO.PY")

one.func()

if __name__ == '__main__':
    print("TWO.PY is beign run directly")
else:
    print("TWO.PY is beign imported")
