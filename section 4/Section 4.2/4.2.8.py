import pandas as pd

series = pd.Series(['apple', 'banana', 'cherry', 'date', 'fig', 'grape'])

def contains_two_vowels(word):
    vowels = 'aeiou'
    return sum(1 for char in word if char in vowels) >= 2

filtered_series = series[series.apply(contains_two_vowels)]

print("Original Series:")
print(series)
print("\nFiltered Series (words with at least two vowels):")
print(filtered_series)
