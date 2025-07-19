#Create an empty tuple
empty_tuple = ()
#Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
siblings = (["Alice", "Bob"], "Charlie", "Diana")
#Join brothers and sisters tuples and assign it to siblings
brothers = ("Bob", "Charlie")
sisters = ("Alice", "Diana")
siblings = brothers + sisters
#How many siblings do you have?
num_siblings = len(siblings)
#Modify the siblings tuple and add the name of your father and mother and assign it to family_members
father = "John"
mother = "Jane"
family_members = siblings + (father, mother)



