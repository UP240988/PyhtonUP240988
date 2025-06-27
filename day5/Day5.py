# 1. Declare an empty list
empty_list = []

# 2. Declare a list with more than 5 items
items_list = [1, 2, 3, 4, 5, 6, 7]

# 3. Find the length of your list
length_of_list = len(items_list)

# 4. Get the first item, the middle item, and the last item of the list
first_item = items_list[0]
middle_item = items_list[len(items_list) // 2]
last_item = items_list[-1]

# 5. Declare a list called mixed_data_types with personal details
mixed_data_types = ["Your Name", 25, 5.9, "Single", "Your Address"]

# 6. Declare a list variable named it_companies
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# 7. Print the list
print(it_companies)

# 8. Print the number of companies in the list
print(len(it_companies))

# 9. Print the first, middle, and last company
print(it_companies[0], it_companies[len(it_companies) // 2], it_companies[-1])

# 10. Modify one of the companies
it_companies[2] = "Meta"
print(it_companies)

# 11. Add an IT company
it_companies.append("Tesla")
print(it_companies)

# 12. Insert an IT company in the middle of the list
it_companies.insert(len(it_companies) // 2, "Twitter")
print(it_companies)

# 13. Change one IT company name to uppercase (IBM excluded!)
it_companies[1] = it_companies[1].upper()
print(it_companies)

# 14. Join the it_companies with a string '#; '
joined_companies = '#; '.join(it_companies)
print(joined_companies)

# 15. Check if a certain company exists in the list
print("Google" in it_companies)

# 16. Sort the list
it_companies.sort()
print(it_companies)

# 17. Reverse the list in descending order
it_companies.reverse()
print(it_companies)

# 18. Slice out the first 3 companies
print(it_companies[:3])

# 19. Slice out the last 3 companies
print(it_companies[-3:])

# 20. Slice out the middle IT company/companies
middle_index = len(it_companies) // 2
print(it_companies[middle_index:middle_index+1] if len(it_companies) % 2 == 1 else it_companies[middle_index-1:middle_index+1])

# 21. Remove the first IT company
it_companies.pop(0)
print(it_companies)

# 22. Remove the middle IT company/companies
middle_index = len(it_companies) // 2
it_companies.pop(middle_index)
print(it_companies)

# 23. Remove the last IT company
it_companies.pop(-1)
print(it_companies)

# 24. Remove all IT companies from the list
it_companies.clear()
print(it_companies)

# 25. Destroy the IT companies list
del it_companies

# 26. Join two lists
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)

# 27. Insert Python and SQL after Redux
full_stack.insert(full_stack.index("Redux") + 1, "Python")
full_stack.insert(full_stack.index("Python") + 1, "SQL")
print(full_stack)