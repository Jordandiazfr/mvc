# --- Model -----
class Model:
    def __init__(self) -> None:
        self.inputs = []
    
    def save_inputs(self, user_input: str):
        self.inputs.append(user_input)
        return True
     # Les vilaines méthodes statiques, il faut faire attention à l'encapsulation
    @staticmethod
    def modify_inputs(user_input: str) -> str:
        return user_input.upper()
        
    def write_file(self):     
        f = open("output.txt", "w")
        for line in self.inputs:     
            f.write(line + "\n")        
        f.close()
        return True
    
# ---- View -----
class View: 
    # à quoi sert ton constructeur puisqu'il ne fait rien? 
    def __init__(self) -> None:
        pass
    @staticmethod
    def get_input():
        user_input = input("Please write something... ")
        if user_input == "":
            return 0
        return user_input
    
    @staticmethod
    def show_file_content():
        f = open("output.txt", "r")
        lines = f.readlines()
        for line in lines:
            if line != '\n':
                print(line)

# --- Controller ---- 
class Controller:
    # C'est une bonne idée
    def __init__(self, model, view) -> None:
        self.view = view
        self.model = model
    
    def manage_inputs(self):     
        for _ in range(2):
            # Tell the view to get inputs
         
            line = self.view.get_input()       
            if line == 0:
                raise ValueError("You must write something")  
            else: 
                # Put them mayus
                line_upper = self.model.modify_inputs(line)  
                
                # Tell the model to save the inputs
                self.model.save_inputs(line_upper) 
        return True
        

    def manage_textfile(self):
        if self.model.write_file():
            self.view.show_file_content()
    

if __name__ == "__main__":
    app =  Controller(view=View(), model=Model())
    if app.manage_inputs(): app.manage_textfile()
