service_tickets = {
    "1": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "2": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}
idtotal = len(service_tickets)


def open_ticket(ticket_id, customer_name, issue_description):
        if ticket_id not in service_tickets:
            service_tickets[ticket_id] = {"Customer": customer_name, "Issue": issue_description, "Status": "open"}
            print("Ticket {} opened successfully.".format(ticket_id))       # Trying to learn using format(), was kind of stalling on that.
        else:
            print("Ticket {} already exists.".format(ticket_id))

def update_status(ticket_id, new_status):
    if ticket_id in service_tickets:
        service_tickets[ticket_id]["Status"] = new_status.lower()           # Keep everything lowercase for easier searching.
        print("Status of Ticket {} updated to {}.".format(ticket_id, new_status.lower()))
    else:
        print("Ticket {} isn't in the dictionary.".format(ticket_id))


def display_tickets(status):
    if status != 'null':
            filtered_tickets = {ticket_id: ticket_info for ticket_id, ticket_info in service_tickets.items() if ticket_info["Status"].lower() == status}
            if filtered_tickets:        # Making sure that the dictionary isn't empty and DOES contain something with the searched status. ^^
                 print("Tickets with status '{}':".format(status))
                 for ticket_id, ticket_info in filtered_tickets.items():
                    print("--------------------")
                    print("Ticket ID:", ticket_id, "Customer:", ticket_info["Customer"],"Issue:", ticket_info["Issue"],"Status:", ticket_info["Status"])
            
            else:
                print("No tickets found with status '{}'.".format(status))
            print("--------------------")

    else:
            print("\nAll Tickets:")
            for ticket_id, ticket_info in service_tickets.items():
                print("--------------------")
                print("Ticket ID:", ticket_id, "Customer:", ticket_info["Customer"],"Issue:", ticket_info["Issue"],"Status:", ticket_info["Status"])
            print("--------------------")


print("Welcome to the Service Ticket Tracker.")
while True:

     print("\nMenu: \n1. Open a new service ticket \n2. Update the status of an existing ticket \n3. Display all tickets or filter by status\n4. Quit")
     try:
        choice = int(input("\nWhat would you like to do? Please enter the number of your action. "))

        if choice == 1:
            idtotal = idtotal + 1
            ticket_id_total = idtotal
            ticket_name = input("Please enter your name. ")
            ticket_issue = input("Please enter a description of your issue. ")
            open_ticket(ticket_id_total, ticket_name, ticket_issue)

        if choice == 2:
            if len(service_tickets) < 1:        # Don't let them update statuses in an empty dictionary
                print("\nThere's nothing in the dictionary.")
            else:
                while True:
                    try:
                        update_choice = int(input("Which ticket would you like to update? "))
                        if update_choice <= len(service_tickets):
                            update_status_name = input("What do you want to mark the ticket's status as? ")
                            update_status(update_choice, update_status_name)
                            break
                        else:
                            print( "That ticket is not in the dictionary.")
                    except ValueError:
                        print("Please enter a valid number. ")

        if choice == 3:
            if len(service_tickets) < 1:
                print("\nThere's nothing in the dictionary.")
            else:
                while True:
                    try:
                        filter_choice = input("Would you like to filter by status? Y or N. ").lower()
                        if filter_choice == 'y':
                            filter_option = input("What status would you like to filter by? ").lower()
                            if filter_option != 'null':
                                display_tickets(filter_option.lower())
                            else:
                                print("You cannot sort by null.")
                            break
                        else:
                            display_tickets('null')
                            break
                    except ValueError:
                        print("Please enter a valid choice. ")
                 

        if choice == 4:
          break

     except:
        print("Please enter a valid number. ")