""" Stepping Down

  Stepper Variables change systematically,
    going through a series of values for control flow

  "Stepper" describes how you are using a variable
    this term is not a JavaScript thing
    it's a general programming concept


  fill in the loop condition and update the stepper variable
"""

print('-- begin --')

holiday = 'winter solstice'
message = ' days remaining until ' + holiday

# declare and assign the stepper variable
# this stepper counts down the days to a holiday
days_remaining = 14
while __:
    tweet = str(days_remaining) + message
    print(tweet)
    
    days_remaining = __  # Count down

final_tweet = 'today is ' + holiday + '!'
print(final_tweet)

assert days_remaining == 0, 'there are 0 days remaining'

print('-- end --')
