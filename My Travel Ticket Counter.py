passenger_name = "Sakshi"        
destination = "Canada"             
ticket_price = 80500.50           
number_of_tickets = 2          
is_available = True            
 
print("Passenger Name:", passenger_name)
print("Destination:", destination)
print("Ticket Price: Rs", ticket_price)
print("Number of Tickets:", number_of_tickets)
print("Tickets Available?", is_available)
 
print(type(passenger_name))
print(type(destination))
print(type(ticket_price))
print(type(number_of_tickets))
print(type(is_available))

 
total_cost = ticket_price * number_of_tickets
discount = 100
final_cost = total_cost - discount
 
print("\nTotal Cost: Rs", total_cost)
print("Discount: Rs", discount)
print("Final Cost: Rs", final_cost)
 
print("Double Ticket Price: Rs", ticket_price * 2)
print("Ticket Price After Rs50 Increase: Rs", ticket_price + 50)
print("Half Ticket Price: Rs", ticket_price / 2)
 

print("\nIs ticket price under Rs100000?", ticket_price < 100000)
print("Are more than 1 tickets booked?", number_of_tickets > 1)
print("Is destination Canada?", destination == "Canada")
print("Is final cost more than Rs120000?", final_cost > 120000)
 
 
travel_message = passenger_name + " is travelling to " + destination + "."
print("\nTravel Message:", travel_message)
 
print("Destination in uppercase:", destination.upper())
print("Passenger name in lowercase:", passenger_name.lower())
print("First letter of destination:", destination[0])
print("Length of passenger name:", len(passenger_name))

 
direct_ticket_price = 90000
indirect_ticket_price = 80500
 
print("\nBefore Swapping:")
print("Direct Ticket Price: Rs", direct_ticket_price)
print("Indirect Ticket Price: Rs", indirect_ticket_price)
 
direct_ticket_price,indirect_ticket_price = indirect_ticket_price, direct_ticket_price
 
print("\nAfter Swapping:")
print("Direct Ticket Price: Rs", direct_ticket_price )
print("Indirect Ticket Price: Rs", indirect_ticket_price)

 
print("\n================================")
print("TRAVEL TICKET SUMMARY")
print("================================")
print("Passenger:", passenger_name)
print("Destination:", destination)
print("Tickets Booked:", number_of_tickets)
print("Final Amount to Pay: Rs", final_cost)
print("Booking Confirmed?", is_available)