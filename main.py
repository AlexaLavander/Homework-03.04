from pprint import pprint

with open("receipts.txt", "rt") as f:
  cook_book = {}
  for receipt in f:
    dish = receipt.strip()
    amount = int(f.readline())
    product = []
    for _ in range(amount):
      ingredient_name, quantity, measure = f.readline().strip().split(" | ")
      product.append({
        "ingredient_name": ingredient_name,
        "quantity": quantity,
        "measure": measure
      }
      )
    cook_book[dish] = product
    f.readline()
print("cook_book =")
pprint(cook_book, sort_dicts = False)

print()
print()
def get_shop_list_by_dishes(dishes, person_count):
  product = {}
  for dish in dishes:
    receipt = cook_book[dish]
    for ingredients in receipt:
      name = ingredients["ingredient_name"]
      measure_quantity = {}
      measure_quantity["measure"] =  ingredients["measure"]
      measure_quantity["quantity"] =  int(ingredients["quantity"])*person_count
      product[name] = measure_quantity
  pprint(product)
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
print()




lines_in_file_1 = []
with open("1.txt", "r") as f:
  for line in f:
    lines_in_file_1.append([line.strip()])


lines_in_file_2 = []
with open("2.txt", "r") as f:
  for line in f:
    lines_in_file_2.append([line.strip()])

lines_in_file_3 = []

with open("3.txt", "r") as f:
  for line in f:
    lines_in_file_3.append([line.strip()])

lines_in_files = []
lines_in_files.append(lines_in_file_1)
lines_in_files.append(lines_in_file_3)
lines_in_files.append(lines_in_file_2)
lengths = {}


lengths["3.txt"] = len(lines_in_file_3)
lengths["2.txt"] = len(lines_in_file_2)
lengths["1.txt"] = len(lines_in_file_1)

sorted_files = {}
sorted_values =sorted(lengths.values())
for amount in sorted_values:
    for key in lengths.keys():
        if lengths[key] == amount:
            sorted_files[key] = lengths[key]
for file in sorted_files:
  print(file)
  print(sorted_files[file])
  with open(file,"r") as f:
    print(f.read())
    print()

