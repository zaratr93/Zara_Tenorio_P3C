#Homogeneous List

integers = [1, 2, 3, 4, 5]

animals = ["dog", "cat", "dolfin"]

names = ["Yoongi", "Hobi", "Taehyung"]

floats =  [9.3, 2.9, 22.2, 7.7]

#Heterogeneous List

numbers_animals_names = ["dog", 31, "Yoongi", 7.7]

list_lists = [[1, 2, 3], ["dog", "cats", "dragonfly"], ["Namjoon", "Seokjin", "Yoongi", "Hoseok", "Taehyung", "Jimin", "Jungkook"]]

#How to acces an element in a list

list = [30, 32, 39, 88]

words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew",
    "kiwi", "lemon", "mango", "nectarine", "orange", "papaya", "quince", "raspberry",
    "strawberry", "tangerine", "ugli", "vanilla", "watermelon", "apricot", "blackberry",
    "cantaloupe", "dragonfruit", "eggplant", "jackfruit", "lime", "mulberry", "nectar",
    "olive", "peach", "pear", "pineapple", "pomegranate", "quinoa", "rhubarb", "soursop",
    "tomato", "zucchini", "artichoke", "broccoli", "carrot", "daikon", "endive", "fennel",
    "garlic", "horseradish", "jalapeno", "kale", "leek", "mushroom", "navy bean", "onion",
    "parsnip", "quinoa", "radish", "spinach", "turnip", "yam", "zucchini", "almond",
    "brazil nut", "cashew", "chestnut", "hazelnut", "pecan", "pine nut", "walnut", "acorn",
    "barley", "corn", "rice", "sorghum", "wheat", "oats", "quinoa", "millet", "spelt",
    "flaxseed", "chia", "pumpkin seed", "sunflower seed", "sesame", "peanut", "soybean",
    "tofu", "tempeh", "seitan", "pasta", "bread", "bagel", "croissant", "biscuit", "cake",
    "cookie", "brownie", "cupcake", "doughnut", "muffin", "pie", "pudding", "scone",
    "tart", "waffle", "pancake", "cereal", "granola", "yogurt", "milk", "cheese",
    "butter", "cream", "sour cream", "ice cream", "sorbet", "custard", "gelato",
    "cabbage", "spinach", "arugula", "lettuce", "cucumber", "zucchini", "eggplant",
    "radish", "bell pepper", "chili pepper", "green bean", "asparagus", "broccoli",
    "cauliflower", "mushroom", "potato", "sweet potato", "pumpkin", "carrot", "onion",
    "garlic", "ginger", "turmeric", "basil", "parsley", "cilantro", "thyme", "oregano",
    "rosemary", "sage", "pepper", "salt", "vinegar", "oil", "mustard", "ketchup",
    "mayonnaise", "hot sauce", "soy sauce", "bbq sauce", "teriyaki", "honey", "syrup",
    "maple", "jam", "jelly", "spread", "chocolate", "vanilla", "cinnamon", "nutmeg"]

print(words[-1])

#list slycing

list = [30, 32, 39, 88]
print(list[1:3]) 
print(list[1:-1])

#update a list

science = ["art", "chemistry", "math"]

science[0] = "Biology"
print(science)

science[2] = "Geology"
print(science)

integers = [3, 6, 9, 12, 15]

integers[-1] = 90.3

print(integers)

#remove
integers.remove(6)

print(integers)

#pop
integers.pop(3)
print(integers)

list_fruits = ["mandarine", "strawberry", "bannana", "grape", "blueberry"]

#del
del list_fruits[2]
print(list_fruits)

list_names = ["Gabriel", "Edgar", "Isai"]
list_names.append("George")
print(list_names)

names2 = ["Sam", "Mateo", "David"]
print(names2.index("Sam"))
print(names2.index("David"))

my_list = ["a", "b", "c", "d"]

print(my_list.index("c"))

#squares
list_of_squares = []
for int in range (1,10):
    square =  int**2
    list_of_squares.append(square)
    
    print(list_of_squares)
    
#list comprehension
#[expression for item in list if condition]

squared2 = [item**2 for item in range(1,10)]
print(squared2)

numbers = [1,2,3,4,5,6,7,8,9]

for number in numbers: 
    print(number**3)
    
    cubic = [numbers**3 for number in numbers]
    print(cubic)
    
    #double the value of the numbers
    
    
    

    
        
        