def remove_all_after(numbers, n):
     #If the element given isn't in the numbers' list then it will return back the original list
    if n not in numbers:
        return numbers
    else:
        #Else it will start finding the index of the first occurance of the element given
        index = numbers.index(n) + 1
        #This is to modify the list to include only elements up to and including the given element
        numbers = numbers[:index]
    #This returns the modified numbers' list    
    return numbers
   
while True:
    try:
        #This input will ask users to input a list of numbers separated by space and split() will split it into a list of strings and then convert each string to an integer to create a list of numbers
        numbers_input = input("Enter a list of numbers separated by space: ").split()
        #I assign an empty list to store the numbers
        numbers = []
        #This is to convert each number from string to integer adding it to the list
        for number in numbers_input:
            numbers.append(int(number))
        #This asks the user to input the border element
        n = int(input("Enter the border element: "))

        #This is to call the function and show the result
        print(f"Output: {remove_all_after(numbers, n)}")
        exit()
    except ValueError:
        print("Invalid input. Please enter a list of numbers separated by space and a border element.")
