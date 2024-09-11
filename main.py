import tkinter as tk
from tkinter import messagebox
import sympy as sp
import math

class CalculadoraCientifica:
    def __init__(self, root):
        """
        Constructor de la clase CalculadoraCientifica.
        
        Parámetro:
        - root: la ventana principal de la aplicación, proporcionada por tkinter.
        """
        self.root = root
        self.root.title("Calculadora Científica")
        self.root.geometry("550x500")  # Ajusta el tamaño de la ventana
        self.root.config(bg='#f0f0f0')  # Cambia el color de fondo de la ventana

        # Campo de entrada
        self.entrada = tk.Entry(root, width=40, borderwidth=5, font=("Arial", 18), bg='#ffffff', fg='#000000')
        self.entrada.grid(row=0, column=0, columnspan=5, padx=10, pady=10)  # Añade padding alrededor

        # Configuración de los botones
        botones = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('C', 1, 4),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('x^2', 2, 4),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('x^3', 3, 4),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3), ('sqrt', 4, 4),
            ('frac', 5, 0), ('sin', 5, 1), ('cos', 5, 2), ('tan', 5, 3), ('cot', 5, 4),
            ('(', 6, 0), (')', 6, 1), ('log', 6, 2), ('pi', 6, 3), ('e', 6, 4)
        ]

        for (texto, fila, col) in botones:
            boton_widget = tk.Button(root, text=texto, width=8, height=2, font=("Arial", 14), bg='#e0e0e0', fg='#000000',
                                    command=lambda t=texto: self.click(t))
            boton_widget.grid(row=fila, column=col, padx=5, pady=5)

    def click(self, texto):
        """
        Maneja el evento de clic en los botones de la calculadora.
        
        Parámetro:
        - texto: el texto del botón que fue presionado.
        """
        if texto == 'C':
            # Borra el contenido del campo de entrada
            self.entrada.delete(0, tk.END)
        elif texto == '=':
            try:
                # Obtiene la expresión del campo de entrada y la evalúa
                expresion = self.entrada.get()
                # Reemplaza operadores y funciones
                expresion = expresion.replace('^', '**')
                expresion = expresion.replace('frac', '/')
                expresion = expresion.replace('x^2', '**2')
                expresion = expresion.replace('x^3', '**3')
                expresion = expresion.replace('pi', str(math.pi))
                expresion = expresion.replace('e', str(math.e))

                resultado = sp.sympify(expresion)  # Convierte la expresión a un objeto simbólico de sympy
                resultado = resultado.evalf() if resultado.is_real else resultado  # Evalúa la expresión y muestra el resultado
                self.entrada.delete(0, tk.END)
                self.entrada.insert(0, str(resultado))  # Muestra el resultado en el campo de entrada
            except Exception as e:
                # Muestra un mensaje de error si la expresión no es válida
                messagebox.showerror("Error", "Entrada inválida")
        else:
            # Inserta el texto del botón en el campo de entrada
            self.entrada.insert(tk.END, texto)

# Código principal
if __name__ == "__main__":
    root = tk.Tk()  # Crea la ventana principal de la aplicación
    app = CalculadoraCientifica(root)  # Crea una instancia de la calculadora científica
    root.mainloop()  # Inicia el bucle principal de eventos de tkinter

"""
Guía Rápida para Usar `tkinter` y Otras Librerías

### `tkinter`:
- **¿Qué es `tkinter`?**
  `tkinter` es la biblioteca estándar de Python para la creación de interfaces gráficas de usuario (GUI). Permite crear ventanas, botones, entradas y otros widgets en aplicaciones de escritorio.

- **Métodos Importantes de `tkinter`:**
  - **Creación de la Ventana Principal:**
    ```python
    root = tk.Tk()  # Crea la ventana principal
    root.title("Título de la Ventana")  # Establece el título de la ventana
    root.geometry("AnchoxAlto")  # Establece el tamaño de la ventana
    root.config(bg="Color")  # Configura el color de fondo de la ventana
    ```

  - **Agregar Widgets:**
    - **Botón:**
      ```python
      boton = tk.Button(root, text="Texto", command=función, width=ancho, height=alto, bg="ColorFondo", fg="ColorTexto")
      boton.pack()  # O usa grid(row=fila, column=col) para una colocación más precisa
      ```

    - **Campo de Entrada:**
      ```python
      entrada = tk.Entry(root, width=ancho, font=("Fuente", tamaño), bg="ColorFondo", fg="ColorTexto")
      entrada.pack()  # O usa grid(row=fila, column=col)
      ```

    - **Campo de Texto:**
      ```python
      texto = tk.Text(root, width=ancho, height=alto, font=("Fuente", tamaño), bg="ColorFondo", fg="ColorTexto")
      texto.pack()  # O usa grid(row=fila, column=col)
      ```

  - **Organización de Widgets:**
    - **pack()**: Organiza los widgets en bloques verticales u horizontales.
    - **grid()**: Organiza los widgets en una cuadrícula.
    - **place()**: Organiza los widgets en ubicaciones absolutas.

  - **Eventos y Manejo de Clics:**
    ```python
    def mi_funcion():
        print("Botón presionado")
    
    boton = tk.Button(root, text="Haz clic", command=mi_funcion)
    ```

- **¿Qué es `sympy`?**
  `sympy` es una biblioteca de Python para matemáticas simbólicas. Permite manipular expresiones algebraicas de manera simbólica y resolver ecuaciones.

  - **Uso Básico:**
    ```python
    import sympy as sp
    expresion = sp.sympify('x^2 + 2*x + 1')  # Convierte una cadena a una expresión simbólica
    resultado = sp.solve(expresion, 'x')  # Resuelve la ecuación
    ```

- **¿Qué es `math`?**
  `math` es una biblioteca estándar de Python para operaciones matemáticas básicas y avanzadas, como funciones trigonométricas y constantes matemáticas.

  - **Uso Básico:**
    ```python
    import math
    resultado = math.sqrt(25)  # Calcula la raíz cuadrada de 25
    ```

### Añadir Más Funcionalidades:
1. **Agregar Más Botones:**
   - Amplía la lista `botones` con nuevas opciones. Asegúrate de añadir el texto y la ubicación deseada.

2. **Modificar Funcionalidades Existentes:**
   - Cambia la función `click` para manejar nuevas operaciones o funciones que desees incluir.

3. **Estilizar la Interfaz:**
   - Ajusta los estilos de los widgets modificando los parámetros en los métodos de creación de widgets. Cambia colores, fuentes, tamaños, etc.

4. **Uso de Funciones Avanzadas:**
   - Puedes usar funciones avanzadas de `sympy` para más cálculos matemáticos simbólicos o definir nuevas funciones y operaciones matemáticas.

Para aprender más sobre `tkinter` y las bibliotecas mencionadas, te recomiendo revisar la [documentación oficial de `tkinter`](https://docs.python.org/3/library/tkinter.html), [sympy](https://docs.sympy.org/latest/index.html), y [math](https://docs.python.org/3/library/math.html).
"""
