#!/usr/bin/env python
# coding: utf-8

# In[85]:


def unicode_to_math_symbol(unicode_string):
    unicode_list = unicode_string.split()
    math_symbols = []

    for code_point in unicode_list:
        try:
            code_point_int = int(code_point, 16)  # Convert hexadecimal string to integer
            math_symbol = chr(code_point_int)
            math_symbols.append(math_symbol)
        except ValueError:
            math_symbols.append("[Invalid Unicode]")

    return " ".join(math_symbols)

# Example usage
unicode_input = input("Enter Unicode code points separated by spaces: ")
result = unicode_to_math_symbol(unicode_input)
print("Math Symbols:", result)


# In[ ]:




