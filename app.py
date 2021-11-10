# --- Model -----
class Model:
     
    def __init__(self) -> None:
        self.stock = self.Stock()
    
    def save_inputs(self, user_input: str):
        self.stock.stock_list.append(user_input)
        return True
    
    def modify_inputs(self,user_input: str) -> str:
        return user_input.upper()
        
    def write_file(self):     
        f = open("output.txt", "w")
        for line in self.stock.stock_list:     
            f.write(line + "\n")        
        f.close()
        return True
    
    class Stock:
        def __init__(self) -> None:
            self.stock_list = []
            
# ---- View -----
class View:
       
    def get_input(self):
        user_input = input("Please write something... ")
        if user_input == "":
            return 0
        return user_input

    def show_file_content(self):
        f = open("output.txt", "r")
        lines = f.readlines()
        print(" ## --- output.txt ---- ## ")
        for line in lines:
            print(line.strip())

# --- Controller ---- 
class Controller:
    
    def __init__(self, model, view) -> None:
        self.view = view
        self.model = model
        self.file_name = ""
        
    def manage_inputs(self):     
        for _ in range(2):
            # Tell the view to get inputs
            line = self.view.get_input()       
            if line == 0:
                raise ValueError("You must write something")  
            else: 
                # Put them in CAPS
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