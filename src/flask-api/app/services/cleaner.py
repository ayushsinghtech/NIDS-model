# app/services/cleaner.py
import os

def cleanup(files):
    for f in files:
        try:
            if os.path.exists(f):
                os.remove(f)
        except Exception as e:
            print("Error deleting file:", f, e)
