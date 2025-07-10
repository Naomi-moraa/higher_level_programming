def remove_char_at(str, n):
    if n < 0 or n >= len(str):
        return str
    return str[:n] + str[n+1:]

# Example usage (you can include this for local testing)
print(remove_char_at("Best School", 3))   # "Bes School"
print(remove_char_at("Python", 0))        # "ython"
print(remove_char_at("Python", 10))       # "Python" (out of range, return original)