# Step 1
# Define class MyFirstClass
class MyFirstClass:
    print("Who wrote this?")

    # Step 2
    # Define string variable called index    
    index = "Author-Book"

    # Step 3
    # Define function hand_list()
    def hand_list(self,philosopher, book):

        #Step 4
        print(MyFirstClass.index)
        # variable + “ wrote the book: ” + variable
        print(philosopher + " wrote the book: " + book)       
        
#Step 5
# Call function handlist()

whodunnit = MyFirstClass()
whodunnit.hand_list("Sun Tzu", "The Art od War")