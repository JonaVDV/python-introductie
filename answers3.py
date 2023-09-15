age_str = input('What is your age? ')
print(f'Your age is {age_str}')

options = {
    '4g': False,
    '5g': False,
    'wifi open': False,
}

answer = input(f'what is your preffered connection? ({"/".join(options.keys())}): ')
if (answer.lower() not in options.keys()):
    print(f'invalid option ({answer})')
else:
    options[answer.lower()] = True
    if (options['wifi open'] is True):
        print('this connection may not be secure')
        answer2 = input('are you sure you want to continue? (y/n): ')
        if (answer2.lower() == 'n'):
            options['wifi open'] = False
            print('connection aborted')
        else:
            print(f'you are connected via {answer.lower()}')
    else:
        print(f'you are connected via {answer.lower()}')