#Utility functions
import re

def normalize(text):
    text = text.lower()
    words = re.findall(r'\b\w+\b', text)
    return words

def tokenize(text):
    return list(set(normalize(text)))