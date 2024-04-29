leet_dict = {"a:": "@",
    "A": "4",
    "B": "8",
    "b": "8",
    "E": "3",
    "e": "3",
    "I": "!",
    "i": "!",
    "L": "1",
    "l": "1",
    "O": "0",
    "o": "0",
    "S": "5",
    "s": "5"
}

def convert(text: str) -> str:
    for key, value in leet_dict.items():
        text = text.replace(key, value)
    
    return text


string = "Bippity Boppity Boo"

print(convert(string))
        