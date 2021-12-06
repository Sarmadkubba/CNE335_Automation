# This is the template code for the CNA337 Final Project
#Sarmad Kubba
# Tamplit base code by Zachary Rubin , zrubin@rtc.edu
# totring TJ Dewey
# with corpration Rick Sturza
# CNA 335 Fall 2021

def print_program_info():
    # TODO - Change your name
    print("Server Automator v0.11 by Sarmad")

# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()
    # TODO - Create a Server object
    Ec2 = Server("13.58.111.80") 
    Eco = Ec2.ping()
    print(Eco)
    # TODO - Call Ping method and print the results
