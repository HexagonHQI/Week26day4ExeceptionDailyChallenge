def divide_numbers_with_bonus():
    try:
        
        num = int(input("Enter a number to divide 5: "))
        result = 5 / num  
    except ZeroDivisionError as e:
        print(f"Error: {e}. You cannot divide by zero!")
    except ValueError as e:
        print(f"Error: Invalid input. Please enter a valid number. {e}")
    except TypeError as e:
        print(f"Error: Type mismatch. {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    else:
        print(f"The result is: {result}")
    finally:
        print("Execution completed.")

# Call the function
divide_numbers_with_bonus()


#Not sure about this one 