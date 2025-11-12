import tkinter as tk #создание графических интерфейсов
import random
from PIL import Image, ImageTk


class SimpleKeygen: #организации кода генератора ключей
    def __init__(self, root): 
        self.root = root #ссылка на главное окно
        self.root.title("Key Generator")
        self.root.geometry("400x320")

        #фоновое изображение
        self.bg_image = Image.open("pic.jpg")
        self.bg_image = self.bg_image.resize((1920, 1080), Image.Resampling.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
            
        #фон
        self.background_label = tk.Label(root, image=self.bg_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
            

        self.letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.digits = "0123456789"
        
        self.create_widgets() #метод создания элементов интерфейса
    
    def create_widgets(self):
        #заголовок с белым фоном
        title_label = tk.Label(self.root, text="KEY GENERATOR", 
                              font=("Arial", 16, "bold"),
                              bg="white", relief="solid", bd=1)
        title_label.pack(pady=20)
        
        #кнопка генерации
        generate_btn = tk.Button(self.root, text="GENERATE KEY", command=self.generate_key, 
                               bg="lightblue", font=("Arial", 12), padx=20, pady=10)
        generate_btn.pack(pady=20)
        
        #поле для отображения ключа
        self.key_display = tk.Entry(self.root, width=25, font=("Courier", 14, "bold"), 
                                  justify='center', state='readonly', bg="white")
        self.key_display.pack(pady=20)
        
        #кнопка копирования
        copy_btn = tk.Button(self.root, text="COPY KEY", command=self.copy_key, 
                           bg="lightgreen")
        copy_btn.pack(pady=10)
        
        #статус с фоном
        self.status_label = tk.Label(self.root, text="Click GENERATE to create key", 
                                   fg="black", bg="white")
        self.status_label.pack(pady=10)
    
    def generate_block(self):
        #2 случайные цифры + 3 случайные буквы
        two_digits = random.sample(self.digits, 2)
        three_letters = random.sample(self.letters, 3)
        
        all_chars = two_digits + three_letters
        random.shuffle(all_chars)
        
        return ''.join(all_chars)
    
    def generate_key(self):
        block1 = self.generate_block()
        block2 = self.generate_block()
        block3 = self.generate_block()
            
        full_key = f"{block1}-{block2}-{block3}"
            
        #вывод ключа
        self.key_display.config(state='normal')
        self.key_display.delete(0, tk.END)
        self.key_display.insert(0, full_key)
        self.key_display.config(state='readonly')
            
        self.status_label.config(text="Key generated!", fg="green")
            
    
    def copy_key(self):
        #копирование ключа
        key = self.key_display.get()
        self.root.clipboard_clear()
        self.root.clipboard_append(key)
        self.status_label.config(text="Copied to clipboard!", fg="blue")

if __name__ == "__main__": 
    root = tk.Tk()
    app = SimpleKeygen(root)
    root.mainloop()
