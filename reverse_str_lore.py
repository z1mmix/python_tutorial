name = input()
def reversed_str (name:str):
  name=name.split()
  reversed_words=[word[::-1]for word in name]
  reversed_sentence="". join(reversed_words)
  return reversed_sentence
print(reversed_str(name=name))
import csv

FILENAME = "users.csv"

users = [
    ["Ur story", input()],


]

with open(FILENAME, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(users)

with open(FILENAME, "a", newline="") as file:
    user = ["U input",  input() ]
    writer = csv.writer(file)
    writer.writerow(user)
    import csv

FILENAME = "users.csv"
with open(FILENAME, "r", newline="") as file:
      reader = csv.reader(file)
      for row in reader:
            print(row[0], " - ", row[1])