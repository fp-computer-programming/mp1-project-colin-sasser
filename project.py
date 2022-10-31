# Creator Cs 10/28/2022

#Create inputs for all blanks/Find sum of each possible answer: adj, noun, place, person, month, age
# Places: 5, w1, w5, w20, w24, w25
# Ages: 1, w2
# Nouns: 9, w3, w4, w8, w15, w17, w19, w21, w22, w23
# Adjectives : 6, w6, w7, w9, w10, w16, w18
# Months: 1, w12
# Persons: 3, w11, w13, w14

w1 = input("place")
w2 = input("age")
w3 = input("noun")
w4 = input("noun")
w5 = input("place")
w6 = input("adj")
w7 = input("adj")
w8 = input("noun")
w9 = input("adj")
w10 = input("adj")
w11 = input("person")
w12 = input("month")
w13 = input("person")
w14 = input("Person")
w15 = input("noun")
w16 = input("adj")
w17 = input("noun")
w18 = input("adj")
w19 = input("noun")
w20 = input("place")
w21 = input("noun")
w22 = input("noun")
w23 = input("noun")
w24 = input("place")
w25 = input("place")

#Write out mad lib,including all the inputs

madlib = """Inigo de Loyola was born in """+w1+""".
 He was """+w2+""" when he left """+w3+""".He eventually became a """+w4+""". 
 At the battle of """+w5+""" his leg was """+w6+""" by a 
cannon. During his """+w7+"""   recovery, He asked for many books about """+w8+""" but 
there werent any so he had to settle for books about Christianity. He found these books 
unexpededly """+w9+""". He also noticed something """+w10+""" happening to him. """+w11+"""
was working with him. In """+w12+""" of 1522, """+w13+""" was well enough to leave home 
with a newfound love for """+w14+""". He cast aside his life as a """+w15+""" and dressed himself
in """+w16+""" clothes and """+w17+""" to take up the life of a """+w18+""". He lived in a 
"""+w19+""" outside the town of """+w20+""". Ignatius began writing about the """+w21+"""
that took hold of him. It was here where he would work on what would become the 
"""+w22+""". Ignatius felt a calling to """+w23+""" but did not have the educational requirements.
To fill these requirements he had to go back to """+w24+""". Igantius continued his education at
"""+w25+""" """ 

# Check to make sure that no two variables are the same 
if w1 == w5 or w1 == w20 or w1 == w24 or w1 == w25:
    print("You can not use the same place more than once")
# Check to see no two nouns are the same 
if w3 == w4 or w3 == w8 or w3 == w15 or w3 == w17 or w3 == w19 or w3 == w21 or w3 == w22 or w3 == w23:
    print("you can not use the same noun more than once")
elif w4 == w3 or w4 == w8 or w4 == w15 or w4 == w17 or w4 == w19 or w4 == w21 or w4 == w22:
    print("You can not use the same noun more than once")
# Check to make sure no two adjectives are the same 


