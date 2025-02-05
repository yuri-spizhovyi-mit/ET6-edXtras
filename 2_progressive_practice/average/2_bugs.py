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
while True:
    user_input = input('enter a number to add, or "done" to finish')

    if user_input == '' or user_input == 'null':
        print('nothing is not allowed')
        continue

    if user_input.lower() == 'done':
        still_entering_numbers = False
    else:
        try:
            next_number = float(user_input)
        except ValueError:
            print(f'"{user_input}" is not a number, it has been ignored')
            break  # Note: This will exit the loop entirely if a non-number is entered

        sum = sum + next_number
        input_count = input_count + 1

average = sum / input_count

average_message = 'the average of your numbers is: ' + str(average)
print(average_message)