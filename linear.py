def linear_search(roll_numbers, target):
      for i in range(len(roll_numbers)):
          if roll_numbers[i] == target:
              return i
      return -1
  
roll_numbers = [101,102,103,104,105]
target = 104
result = linear_search(roll_numbers, target)
  
if result != -1:
      print(f"Element found at index {result}")
else:
      print("Element not found")
  
