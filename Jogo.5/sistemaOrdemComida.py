italian_food = ["Pasta Bolognese", "Pepperoni Pizza", "Margherita Pizza", "Lasagna"]
indian_food = ["Curry", "Chutney", "Samosa", "Naan"]
print("Bem-vindo! Ao sistema de Pedido de Comidas!\n")
while True:
  food_type = input("Qual comida gostaria?\nTemos comida Italiana e Indiana.\n").capitalize() #deixa a primeira maiuscula
  if food_type == "Italiana" or food_type == "Indiana":
    break
  else:
    print("Não servimos esse tipo de prato, escolha novamente, por favor.\n")  

def display_available_meals(food_type):
  if food_type == "Italiana":    
    for diches in italian_food:
      print(diches)
  elif food_type == "Indiana":
    for diches in indian_food:
      print(diches) 

def find_meal(name, food, amount):
    if food == "Italiana":
      menu = italian_food
    else:
      menu = indian_food  
    return f"{amount}: {name}" if name in menu else "Meal not found"  

display_available_meals(food_type)
name_input = input("Which meal: ").title() #deixa cada palavra maiuscula
amount_input = int(input("Amount of meal: "))

result = find_meal(name_input, food_type, amount_input)
print(result)