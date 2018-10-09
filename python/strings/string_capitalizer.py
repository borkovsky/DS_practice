# capitalize
# # You are asked to ensure that the first and last names of 
# people begin with a capital letter in their passports. 
# For example, alison heck should be capitalised correctly as Alison Heck.

def solve(s):
  s_list = s.split()
  s_list_cap = []
  for elem in s_list:
    print(elem)
    s_list_cap.append(elem.capitalize())
    return s_list_cap