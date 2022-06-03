import lexer

while True:
    text = input("Kandy >")
    output = lexer.run(text)
    print(output)