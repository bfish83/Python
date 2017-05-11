# Barret Fisher
# barret.fisher@uky.edu
# CS115 Section 5
# 12-6-12
# Program 5
# Purpose: Process a file to add to a list of domain names/IP addresses 
# Preconditions: File of instructions
# Postconditions: Adds to (or creates) file with processed instructions



# get_dns_table
# Purpose: To read data into lists
# Preconditions: 2 lists to add to, dnsNames and ipAddresses
# Postconditions: Data from dnstable.txt is added to the lists
def get_dns_table(dnsNames,ipAddresses):
    try:
        infile = open("dnstable.txt", "r")
    except IOError:
        return
    rawdata = infile.read()
    infile.close()
    data = rawdata.split() #removes newline characters
    for i in range(0,len(data),2):
        dnsNames.append(data[i])
    for i in range(1,len(data),2):
        ipAddresses.append(data[i])
    print(len(dnsNames), "entries")
    print()


# selection_sort
# Purpose: to sort parrallel lists dnsNames and ipAddresses
# Preconditions: Length of dnsNames for control(n), and lists dnsNames and ipAddresses
# Postconditions: Sorted dnsNames alphabetically with ipAddresses sorted to match
def selection_sort(n,dnsNames,ipAddresses):
    if n > 1:
        for i in range(len(dnsNames)-1):
            if dnsNames[i+1] < dnsNames[i]:
                dnsTemp = dnsNames[i]
                ipTemp = ipAddresses[i]
                dnsNames[i] = dnsNames[i+1]
                ipAddresses[i] = ipAddresses[i+1]
                dnsNames[i+1] = dnsTemp
                ipAddresses[i+1] = ipTemp
        n -= 1
        # function will sort the list n times, enough to bring bottom item to top.
        selection_sort(n,dnsNames,ipAddresses)
    else:
        return


# dns_set
# Purpose: Adds to lists if not there, replaces if it is.
# Preconditions: Strings new DNS entry and IP, and lists dnsNames and ipAddresses
# Postconditions: Looks for new DNS entry, if there it replaces IP, if not it adds both
def dns_set(first,second,dnsNames,ipAddresses):
    print("Inserting", first, second)
    if first in dnsNames:
        location = dnsNames.index(first)
        print("Found", first, "Replacing", ipAddresses[location], "with", second)
        ipAddresses[location] = second
    else:
        dnsNames.append(first)
        ipAddresses.append(second)
        print("New Entry inserted")
    print("Number of entries now", len(dnsNames))
    print()


# dns_get
# Purpose: To print value corresponding to entry if it exists in lists
# Preconditions: entry to search for, and lists dnsNames/ipAddresses
# Postconditions: Prints value (DNS or IP) corresponding to entry if it exists
def dns_get(entry,dnsNames,ipAddresses):
    flag = False
    for i in entry:
        if i.isalpha() == True:
            flag = True
    if flag == True:
        if entry in dnsNames:
            location = dnsNames.index(entry)
            print("Lookup of", entry, "gives", ipAddresses[location])
        else:
            print("Lookup of", entry, "gives Not found")
    else:
        if entry in ipAddresses:
            location = ipAddresses.index(entry)
            print("Lookup of", entry, "gives", dnsNames[location])
        else:
            print("Lookup of", entry, "gives Not found")
    print()


# display_lists
# Purpose: To output to screen dns and ip addresses
# Preconditions: Lists dnsNames, ipAddresses
# Postconditions: Outputs lists to screen side by side, with DNS sorted alphabetically
def display_lists(dnsNames,ipAddresses):
    selection_sort(len(dnsNames),dnsNames,ipAddresses) #calls sort function
    print("----------------------------------------")
    print("IP Numbers", "Domain Names", sep="\t")
    for i in range(len(dnsNames)):
        print(ipAddresses[i], dnsNames[i], sep="\t")
    print("----------------------------------------")
    print()


# put_dns_table
# Purpose: Outputs new dns IP lists to dnstable.txt, overwriting it
# Preconditions: Lists dnsNames and ipAddresses
# Postconditions: Overwrites dnstable.txt with new info, sorted
def put_dns_table(dnsNames,ipAddresses):
    selection_sort(len(dnsNames),dnsNames,ipAddresses) #calls sort function
    outfile = open("dnstable.txt", "w")
    for i in range(len(dnsNames)):
        print(dnsNames[i], file=outfile)
        print(ipAddresses[i], file=outfile)
    outfile.close()



def main():
    print("CS 115 DNS Simulation")
    print()

    # creates empty lists for storing data
    dnsNames = []
    ipAddresses = []

    # adds to empty lists if dnstable.txt exists
    print("Reading dnstable.txt")    
    get_dns_table(dnsNames,ipAddresses)

    # get input from user
    instructions = input("Name of command file: ")
    print()
    try:
        infile = open(instructions, "r")
    except IOError:
        print("Cannot open file ", instructions, ". Are you sure it's typed correctly?", sep="")
        return
    rawRules = infile.readlines()
    infile.close()
    rules = []
    for i in range(len(rawRules)):
        rules.append(rawRules[i].strip()) #removes newline characters

    # main purpose of main function, processing instructions file
    entries = []
    for i in range(len(rules)):
        entries = rules[i].split() #separates each line into a list of its elements
        if entries[0] == "=":
            print("Processing SET")
            dns_set(entries[1],entries[2],dnsNames,ipAddresses) #call dns_set function
        elif entries[0] == "?":
            print("Processing GET")
            dns_get(entries[1],dnsNames,ipAddresses) #call dns_get function
        elif entries[0] == "*":
            print("Processing SHOW")
            display_lists(dnsNames,ipAddresses) #call display_lists function
        else:
            print("Error in command file", entries[0]) #notes instruction file error
            print()

    #outputs new data to file
    put_dns_table(dnsNames,ipAddresses)
    
main()
