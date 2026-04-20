def divide_numbers(a: str, b: str) -> None:
    
    try:
        val_a = int(a)
        val_b = int(b)
        print(val_a / val_b)

    except Exception as error:
        print("An error occurred:", error)



# do not modify below this line
divide_numbers("10", "2")
divide_numbers("12", "0")
divide_numbers("2", "not a number")