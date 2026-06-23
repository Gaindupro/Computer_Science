movies = {
    1: {"title": "Avatar: The Way of Water", "price": 1500.00, "seats": 50},
    2: {"title": "Avengers: Endgame", "price": 1500, "seats": 15},
    3: {"title": "Spider-Man: No Way Home", "price": 1250, "seats": 30},
    4: {"title": "Ranja Sinhala", "price": 1250, "seats": 40},
    5: {"title": "Top Gun: Maverick", "price": 1500, "seats": 20},
    6: {"title": "Jurassic World 2025", "price": 1500, "seats": 60},
    7: {"title": "OIC Gadafi ", "price": 1000, "seats": 5},
    8: {"title": "Suura Detuwo", "price": 1000, "seats": 60}
    
}
#comment
receipt_items = []
total_amount_to_pay = 0.0

print("------------------------------------")
print("  WELCOME TO Gaiya's Film House  ")
print("------------------------------------")

username = input("Please enter your username to log in: ")
password = input("Please enter your password: ")

print(f"\nLogin successful! Welcome back, {username}!\n")

while True:
    
    print("\n--------------------------------------------------")
    print("NOW SHOWING:")
    for key, movie_data in movies.items():
        print(f"[{key}] {movie_data['title']} | Price: LKR{movie_data['price']:.2f} | Available Seats: {movie_data['seats']}")
    print("--------------------------------------------------")
    
    try:
        movie_choice = int(input("\nEnter the number of the movie you want to watch: "))
    except ValueError:
        print("Error: Please enter a valid number.")
        continue 
        
    if movie_choice in movies:
        selected_movie = movies[movie_choice]
        
        try:
            tickets_needed = int(input(f"How many tickets for '{selected_movie['title']}'? "))
        except ValueError:
            print("Error: Please enter a valid number of tickets.")
            continue
            
        
        if tickets_needed <= 0:
            print("You must buy at least 1 ticket.")
        elif tickets_needed <= selected_movie['seats']:
            
            cost = tickets_needed * selected_movie['price']
            
            
            movies[movie_choice]['seats'] -= tickets_needed
            
            
            total_amount_to_pay +=cost
            
          
            receipt_items.append({
                "movie_name": selected_movie['title'],
                "ticket_count": tickets_needed,
                "total_cost": cost
            })
            
            print(f"\nSUCCESS! {tickets_needed} ticket(s) added to your cart for LKR{cost:.2f}.")
        else:
            print(f"\nSorry, we only have {selected_movie['seats']} seats left for that movie.")
    else:
        print("\nInvalid movie choice. Please try again.")

    
    print("\n--------------------------------------------------")
    print("What would you like to do next?")
    print("[1] Book another movie")
    print("[2] View Receipt")
    
    next_action = input("Enter your choice (1 or 2): ")
    
    if next_action == '2':
        
        print("\n\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
        print("      ______YOUR TICKET/RECEIPT_____         ")
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
        print(f"Customer: {username}\n")

        if len(receipt_items) == 0:
            print("You did not book any tickets.")
        else:
            for item in receipt_items:
                print(f"Movie: {item['movie_name']}")
                print(f"Tickets: {item['ticket_count']}")
                print(f"Subtotal: LKR{item['total_cost']:.2f}")
                
                print("------------------------------------")
            
            
            print(f"GRAND TOTAL: LKR{total_amount_to_pay:.2f}")
        
     
        print("\n====================================")
        print("Would you like to:")
        print("[1] Go back to Movies Menu")
        print("[2] Exit Application")
        post_receipt = input("Enter your choice (1 or 2): ")
        
        if post_receipt == '2':
            print("\nThank you for choosing Gaiya's Film House!")
            print(f"Your ticket Refarance - ID20081204")
            print("Enjoy your show!")
            print("====================================\n")
            break 
