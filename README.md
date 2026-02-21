# Proyecto Integrador - Unidad 1: Desarrollo de Interfaces de Usuario

Este repositorio contiene la implementación completa y el análisis detallado del proyecto integrador de la Unidad 1. Se ha desarrollado una aplicación robusta utilizando el framework **Flet**.

## 🚀 Descripción del Proyecto
El objetivo es crear un formulario de registro de estudiantes que implementa validaciones de seguridad y una experiencia de usuario moderna.

---

## 📄 Código Completo (`formulario2.py`)

A continuación se presenta el código íntegro del programa:

```python
import flet as ft

def main(page: ft.Page):
    # Configuración de la página
    page.title = "Registro de Estudiantes - Tópicos Avanzados"
    page.bgcolor = "#FDFBE3"
    page.padding = 30
    page.theme_mode = ft.ThemeMode.LIGHT

    # --- 2.1 Campos de texto (TextField) ---
    txt_nombre = ft.TextField(label="Nombre", border_color="#4D2A32", expand=True, value="")
    txt_error_nombre = ft.Text("", color="red", size=12, visible=False)
    col_nombre = ft.Column([txt_nombre, txt_error_nombre], spacing=2)

    txt_control = ft.TextField(label="Numero de control", border_color="#4D2A32", expand=True, value="")
    txt_error_control = ft.Text("", color="red", size=12, visible=False)
    col_control = ft.Column([txt_control, txt_error_control], spacing=2)

    txt_email = ft.TextField(label="Email", border_color="#4D2A32", value="")
    txt_error_email = ft.Text("", color="red", size=12, visible=False)
    col_email = ft.Column([txt_email, txt_error_email], spacing=2)

    # --- 2.2 Listas desplegables (Dropdown) ---
    dd_carrera = ft.Dropdown(
        label="Carrera",
        expand=True,
        border_color="#4D2A32",
        options=[
            ft.dropdown.Option("Ingeniería en Sistemas"),
            ft.dropdown.Option("Ingeniería Civil"),
            ft.dropdown.Option("Ingeniería Industrial"),
        ]
    )

    dd_semestre = ft.Dropdown(
        label="Semestre",
        expand=True,
        border_color="#4D2A32",
        options=[ft.dropdown.Option(str(i)) for i in range(1, 7)]
    )

    # --- 2.3 Botones de radio (RadioGroup) ---
    rg_genero = ft.RadioGroup(content=ft.Row([
        ft.Radio(value="masculino", label="Masculino", fill_color="#4D2A32"),
        ft.Radio(value="femenino", label="Femenino", fill_color="#4D2A32")
    ]))

    row_genero = ft.Row([
        ft.Text("Genero:", color="#4D2A32", weight=ft.FontWeight.BOLD, size=16),
        rg_genero
    ], alignment=ft.MainAxisAlignment.START)

    txt_error_genero = ft.Text("", color="red", size=12, visible=False)
    row_genero_con_error = ft.Column([row_genero, txt_error_genero], spacing=2)

    # Lógica de Validación
    def validar_campos():
        es_valido = True
        COLOR_ERROR = "red"
        COLOR_NORMAL = "#4D2A32"

        if txt_nombre.value is None or txt_nombre.value.strip() == "":
            txt_nombre.border_color = COLOR_ERROR
            txt_error_nombre.value = "Ingresa tu nombre"
            txt_error_nombre.visible = True
            es_valido = False
        else:
            txt_nombre.border_color = COLOR_NORMAL
            txt_error_nombre.visible = False

        if txt_control.value is None or txt_control.value.strip() == "":
            txt_control.border_color = COLOR_ERROR
            txt_error_control.value = "Ingresa tu número de control"
            txt_error_control.visible = True
            es_valido = False
        else:
            txt_control.border_color = COLOR_NORMAL
            txt_error_control.visible = False

        if txt_email.value is None or txt_email.value.strip() == "":
            txt_email.border_color = COLOR_ERROR
            txt_error_email.value = "Ingresa tu correo electrónico"
            txt_error_email.visible = True
            es_valido = False
        elif "@" not in txt_email.value:
            txt_email.border_color = COLOR_ERROR
            txt_error_email.value = "Ingresa una dirección de correo válida"
            txt_error_email.visible = True
            es_valido = False
        else:
            txt_email.border_color = COLOR_NORMAL
            txt_error_email.visible = False

        if not dd_carrera.value:
            dd_carrera.border_color = COLOR_ERROR
            dd_carrera.error_text = "Selecciona una opción"
            es_valido = False
        else:
            dd_carrera.border_color = COLOR_NORMAL
            dd_carrera.error_text = None

        if not dd_semestre.value:
            dd_semestre.border_color = COLOR_ERROR
            dd_semestre.error_text = "Selecciona una opción"
            es_valido = False
        else:
            dd_semestre.border_color = COLOR_NORMAL
            dd_semestre.error_text = None

        if not rg_genero.value:
            txt_error_genero.value = "Selecciona una opción"
            txt_error_genero.visible = True
            es_valido = False
        else:
            txt_error_genero.visible = False

        return es_valido

    def enviar_datos(e):
        if not validar_campos():
            page.update()
            return

        nombre = txt_nombre.value.strip()
        control = txt_control.value.strip()
        email = txt_email.value.strip()
        carrera = dd_carrera.value
        semestre = dd_semestre.value
        genero = rg_genero.value

        def cerrar_dialogo(e):
            dlg_datos.open = False
            page.update()

        dlg_datos = ft.AlertDialog(
            title=ft.Text("Datos del Estudiante", weight=ft.FontWeight.BOLD, color="#4D2A32", size=20),
            content=ft.Column([
                ft.Divider(color="#4D2A32"),
                ft.Text(f"Nombre: {nombre}", size=15),
                ft.Text(f"Número de control: {control}", size=15),
                ft.Text(f"Email: {email}", size=15),
                ft.Text(f"Carrera: {carrera}", size=15),
                ft.Text(f"Semestre: {semestre}", size=15),
                ft.Text(f"Género: {genero}", size=15),
            ], tight=True, spacing=8),
            actions=[ft.TextButton("Cerrar", on_click=cerrar_dialogo)],
            actions_alignment=ft.MainAxisAlignment.END,
        )

        page.dialog = dlg_datos
        dlg_datos.open = True
        page.update()

    # Botón de envío
    btn_enviar = ft.Button(
        content=ft.Text("Enviar", color="black", size=16),
        bgcolor=ft.Colors.GREY_500,
        width=page.width,
        on_click=enviar_datos,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
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

---

## 🛠️ Explicación Detallada de los Componentes

### 1. Configuración de la Ventana (`page`)
En la función `main`, el objeto `page` representa la ventana de la aplicación.
*   **`page.title`**: Define el título en la barra del navegador.
*   **`page.bgcolor`**: Establece el fondo crema para una estética visual armoniosa.
*   **`page.theme_mode`**: Forzamos el tema claro para mantener la consistencia del diseño.

### 2. Controles de Entrada de Datos
*   **`ft.TextField` (Nombre, Control, Email)**: Son cajas de texto de una sola línea. Utilizamos la propiedad `label` para indicar qué dato se solicita.
    *   *Detalle técnico:* Se envuelven en un `ft.Column` junto a un `ft.Text` de error para que los mensajes aparezcan justo debajo del campo.
*   **`ft.Dropdown` (Carrera, Semestre)**: Listas desplegables con opciones predefinidas. El semestre se genera usando `range(1, 7)` para evitar repetición de código.
*   **`ft.RadioGroup` (Género)**: Agrupa controles `ft.Radio` asegurando que el usuario solo elija "Masculino" o "Femenino". Se visualiza dentro de un `ft.Row` para alineación horizontal.

### 3. Sistema de Validación (`validar_campos`)
Esta función es el motor de seguridad del formulario:
*   **Validación de Entradas Vacías**: Se comprueba con `.strip()` que no existan campos solo con espacios. Si falta un dato, el borde del campo se vuelve rojo.
*   **Validación de Formato de Email**: Se utiliza una búsqueda de patrón simple (`@`) para validar que el correo tenga una estructura mínima aceptable.
*   **Reset de Errores**: Cada vez que se intenta enviar, la función limpia los estilos previos si el usuario ya corrigió la entrada.

### 4. Manejo de Eventos y Lógica de Negocio (`enviar_datos`)
*   Se activa con el método `on_click` del botón.
*   **AlertDialog (AlertDialog)**: Es el componente solicitado para mostrar resultados. Se configura como un diálogo modal que interrumpe la interacción hasta que el usuario lo cierra.
    *   Presenta un resumen estructurado utilizando `ft.Column` y `ft.Divider` para mayor legibilidad.

### 5. Layout y Estructura Visual
*   **`ft.Column`**: Organiza los elementos de arriba hacia abajo.
*   **`ft.Row`**: Organiza los elementos de izquierda a derecha (usado en los Dropdowns de Carrera/Semestre).

---

## 🛠️ Tecnologías y Requisitos
- **Framework:** Flet (Python)
- **Instalación:** `pip install flet`

---
**Desarrollado por:** IKERD11
**Materia:** Tópicos Avanzados de Programación
**Unidad:** 1
