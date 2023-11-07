## Lógica de um tradutor para girafês do curso Learn Python - Full Course for Beginners [Tutorial]

def translate(phrase):
    translation = ""
    
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else:
            translation = translation + letter
    
    return translation

print(translate("I love Barbara"))
