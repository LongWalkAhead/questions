restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}
new_menu = {"beverages": {"sprite": 1.99, "Coke": 1.89}}
restaurant_menu.update(new_menu)

new_steak = {"Main Course": {"Steak": 17.99, "Salmon": 13.99}}
restaurant_menu.update(new_steak)

removing_Bruschetta = {"Starters": {"Soup": 5.99}}
restaurant_menu.update(removing_Bruschetta)
print(restaurant_menu)

import copy
service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}}






def opening_new_service_ticket():
    new_ticket = {"Ticket003": {"Customer": "John", "Issue": "None", "Status": "Open"}}
    service_tickets.update(new_ticket)
    print(service_tickets)
        
opening_new_service_ticket()





def updating_status_of_ticket():
    old_ticket = {"Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"}}
    updated_ticket = {"Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "closed"}}
    old_ticket.update(updated_ticket)
    print(old_ticket)
    


updating_status_of_ticket()











"""Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
Implement functions to:
Open a new service ticket.
Update the status of an existing ticket.
Display all tickets or filter by status.
Initialize with some sample tickets and include functionality for additional ticket entry."""