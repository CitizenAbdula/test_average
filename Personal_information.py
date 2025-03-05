# Enter a loop to contain the entire program, and break if information is correct
while True:
    # INPUT (Prompt the user to enter their name)
    name = input('Enter your name: ')

    # INPUT (Prompt the user to enter their address with city, state, and ZIP)
    address = input('Enter your address with city, state, and ZIP: ')

    # INPUT (Prompt the user to enter their telephone number)
    num = int(input('Enter your telephone number: '))

    # INPUT (Prompt the user to enter their college major)
    college_major = input('Enter your college major: ')

    # OUTPUT (Display the information)
    print('\nPlease confirm your personal information')
    print(f'\nName: {name}')
    print(f'Address (City, State, ZIP): {address}')
    print(f'Telephone number: {num}')
    print(f'College Major: {college_major}')

    # INPUT (Ask if the information is correct)
    # User can use upper or lower case
    confirm = input('Is the information correct, (YES/NO): ').upper()

    # PROCESS (If it's correct, then we end the program, if not loop continues)
    if confirm == 'YES':
        print('\nThank you for sharing your data with us')
        break
    else:
        print('Re-enter your correct informtion\n')
