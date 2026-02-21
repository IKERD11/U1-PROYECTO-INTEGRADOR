# Proyecto Integrador - Unidad 1: Desarrollo de Interfaces de Usuario

Este repositorio contiene la implementación completa y el análisis detallado del proyecto integrador de la Unidad 1. Se ha desarrollado una aplicación robusta utilizando el framework **Flet**.

## 🚀 Descripción del Proyecto
El objetivo es crear un formulario de registro de estudiantes que implementa validaciones de seguridad y una experiencia de usuario moderna.

---

## 🛠️ Explicación del Código por Secciones

A continuación, se desglosa el código de `formulario2.py` en sus secciones principales para explicar detalladamente su funcionamiento.

### 1. Importación y Punto de Entrada
Iniciamos importando la librería `flet` y definiendo la función `main`, que es el corazón de nuestra aplicación.

```python
import flet as ft

def main(page: ft.Page):
    # Configuración inicial de la página
    page.title = "Registro de Estudiantes - Tópicos Avanzados"
    page.bgcolor = "#FDFBE3"  # Color de fondo crema
    page.padding = 30
    page.theme_mode = ft.ThemeMode.LIGHT
```
*   **Análisis:** Definimos propiedades visuales básicas del contenedor principal (`page`), como el título, color de fondo y el margen interno.

### 2. Definición de Controles de Entrada
En esta sección se crean los componentes que interactuarán con el usuario.

```python
    # Campos de Texto (Nombre, Control, Email)
    txt_nombre = ft.TextField(label="Nombre", border_color="#4D2A32", expand=True, value="")
    txt_error_nombre = ft.Text("", color="red", size=12, visible=False)
    col_nombre = ft.Column([txt_nombre, txt_error_nombre], spacing=2)

    txt_control = ft.TextField(label="Numero de control", border_color="#4D2A32", expand=True, value="")
    txt_error_control = ft.Text("", color="red", size=12, visible=False)
    col_control = ft.Column([txt_control, txt_error_control], spacing=2)

    txt_email = ft.TextField(label="Email", border_color="#4D2A32", value="")
    txt_error_email = ft.Text("", color="red", size=12, visible=False)
    col_email = ft.Column([txt_email, txt_error_email], spacing=2)

    # Listas Desplegables (Carrera y Semestre)
    dd_carrera = ft.Dropdown(
        label="Carrera", expand=True, border_color="#4D2A32",
        options=[
            ft.dropdown.Option("Ingeniería en Sistemas"),
            ft.dropdown.Option("Ingeniería Civil"),
            ft.dropdown.Option("Ingeniería Industrial"),
        ]
    )

    dd_semestre = ft.Dropdown(
        label="Semestre", expand=True, border_color="#4D2A32",
        options=[ft.dropdown.Option(str(i)) for i in range(1, 7)]
    )

    # Botones de Radio (Género)
    rg_genero = ft.RadioGroup(content=ft.Row([
        ft.Radio(value="masculino", label="Masculino", fill_color="#4D2A32"),
        ft.Radio(value="femenino", label="Femenino", fill_color="#4D2A32")
    ]))
```
*   **Análisis:** Utilizamos `ft.TextField` para texto libre, `ft.Dropdown` para opciones cerradas y `ft.RadioGroup` para selecciones exclusivas. Cada campo de texto tiene asociado un `ft.Text` de error para mostrar validaciones visuales.

### 3. Lógica de Validación Integrada
Esta función interna se encarga de verificar que los datos cumplan con los requisitos del proyecto.

```python
    def validar_campos():
        es_valido = True
        # Validación de Nombre
        if txt_nombre.value is None or txt_nombre.value.strip() == "":
            txt_nombre.border_color = "red"
            txt_error_nombre.value = "Ingresa tu nombre"
            txt_error_nombre.visible = True
            es_valido = False
        else:
            txt_nombre.border_color = "#4D2A32"
            txt_error_nombre.visible = False

        # Validación de Email (Formato)
        if "@" not in txt_email.value:
            txt_email.border_color = "red"
            txt_error_email.value = "Ingresa una dirección de correo válida"
            txt_error_email.visible = True
            es_valido = False
        
        # ... (Validación similar para el resto de campos)
        return es_valido
```
*   **Análisis:** La función devuelve `False` si encuentra algún error y cambia dinámicamente el estilo visual de los componentes (borde rojo y visibilidad de etiquetas de error).

### 4. Procesamiento de Datos y Ventana Modal
Aquí es donde se capturan los datos finales y se presentan mediante un `AlertDialog`.

```python
    def enviar_datos(e):
        if not validar_campos():
            page.update()
            return

        # Captura de datos
        nombre = txt_nombre.value.strip()
        # ... (Captura del resto de variables)

        # Configuración del AlertDialog
        dlg_datos = ft.AlertDialog(
            title=ft.Text("Datos del Estudiante", weight=ft.FontWeight.BOLD),
            content=ft.Column([
                ft.Divider(),
                ft.Text(f"Nombre: {nombre}"),
                # ... (Visualización de datos capturados)
            ], tight=True),
            actions=[ft.TextButton("Cerrar", on_click=cerrar_dialogo)],
        )

        page.dialog = dlg_datos
        dlg_datos.open = True
        page.update()
```
*   **Análisis:** La función `enviar_datos` actúa como el controlador del formulario. Utiliza `ft.AlertDialog` para cumplir con el requisito de mostrar los datos en una ventana modal tras una validación exitosa.

### 5. Ensamblado de la Interfaz (Layout)
Finalmente, organizamos todos los componentes en la página.

```python
    btn_enviar = ft.Button(
        content=ft.Text("Enviar", color="black"),
        bgcolor=ft.Colors.GREY_500,
        on_click=enviar_datos
    )

    page.add(
        ft.Column([
            col_nombre,
            col_control,
            col_email,
            ft.Row([dd_carrera, dd_semestre], spacing=10),
            row_genero_con_error,
            btn_enviar
        ], spacing=15)
    )

ft.app(target=main, view=ft.AppView.WEB_BROWSER)
```
*   **Análisis:** Utilizamos `ft.Column` para apilar los elementos verticalmente y `ft.Row` para los controles que deben ir en la misma línea.

---

## 📦 Instalación y Ejecución
1. Instala las dependencias: `pip install -r requirements.txt`
2. Ejecuta el programa: `python formulario2.py`

---
**Desarrollado por:** IKERD11
**Materia:** Tópicos Avanzados de Programación
**Unidad:** 1
