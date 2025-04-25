s = input().lower()
count=sum(1 for ch in s if ch in 'aeiou')
print("Vowel Count:",count)
