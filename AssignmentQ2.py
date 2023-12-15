# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 16:43:27 2023

@author: kaman
"""

import pandas as pd

def countVowels(name):
    """
    This is to count the vowels in a string

    Parameters
    ----------
    name : string
        The string to be checked.

    Returns
    -------
    int
        Total number of vowels in the string.

    """
    vowels = "aeiouAEIOU"
    return sum(name.count(vowel) for vowel in vowels)

# Read file into a df
df = pd.read_csv('data/titles.csv', keep_default_na=False)

df['vowels'] = df.apply(lambda row: countVowels(row.title), axis = 1)

print(df)