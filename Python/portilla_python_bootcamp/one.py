#python one.py
#python runs all the def's at indent level 0
#and in the background when you do python one.property
#it assigns __name__ = "__main__"
#so below we got the direct call check
# if __name__ == "__main__":
#   set the order of execution

def func():
    print("I AM IN ONE.PY")

print("I am at the top")

if __name__ == "__main__":
    print("one.py is beign run directly")
else:
    print("one.py is beign imported")
