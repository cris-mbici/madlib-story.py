first_noun = input("Choose any noun: ")
first_adjective = input("Choose any adjective to describe your noun: ")
first_verb = input("Choose any verb: ")

second_noun = input("Choose any noun: ")
second_adjective = input("Choose any adjective to describe your noun: ")
second_verb = input("Choose any verb: ")

story = f"""
Once upon a time, there was a {first_adjective} {first_noun} who loved to {first_verb}
He loved {first_verb}ing so much that it annoyed {second_adjective} {second_noun} who loved {second_verb}ing
So they had a conversation to talk things through
{first_noun}: You call me {first_adjective} and say that I {first_verb} too much!
{second_noun}: Get off that high horse! You call me {second_adjective} and say that I love {second_verb}ing too much!
{first_noun}: Okay. I am {first_adjective} and you are {second_adjective}. Let's just do our own thing
{second_noun}: I'll keep {second_verb}ing and you keep {first_verb}ing.
{first_noun}: Good
Fin
"""

print(story)