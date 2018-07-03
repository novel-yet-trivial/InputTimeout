# TimedInput
A python module to add a timeout option to the input function. 

To use, download the zip file (big green button) and move the TimedInput folder in your project folder. Then add this to your code: 

    from TimedInput import timed_input as input

Now your input function has a timeout feature. Example program: 

    from TimedInput import timed_input as input

    correct_password = "password"
    user_says = input("You have 5 seconds to enter your password: ", timeout=5)
    if user_says == correct_password:
        print("Correct. You may enter.")
    elif user_says is None:
        print("You ran out of time!")
    else:
        print("Wrong password; access denied.")

If you do not specify a timeout, your input function will work like normal and wait forever. 
