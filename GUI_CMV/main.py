import customtkinter as ctk
from GUI import CMV_PROJECT_GUI

with open('data.csv', 'w') as file:
    file.truncate()

if __name__ == "__main__":
    root = ctk.CTk()
    app = CMV_PROJECT_GUI(root)
    root.mainloop()        