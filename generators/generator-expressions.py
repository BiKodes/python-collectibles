# List comprehension produces the complete list of items at once:
a = range(6)
print("List comprehension", end=':')
b = [x + 2 for x in a]
print(b)

# generator expression which returns the same items but one at a time:
print("Generator expression", end=':n')
c=(x+2 for x in a)
print(c)
for y in c:
    print(y)

# Generator functions can be used within other functions as well:
a = range(6)
print("Generator expression", end=':n')
c = (x+2 for x in a)
print(c)
print(min(c))

cookie_list = ["Raspberry", "Choc-Chip", "Cinnamon", "Oat"]

cookie_generator = (cookie for cookie in cookie_list)

for cookie in cookie_generator:
    print(cookie)

# Reading Large Files:
csv_gen = (row for row in open(file_name))

nums_squared_gc = (num**2  for num in range(5))

# Creating Data Pipelines With Generators:

file_name = "techcrunch.csv"
lines = (line for line in open(file_name))
list_line = (s.rstrip().split(",") for s in lines)
cols = next(list_line)

company_dicts = (dict(zip(cols, data)) for data in list_line)

funding = (
    int(company_dict["raisedAmt"])
    for company_dict in company_dicts
    if company_dict["round"] == "a"
)

total_series_a = sum(funding)
print(f"Total series A fundraising: Ksh.{total_series_a}")
