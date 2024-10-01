class typhoon_directory:
    def __init__(self):
        self.directory = {
            "Agaton": ["MARCH", "95KPH"], 
            "Basyang": ["JULY", "130KPH"], 
            "Caloy": ["JULY", "65KPH"],
            "Domeng": ["AUGUST", "65KPH"],
            "Ester": ["AUGUST", "95KPH"],
            "Florita": ["AUGUST", "55KPH"],
            "Glenda": ["AUGUST", "175KPH"],
            "Henry": ["SEPTEMBER", "65KPH"],
            "Inday": ["SEPTEMBER", "195KPH"],
            "Juan": ["OCTOBER", "305KPH"]           
        }
    
    def month(self, typhoon_name):
        print(f"{typhoon_name} Month: {self.directory[typhoon_name][0]}")
    
    def speed(self, typhoon_name):
        print(f"{typhoon_name} Speed: {self.directory[typhoon_name][1]}")
    
    def add_typhoon(self, name, month, speed):
        self.directory[name] = [month, speed]
        print(f"Typhoon {name} with month {month} speed {speed} kph are addedddd to directoryyyyyy")
        
    def add_typhoon_from_input(self):
        name = input("Enter typhoon name: ")
        month = input("Enter typhoon month: ")
        speed = input("Enter typhoon speed: ")
        self.add_typhoon(name, month, speed)
    
    def view_all_typhoons(self):
        for name, details in self.directory.items():
            print(f"Typhoon {name}: Month - {details[0]}, Speed - {details[1]}")

Directory = typhoon_directory()
Directory.month("Basyang")
Directory.speed("Basyang")

Directory.add_typhoon_from_input()
print("\n")
print("\n")
print("============================================================================================================")
Directory.view_all_typhoons()
