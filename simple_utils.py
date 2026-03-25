# simple_utils.py - A tiny utility library

def reverse_string(text):
    """
    Reverse the characters in a string.
    
    Returns:
        reversed_text (str): The input string with characters in reverse order.
    """
    return text[::-1]

def count_words(sentence):
    """
    Count the number of words in a sentence.
    
    Parameters:
        sentence (str): Input text; words are delimited by whitespace.
    
    Returns:
        int: Number of whitespace-delimited words in the input sentence.
    """
    return len(sentence.split())

def celsius_to_fahrenheit(celsius):
    """
    Convert a temperature from degrees Celsius to degrees Fahrenheit.
    
    Parameters:
        celsius (float): Temperature in degrees Celsius.
    
    Returns:
        float: Temperature converted to degrees Fahrenheit.
    """
    return (celsius * 9/5) + 32
