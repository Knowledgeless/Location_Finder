
#######################################################
#   If you got any unknown error which one I didn't   #
#   controled in the script, Please let me know.      #
#   Author: knowledgeless                             # 
#   Github: http://github.com/knowledgeless           #
#######################################################

try:
    import reverse_geocoder as rc 
    import pprint
    import os

    os.system("sh install.sh")

    def locator():
        lat = float(input("\nEnter your lattitude co-ordinates: "))
        lon = float(input("Enter your longitude co-ordinates: "))
        locations = (lat, lon)
        location = rc.search(locations)
        print("\n")
        pprint.pprint(location)

    if __name__ == "__main__":
        locator()

except ModuleNotFoundError:
    print('''
        Install Essential Module First
        Run "bash install.sh"
        After that try this script again
    ''')
except KeyboardInterrupt:
    print("\n\n\tYou Killed The Process Manually\n")

except ValueError:
    print("\n\tYou Entered Wrong Value\n")
