#Includes - 
      #Part 1 - Main Version
      #PART 2 - List [extension]
      #Part 3 - Text File (extension) 


#############Part 1 - Main Version

#Importing Graphics module
from graphics import *

#Initialize variables 
student_count = 0
progress_count = 0
trailer_count = 0
retriever_count = 0
exclude_count = 0

progression_list = [] ###List variable for progression outcome

#Function to get validation
def valid_credits(prompt):
    while True:
        try:
            credit = int(input(prompt))
            if credit in range(0,121,20):
                return credit
            else:
                print ("Out of range")
        except ValueError:
            print ("Integer required")
            

#Function to get the progression outcome
def process(pass_credits, defer_credits, fail_credits):
    global progress_count, trailer_count, retriever_count, exclude_count

    #Check if the total credits is 120
    total = pass_credits + defer_credits + fail_credits
    if total != 120:
        print ("Incorrect total")

    #Check the progression outcome
    else:
        if pass_credits == 120:
            print ("Progress")
            progress_count += 1  #Increment Progress count
            progression_list.append ([pass_credits, defer_credits, fail_credits])  ##Append the outcome to the progression_list
            
        elif pass_credits == 100:
            print ("Progress (module trailer)")
            trailer_count += 1  #Increment Progress module trailer count
            progression_list.append ([pass_credits, defer_credits, fail_credits])  ##Append the outcome to the progression_list
            
        elif fail_credits >= 80:
            print ("Exclude")
            exclude_count += 1  #Increment Exclude count
            progression_list.append ([pass_credits, defer_credits, fail_credits])  ##Append the outcome to the progression_list
            
        else:
            print ("Do not progress - module retriever")
            retriever_count += 1  #Increment module retriever count
            progression_list.append ([pass_credits, defer_credits, fail_credits])  ##Append the outcome to the progression_list

#Function to get multiple outcomes or view results
def continuation():
    global student_count
    while True:
        print ("Would you like to enter another set of data?")
        choice = input("Enter 'y' for yes or 'q' to quit and view results:").lower()
        print("\n")

        if choice == "y":
            student_count += 1 #Increment student count
            return True
            
        elif choice == "q":
            return False
        
        else:
            print ("Invalid choice. Please enter 'y' or 'q'.")

#Function to continuously prompt the user to enter Pass, defer, fail credits
def main_inputs():
    while True:
        pass_credits = valid_credits ("Please enter your total PASS credits:")
        defer_credits = valid_credits ("Please enter your total DEFER credits:")
        fail_credits = valid_credits ("Please enter your total FAIL credits:")
        process(pass_credits, defer_credits, fail_credits)
        print ("\n")    

        if not continuation():
            break
main_inputs()



############Graphical representation - Histogram
    
#Function to create a histogram
def histogram():
    #Creating the window
    win = GraphWin ("Histogram", 800, 600)
    win.setBackground ("MintCream")

    #Reference of the colors-
    #HTML color groups. Available at: https://www.w3schools.com/colors/colors_groups.asp (Accessed: 26 November 2023).

    #A Line below the histogram
    line = Line (Point(50, 500), Point(750, 500))
    line.setOutline("Dimgray")
    line.draw(win)

    #A Label for the histogram
    label = Text (Point(220, 35), "Histogram Results")
    label.setTextColor ("Dimgray")
    label.setStyle ("bold")
    label.setSize (20)
    label.draw(win)

    #Defining Histogram Parameters
    bar_width = 140
    bar_gap = 15
    max_count = max (progress_count, trailer_count, retriever_count, exclude_count)
    scale_factor = 400 / max_count

    #Function to draw bars in the histogram
    def bar_(category, count, color, margin):
        height = count * scale_factor
        point1 = Point(margin, 500)
        point2 = Point(margin + bar_width, 500 - height)
        bar = Rectangle (point1, point2)
        bar.setFill(color)
        bar.setOutline("DimGray")
        bar.draw(win)

        #Adding Text (count) above each bar
        text1 = Text (Point(margin + bar_width / 2, 500 - height-15), f"{count}")
        text1.setTextColor("SlateGray")
        text1.setSize (20)
        text1.setStyle ("bold")
        text1.draw(win)

        #Adding Text (category) below each bar
        text2 = Text (Point(margin + bar_width / 2, 520), f"{category}")
        text2.setTextColor ("SlateGray")
        text2.setSize (18)
        text2.setStyle ("bold")
        text2.draw(win)

    #Drawing bars for each category
    bar_("Progress", progress_count, "PaleGreen", 100)
    bar_("Trailer", trailer_count, "DarkSeaGreen", 100 + bar_width + bar_gap)
    bar_("Retriever", retriever_count, "OliveDrab", 100 + 2 * (bar_width + bar_gap))
    bar_("Excluded", exclude_count, "RosyBrown", 100 + 3 * (bar_width + bar_gap))

    #Adding Text (Total count) below the histogram
    text3 = Text (Point(240, 565), f"{student_count} outcomes in total.")
    text3.setTextColor ("SlateGray")
    text3.setSize (20)
    text3.setStyle ("bold")
    text3.draw(win)

    #Wait for a mouse click to end
    win.getMouse()
    win.close()
histogram()


############PART 2 - List [extension]

#Accessing the list to print in the given format
print("Part 2:")
for data in progression_list:
    #convert the data list to a string
    #Reference-
    #(2023)How to convert list to string: STRING to list - python program, Available at: https://www.mygreatlearning.com/blog/convert-list-to-string-python-program/#:~:text=Using%20Join%20Function,into%20a%20string%20using%20Python. (Accessed: 26 November 2023). 
    i = ', '.join(map(str, data))
    
    #Check conditions to add to the list
    if data[0] == 120:
        print ("Progress -", i)
        
    elif data[0] == 100:
        print ("Progress (module trailer) -", i)
        
    elif data[2] >= 80:
        print ("Exclude -", i)
        
    else:
        print ("Module retriever -", i)
print("\n")



############PART 3 -  Text File [extension]

#Saving inputed progression data to a text file
with open ("progression_data.txt","w") as f:
    for data in progression_list:
        i = ', '.join(map(str, data))

        if data[0] == 120:
            f.write("Progress - {i}\n")
            
        elif data[0] == 100:
           f.write("Progress (module trailer) - {i}\n")
            
        elif data[2] >= 80:
            f.write("Exclude - {i}\n")
            
        else:
            f.write("Module retriever - {i}\n")
       
#Accessing the text file and print        
print("Part 3:") 
with open("progression_data.txt", "r") as f:
     f_data = f.read()
     print(f_data)
    