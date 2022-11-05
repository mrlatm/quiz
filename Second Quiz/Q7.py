text = "Today is difficult, tomorrow is much more difficult, but the day after tomorrow is beautiful. most people die tomorrow evening."
text = text.split()
first_word, *rest, last_word = text
print("-"*80)
print(f"first word: {first_word}\nlastword: {last_word}\nrest: {rest}")
print("-"*80)