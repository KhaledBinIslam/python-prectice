# Loop through the letters in the word "banana":
for x in "banana":
    print(x)
# To get the length of a string, use the len() function.
a= "hello world!"
print(len(a))

# To check if a certain phrase or character is present in a string, we can use the keyword in.
txt = "the best things life is free!"
print("free" in txt)

# Print only if "free" is present:
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

  # Check if "expensive" is NOT present in the following text:
  txt = "The best things in life are free!"
  print("expensive" not in txt)

  # print only if "expensive" is NOT present:
  txt = "The best things in life are free!"
  if "expensive" not in txt:
      print("No, 'expensive' is NOT present.")