# arrays and hashing

`contains-duplicate.py`
https://leetcode.com/problems/contains-duplicate/description/
- there are multiple ways of solving this problem but the best way is to use a set or a hashmap
- the set/map is used to track the numbers that have been found in the array
- when we encounter a number that is already in the set/map we return True
- if we encounter a number that is not in the set/map we add it in the set

`valid-anagram.py`
https://leetcode.com/problems/valid-anagram/description/
- two strings are anagrams if they have the same characters and frequency of characters, aka reshuffling the characters they will spell the same thing
- the easy / brute force solution is to sort both strings and check if they are the same
- the more efficient solution is to add the frequency of both letters in the string to a hash table and keep track of how frequent
- then we can check if the hash maps are the same, if they are then they are anagrams