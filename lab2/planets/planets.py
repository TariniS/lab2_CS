#Name: Tarini Srikanth
#Instructor: Turner-05
#Project: Lab 2
weightOnMars =0
weightOnJupiter=0
def weight_on_planets(userweight):
   # gathers the user weight from the user
   #sets 2 variables and multiplies them by the corresponding weight
   # sets 2 string variables equal to the string
   weightOnMars= userweight*0.38
   weightOnJupiter = userweight*2.34
   string1="\nOn Mars you would weigh"
   string2="\nOn Jupiter you would weigh"
   string3=  "pounds."
   # prints the strings along with the variables
   print(string1,weightOnMars,string3,string2,weightOnJupiter,"pounds.")

if __name__ == '__main__':
   weight=int(input("What do you weigh on earth? "))
   weight_on_planets(weight)

