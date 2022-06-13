import lexer

while True:
    text = input("Kandy >")
    output,error = lexer.run(text)
    print(error.print_string()) if error else print(output)