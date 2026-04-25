import tkinter as tk

class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora POO con Tkinter")
        self.geometry("300x400")
        self.resizable(False, False)

        self.expresion = ""
        self.text_input = tk.StringVar()

        
        self._crear_interfaz()

    def _crear_interfaz(self):
        
        pantalla = tk.Entry(self, textvariable=self.text_input, font=("Arial", 20), bd=10, insertwidth=2,
                            width=14, borderwidth=4, relief="ridge", justify="right")
        pantalla.grid(row=0, column=0, columnspan=4)

        botones = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
            ("C", 5, 0)
        ]

        for (texto, fila, columna) in botones:
            boton = tk.Button(self, text=texto, padx=20, pady=20, font=("Arial", 14),
                              command=lambda t=texto: self._click_boton(t))
            boton.grid(row=fila, column=columna, sticky="nsew")

    def _click_boton(self, valor):
        if valor == "C":
            self.expresion = ""
            self.text_input.set("")
        elif valor == "=":
            try:
                resultado = str(eval(self.expresion))
                self.text_input.set(resultado)
                self.expresion = resultado
            except Exception:
                self.text_input.set("Error")
                self.expresion = ""
        else:
            self.expresion += str(valor)
            self.text_input.set(self.expresion)


if __name__ == "__main__":
    app = Calculadora()
    app.mainloop()
