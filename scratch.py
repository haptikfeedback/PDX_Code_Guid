# print("How old are you?", end='')
# age = input()
# print("How tall are you?", end='')
# height = input()
# print("How much do you weight?", end="")
# weight = input()
#
# print(f"So, you're {age} old, {height} tall and {weight} heavy.")

from sys import argv

script, user_name = argv
prompt = '>'

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("what kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice!
""")
