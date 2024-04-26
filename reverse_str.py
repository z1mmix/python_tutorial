name = "ya vahye kak tut samomy napisat"
def reversed_str (name:str):
  name=name.split()
  reversed_words=[word[::-1]for word in name]
  reversed_sentence="". join(reversed_words)
  return reversed_sentence
print(reversed_str(name=name))
