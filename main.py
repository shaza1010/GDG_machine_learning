
# live task in session 2

word = input("write your word: ")
vowel_count = 0
for letter in word:
    if letter in "aeiou":
        vowel_count += 1
print(f"uppercase: {word.upper()}")
print(f"vowel count: {vowel_count}")
print(f"reverse: {word[::-1]}")


