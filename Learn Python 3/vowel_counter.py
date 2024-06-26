vowels = ["a", "e", "i", "o", "u"]

# Write your function here
def vowel_counter(word):
  counter = 0
  for i in word:
    if i in vowels:
      counter += 1
  return counter

print(vowel_counter("hello"))