# This is the template code for the CNA337 Final Project
# Zachary Rubin, zrubin@rtc.edu
# CNE 335 Fall 2021
# Sarmad Kubba
# template base code by Zachary Rubin , zrubin@rtc.edu
# tutoring TJ Dewey
# with Cooperation Rick Sturza



from Server import Server
def print_program_info():
    # TODO - Change your name
    print("Server Automator v0.14 by SarmadKubba")

# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()
    # TODO - Create a Server object
    Ec2 = Server("3.144.196.8")
    # TODO - Call Ping method and print the results

    Echo = Ec2.ping()
    print(Echo)

    Ec2.update()
