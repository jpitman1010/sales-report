"""Generate sales report showing total melons each salesperson sold."""


salespeople = []
melons_sold = []
# creating a blank list to input values into
f = open('sales-report.txt')
# opening file and assigning it to a variable to be used in the below for loop
for line in f:
    # using a for loop to remove begining and ending white spaces and then
    # turning the document with information into a list with each attribute 
    # separated by the | placed into a new index of the list. The list is called entries.
    # and will be used to iterate through to find values.
    line = line.rstrip()
    entries = line.split('|')

    salesperson = entries[0]
    # this is designating the etntries list just created at index 0 as being salesperson
    melons = int(entries[2])
    # number of melons, which is at the 3rd location on the entries list is assigned

    if salesperson in salespeople:
        # if statement to keep from repeating salespersons in the salespeople list
        # if they are in the list the index of the current salesperson is being found. 
        position = salespeople.index(salesperson)

        melons_sold[position] += melons
        # if salesperson is found in salespeople list, the list starting as an empty list
        # called melons_sold at the index identified as position above
    else:
        # if salesperson is not in the salespeople list the list is appended with the value of
        # the salesperson, then the melons_sold list is also appeneded with the integer melons
        salespeople.append(salesperson)
        melons_sold.append(melons)


for i in range(len(salespeople)):
    # iterating the salespeople list to have index value to allow print statements 
    # from both lists salespeople and melons.
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')


    # this process could better be done by defining a function that can be called
    # for multiple reports and future reports.  
    # it would be better to have a dictionary of values with the key values set equal to 
    # the variables (i.e. associating salespeopl as the keys and the values being the 
    # total amount sold and number of melons sold).
    # you could then either print the statement when the function is called or 
    # build another function specifically for printing out a report using the 
    # ability to call the function previously made.  