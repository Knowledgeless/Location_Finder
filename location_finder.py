
#######################################################
#   If you got any unknown error which one I didn't   #
#   controled in the script, Please let me know.      #
#   Author: knowledgeless                             # 
#   Github: https://github.com/knowledgeless           #
#######################################################

try:
    import reverse_geocoder as rc 
    import pprint
    import os

    #os.system("sh install.sh")

    def locator():
        lat = float(input("\nLattitude : "))
        lon = float(input("ongitude : "))
        locations = (lat, lon)
        location = rc.search(locations)
        print("\n")
        #pprint.pprint(location)
        
        for i in reversed(location):
            for j in i.items():
                print(j)
        print("\n")

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
