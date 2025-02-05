instructions = (
    'calculate the average of many numbers:\n\n'
    '- you must input something\n'
    '- input a number and it will be added to the sum\n'
    '- input "done" and the program will finish (case insensitive)\n'
    '- input anything else and it will be ignored\n\n'
    'when you have finished inputting numbers, the average will be displayed'
)
print(instructions)

sum = 0
input_count = 0

still_entering_numbers = True
while still_entering_numbers:
    user_input = input('_')
    print('user_input:', type(user_input), user_input)

    if user_input == '' or user_input is None:
        print('nothing is not allowed')
        _  

    if user_input.lower() == 'done':
        still_entering_numbers = False
        _  

    try:
        next_number = float(user_input)
    except ValueError:
        print(f'"{user_input}" is not a number, it has been ignored')
        _  

    sum = _ 
    print('sum:', type(sum), sum)

    input_count = _  
    print('input_count:', type(input_count), input_count)

average = _  
print('average:', type(average), average)

average_message = 'the average of your numbers is: ' + str(average)
print(average_message)
