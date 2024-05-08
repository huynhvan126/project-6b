# Author: Van Huynh
# GitHub username: huynhvan126
# Date: 05/08/2024
# Description: add surnames to the list of names that start with "K".
def add_surname(first_name):
    """Define a function named add_surname that takes as a parameter a list of first names."""
    kardashian_names = [name + " Kardashian" for name in first_name if name.startswith("K")]
    return kardashian_names
