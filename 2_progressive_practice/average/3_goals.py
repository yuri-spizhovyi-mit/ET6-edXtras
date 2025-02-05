# #todo

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

while True:
    user_input = input('enter a number to add, or "done" to finish')

    if user_input == '':
        print('nothing is not allowed')
        continue

    # -- BEGIN: update sum and input_count if input is a number, exit if it is "done" -- 
    # -- END --

average = sum / input_count

average_message = 'the average of your numbers is: ' + str(average)
print(average_message)
