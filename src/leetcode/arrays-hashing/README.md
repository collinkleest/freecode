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

`two-sum.py`
https://leetcode.com/problems/two-sum/description/

- brute force method, compare every number (not efficient O(n^2) time complexity)
- faster method would be getting the difference and keeping track of numbers in a hashmap
- if difference is in the hashmap then we know the current number + the difference number in the hashmap are our two numbers

`group-anagrams.py`
https://leetcode.com/problems/group-anagrams/

- sort each string and use hashmap to map sorted string -> array of strs therefore grouping the anagrams
- this is the easiest solution and the first one i came across
- **remember** a list is not hashable in python, we can convert to string or tuple to make it hashable
- we can use a default dictionary from `collections` module to create a dict with a default value of an empty array like so `defaultdict(list)`
- this will never raise a key error
