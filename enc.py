import os, sys , platform
    
try:
    __import__("cython")
except Exception as e:
    exit(str(e))
