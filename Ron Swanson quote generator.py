import random

quotes = [
    "There’s only one thing I hate more than lying: skim milk. Which is water that’s lying about being milk.",
    "The less I know about other people’s affairs, the happier I am. I’m not interested in caring about people. I once worked with a guy for three years and never learned his name. Best friend I ever had. We still never talk sometimes.",
    "Dear frozen yogurt, you are the celery of desserts. Be ice cream, or be nothing"
]

while True:
    print("Ron Swanson Quotes")
    print("1. Get a Funny Quote")
    print("2. Exit")
    
    choice = input("Enter your choice (1/2): ")
    
    if choice == '1':
        random_quote = random.choice(quotes)
        print("Random Quote:")
        print(random_quote)
    elif choice == '2':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1 to get a quote or 2 to exit.")