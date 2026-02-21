# ============================================================================
# formulario2.py - Registro de Estudiantes
# Framework: Flet 0.80.5
# Descripción: Formulario de registro que recopila datos de estudiantes
#              y los muestra en una ventana emergente (overlay) al enviar.
# ============================================================================
import flet as ft

def main(page: ft.Page):
    """
    Función principal de la aplicación.
    Recibe el objeto 'page' que representa la ventana/pestaña del navegador.
    Aquí se configuran las propiedades de la página y se construye toda la interfaz.
    """

    # ========================================================================
    # SECCIÓN 1: CONFIGURACIÓN DE LA PÁGINA (Subtema 1.1 - Interfaces gráficas)
    # Estas propiedades definen la apariencia general de la ventana.
    # ========================================================================
    page.title = "Registro de Estudiantes - Tópicos Avanzados"
    page.bgcolor = "#FDFBE3"            # Color de fondo crema
    page.padding = 30                    # Margen interno de la página (px)
    page.theme_mode = ft.ThemeMode.LIGHT # Tema claro

    # ========================================================================
    # SECCIÓN 2: CONTROLES DE ENTRADA (Subtema 1.4 - Controles de entrada)
    # Cada control captura un dato del estudiante.
    # ========================================================================

    # --- 2.1 Campos de texto (TextField) ---
    # TextField: campo de texto libre donde el usuario escribe.
    # Parámetros clave:
    #   label       → texto que aparece como placeholder/etiqueta
    #   border_color→ color del borde del campo
    #   expand      → True = ocupa todo el ancho disponible
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
    # Dropdown: lista de opciones predefinidas para seleccionar una.
    # Parámetros clave:
    #   options → lista de ft.dropdown.Option con los valores seleccionables
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
        # Genera opciones del 1 al 6 automáticamente con list comprehension
        options=[ft.dropdown.Option(str(i)) for i in range(1, 7)]
    )

    # Campos auxiliares (no se usan en la interfaz actual, reservados para futuro)
    txt_carrera = ft.TextField(label="Carrera", expand=True, border_color="#4D2A32")
    txt_semestre = ft.TextField(label="Semestre", expand=True, border_color="#4D2A32")

    # --- 2.3 Botones de radio (RadioGroup + Radio) ---
    # RadioGroup: agrupa botones de radio para que solo uno pueda estar seleccionado.
    # Radio: cada opción individual dentro del grupo.
    # Parámetros clave:
    #   value      → valor que se almacena al seleccionar esta opción
    #   label      → texto visible junto al botón
    #   fill_color → color del botón cuando está seleccionado
    rg_genero = ft.RadioGroup(content=ft.Row([
        ft.Radio(value="masculino", label="Masculino", fill_color="#4D2A32"),
        ft.Radio(value="femenino", label="Femenino", fill_color="#4D2A32")
    ]))

    # Row para mostrar la etiqueta "Genero:" junto a los radio buttons
    row_genero = ft.Row([
        ft.Text("Genero:", color="#4D2A32", weight=ft.FontWeight.BOLD, size=16),
        rg_genero
    ], alignment=ft.MainAxisAlignment.START)

    # ========================================================================
    # SECCIÓN 3: MANEJO DE EVENTOS (Subtema 1.5 - Eventos)
    # Función que se ejecuta cuando el usuario presiona el botón "Enviar".
    # Recopila los datos y muestra una ventana emergente (overlay).
    # ========================================================================
    # Texto de error para el radio group de género (inicialmente oculto)
    txt_error_genero = ft.Text("", color="red", size=12, visible=False)

    # Se inserta el texto de error debajo de la fila de género
    row_genero_con_error = ft.Column([row_genero, txt_error_genero], spacing=2)

    def validar_campos():
        """
        Valida todos los campos del formulario.
        - Campos vacíos se marcan con borde rojo y texto de ayuda.
        - El email debe contener '@'.
        - El radio group muestra un mensaje de error si no se selecciona.
        Retorna True si todo es válido, False en caso contrario.
        """
        es_valido = True
        COLOR_ERROR = "red"
        COLOR_NORMAL = "#4D2A32"

        # --- Validar nombre ---
        if txt_nombre.value is None or txt_nombre.value.strip() == "":
            txt_nombre.border_color = COLOR_ERROR
            txt_error_nombre.value = "Ingresa tu nombre"
            txt_error_nombre.visible = True
            es_valido = False
        else:
            txt_nombre.border_color = COLOR_NORMAL
            txt_error_nombre.value = ""
            txt_error_nombre.visible = False

        # --- Validar número de control ---
        if txt_control.value is None or txt_control.value.strip() == "":
            txt_control.border_color = COLOR_ERROR
            txt_error_control.value = "Ingresa tu número de control"
            txt_error_control.visible = True
            es_valido = False
        else:
            txt_control.border_color = COLOR_NORMAL
            txt_error_control.value = ""
            txt_error_control.visible = False

        # --- Validar email ---
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
            txt_error_email.value = ""
            txt_error_email.visible = False

        # --- Validar carrera (dropdown) ---
        if not dd_carrera.value:
            dd_carrera.border_color = COLOR_ERROR
            dd_carrera.error_text = "Selecciona una opción"
            es_valido = False
        else:
            dd_carrera.border_color = COLOR_NORMAL
            dd_carrera.error_text = None

        # --- Validar semestre (dropdown) ---
        if not dd_semestre.value:
            dd_semestre.border_color = COLOR_ERROR
            dd_semestre.error_text = "Selecciona una opción"
            es_valido = False
        else:
            dd_semestre.border_color = COLOR_NORMAL
            dd_semestre.error_text = None

        # --- Validar género (radio group) ---
        if not rg_genero.value:
            txt_error_genero.value = "Selecciona una opción"
            txt_error_genero.visible = True
            es_valido = False
        else:
            txt_error_genero.value = ""
            txt_error_genero.visible = False

        return es_valido

    def enviar_datos(e):
        """
        Evento on_click del botón Enviar.
        1. Valida los campos del formulario.
        2. Si hay errores, marca los campos en rojo y muestra mensajes.
        3. Si todo es válido, muestra la ventana emergente con los datos.
        """
        # Paso 1: Validar todos los campos
        if not validar_campos():
            page.update()  # Actualizar para mostrar los errores visuales
            return  # Detener si hay errores

        # Paso 2: Recopilar valores (ya validados, no necesitan valor por defecto)
        nombre = txt_nombre.value.strip()
        control = txt_control.value.strip()
        email = txt_email.value.strip()
        carrera = dd_carrera.value
        semestre = dd_semestre.value
        genero = rg_genero.value

        # Función interna para cerrar la ventana emergente
        def cerrar_dialogo(e):
            """Cierra el diálogo y lo remueve de la página."""
            dlg_datos.open = False
            page.update()

        # Paso 3: Construir la ventana emergente usando AlertDialog
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
            actions=[
                ft.TextButton("Cerrar", on_click=cerrar_dialogo),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )

        # Paso 4: Mostrar el diálogo en la página y actualizar
        page.dialog = dlg_datos
        dlg_datos.open = True
        page.update()

    # ========================================================================
    # SECCIÓN 4: BOTÓN DE ENVÍO
    # Botón que dispara el evento enviar_datos al hacer clic.
    # ========================================================================
    btn_enviar = ft.Button(
        content=ft.Text("Enviar", color="black", size=16),
        bgcolor=ft.Colors.GREY_500,       # Color de fondo gris
        width=page.width,                 # Ancho completo de la página
        on_click=enviar_datos,            # ← CONEXIÓN DEL EVENTO (Subtema 1.5)
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=0),  # Sin bordes redondeados
        )
    )

    # ========================================================================
    # SECCIÓN 5: CONSTRUCCIÓN DE LA INTERFAZ (Subtema 1.1 - Layout)
    # page.add() agrega los controles a la página en orden vertical (Column).
    # Row() organiza controles en una fila horizontal.
    # ========================================================================
    page.add(
        ft.Column([
            col_nombre,          # Campo de nombre + error
            col_control,         # Campo de número de control + error
            col_email,           # Campo de email + error
            ft.Row([             # Fila horizontal con dos dropdowns
                dd_carrera,      #   └── Dropdown de carrera
                dd_semestre      #   └── Dropdown de semestre
            ], spacing=10),
            row_genero_con_error, # Fila con radio buttons de género + error
            btn_enviar           # Botón de envío
        ], spacing=15)           # Espaciado vertical entre controles
    )

# ============================================================================
# PUNTO DE ENTRADA - Ejecuta la aplicación en el navegador web
# ft.app() inicia el servidor Flet y abre la app en una pestaña del navegador.
# ============================================================================
ft.app(target=main, view=ft.AppView.WEB_BROWSER)