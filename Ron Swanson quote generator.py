import random

ron_quotes = [
    "There’s only one thing I hate more than lying: skim milk. Which is water that’s lying about being milk.",
    "The less I know about other people’s affairs, the happier I am. I’m not interested in caring about people. I once worked with a guy for three years and never learned his name. Best friend I ever had. We still never talk sometimes.",
    "Dear frozen yogurt, you are the celery of desserts. Be ice cream, or be nothing"
]

april_quotes = [
    "Time is money, money is power, power is pizza, and pizza is knowledge.",
    "She's the cold, distant mother I never had... I love her.",
    "I wasn't listening, but I strongly disagree"
]

leslie_quotes = [
    "We have to remember what's important in life: friends, waffles and work. Or waffles, friends, work. But work has to come third.",
    "What I hear when I'm being yelled at is people caring really loudly at me.",
    "I would like a glass of red wine, and I'll take the cheapest one you have because I can't tell the difference."
]

while True:
    print("Parks and Rec Quotes")
    print("1. Ron Swanson Quotes")
    print("2. April Ludgate Quotes")
    print("3. Leslie Knope Quotes")
    print("4. Exit")
    
    choice = input("Enter your choice (1/2/3/4/5): ")
    
    if choice == '1':
        random_quote = random.choice(ron_quotes)
        print("Ron Quote:")
        print(random_quote)
    elif choice == '2':
        random_quote = random.choice(april_quotes)
        print("April Quote:")
        print(random_quote)
    elif choice == '3':
        random_quote = random.choice(leslie_quotes)
        print("Leslie Quote:")
        print(random_quote)
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2 or 3. Enter 4 to exit.")