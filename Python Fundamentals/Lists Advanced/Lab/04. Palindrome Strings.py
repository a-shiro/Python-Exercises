string = input().split()
searched_palindrome = input()

palindromes = [word for word in string if word == word[::-1]]
palindromes_count = palindromes.count(searched_palindrome)

print(palindromes)
print(f"Found palindrome {palindromes_count} times")