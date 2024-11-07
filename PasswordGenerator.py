import random as rand
import string

class UserInput:
    def __init__(self):
        """
        self.number_of_passwords = self.getNumOfPassword()
        self.length_of_password = self.getLengthOfPassword()
        """
        pass
        
    def getNumOfPassword(self):
        number_of_passwords = int(input("How many passwords would you like to generate: "))
        
        return number_of_passwords
        
    def getLengthOfPassword(self):
        length_of_password = int(input("Length of password: "))
        
        return length_of_password
        
    def getSaveFileRequest(self):
        yes_no = False
        while(True):
            yes_no = input("Would you like to save the generated passwords to a file? (1: YES, 2: NO): ")
            if yes_no in {"1", "YES", "Yes", "yes", "2", "NO", "No", "no"}:
                break
            else:
                continue
                
        if yes_no in {"1", "YES", "Yes", "yes"}:
            yes_no = True
        else:
            yes_no = false
            
        return yes_no
        
    def getFileName(self):
        file_name = input("Name of file: ")
        return file_name
        
class GeneratePasswords:
    def __init__(self):
        self.password_dict = {}
        
    
    
    def generatePassword(self, number_of_passwords, length_of_password):
        for i in range(1, number_of_passwords + 1):
            password = ""
            
                
            password = password.join(rand.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=length_of_password))
            self.password_dict[i] = password
        
        return self.password_dict
        
class SaveToFile:
    def __init__(self):
        pass
    
    def saveFile(self, file_name, password_dict):
        for i in range(0, len(password_dict)):
            with open(file_name, 'a') as file:
                password = password_dict[i+1] + "\n"
                file.write(password)
        
        print(f"Passwords saved to {file_name}")
            
class Main:
    def __init__(self):
        user_input = UserInput()
        generator = GeneratePasswords()
        save_file_class = SaveToFile()
        
        quantity =  user_input.getNumOfPassword()
        length = user_input.getLengthOfPassword()
        
        dictionary = generator.generatePassword(quantity, length)
        print(dictionary)
        
        save_file = user_input.getSaveFileRequest()
        name_of_file = ""
        if(save_file == True):
            name_of_file = user_input.getFileName() + ".txt"
            save_file_class.saveFile(name_of_file, dictionary)
    
if __name__ == "__main__":
    Main()
                    
