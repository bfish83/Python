# Barret Fisher
# barret.fisher@uky.edu
# CS115 Section 5
# 11-19-12
# Program 4: Search engine
# Purpose: Search database file to find URL's that match user search, and output
#           results to webpage, and record data in secret file
# Preconditions: Inputs from user(name, database, search, case setting, webpage)
# Postconditions: Number of hits output, webpage created, name and search added
#                   to secret file


# secret
# Purpose: open secret.txt and output to secret.txt userids and searches
# Preconditions: Parameters userid, search
# Postconditions: outputs to secret.txt userids and searches
def secret(name, search):
    outfile = open("secret.txt", "a")
    print(name, file=outfile)
    print(search, file=outfile)
    outfile.close()


# outputline
# Purpose: To output to html file search hits with URL and hits bolded
# Preconditions: hits, database keywords, URL with keywords,
#                   search phrase, outputfile
# Postconditions: HTML file has table created/appended
def outputline(hits, tags, url, search, outfile):
    if hits == 1:
        print("<p align=center>", file=outfile)
        print("<table border>", file=outfile)
        print("<tr><th>Hit<th>URL</tr>", file=outfile)
    print("<tr><td>", file=outfile)
    tags = tags.replace(search, "<b>"+search+"</b>")
    print(tags, file=outfile)
    print("<td><a href=\"", url, "\" align=center>", url, "</a></tr>", file=outfile)




def main():

    # get user inputs
    print("Big Blue Search Engine")
    name = input("Your user name? ")
    data = input("Enter name of database file (.txt will be added): ")
    search = input("Keyword string to search for: ")
    results = input("Enter name for web page of results (extension of .htm will be added): ")
    case = input("Do you want search to be case sensitive? (y or n) ")

    # append name/search to secret file
    secret(name, search)

    # check database file
    temp = data + ".txt"
    try:
        infile = open(temp, "r")
    except IOError:
        print("Cannot open", temp)
        return
    data = infile.readlines()
    infile.close()

    # create output html file
    temp = results + ".htm"
    outfile = open(temp, "w")
    print(temp, "created")
    print("<html>", file=outfile)
    print("<title>Search Findings</title>", file=outfile)
    print("<body>", file=outfile)

    # make lowercase if user specified, put appropriate header on page
    if case != "y":
        search = search.lower()
        data = [i.lower() for i in data]
        print("<h2><p align=center>Search for \"", search, "\"</h2>", sep="", file=outfile)
    else:
        print("<h2><p align=center>Case Sensitive Search for \"", search, "\"</h2>", sep="", file=outfile)

    # call outputline function for every search hit
    hits = 0
    for i in range(0, len(data), 2):
        if search in data[i]:
            hits += 1
            outputline(hits, data[i], data[i + 1], search, outfile)

    # if no hits (finish and close file)
    if hits == 0:
        print("0 hits")
        print("<p align=center>", file=outfile)
        print("<table border>", file=outfile)
        print("<tr><td>", search, "<td> not found! </tr>", file=outfile)
        print("</table>", file=outfile)
        print("</body>", file=outfile)
        print("</html>", file=outfile)
        outfile.close()

    # if hits (finish and close file)
    else:
        print(hits, "hit(s)")
        print("</table>", file=outfile)
        print("</body>", file=outfile)
        print("</html>", file=outfile)
        outfile.close()
    
main()
