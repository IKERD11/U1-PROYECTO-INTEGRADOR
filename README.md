# 🎓 Proyecto Integrador - Unidad 1: Desarrollo de Interfaces de Usuario

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flet](https://img.shields.io/badge/Flet-0.80.5-00599C?style=for-the-badge&logo=flutter&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completado-success?style=for-the-badge)

Este repositorio alberga el **Proyecto Integrador de la Unidad 1**, enfocado en la creación de interfaces de usuario robustas, interactivas y validadas mediante el framework **Flet**. 

---

## 📋 Tabla de Contenidos
- [🚀 Descripción del Proyecto](#-descripción-del-proyecto)
- [🛠️ Arquitectura y Funcionamiento Detallado](#️-arquitectura-y-funcionamiento-detallado)
  - [1. Configuración de la Ventana](#1-configuración-de-la-ventana)
  - [2. Declaración de Controles (Componentes UI)](#2-declaración-de-controles-componentes-ui)
  - [3. Sistema de Validación Exhaustivo](#3-sistema-de-validación-exhaustivo)
  - [4. Procesamiento de Datos y AlertDialog](#4-procesamiento-de-datos-y-alertdialog)
- [📦 Instalación y Uso](#-instalación-y-uso)
- [✨ Funcionalidades Clave](#-funcionalidades-clave)

---

## 🚀 Descripción del Proyecto
La aplicación implementa un formulario de registro académico diseñado bajo principios de usabilidad y diseño limpio. Integra un motor de validación que garantiza que la información recogida sea veraz y completa, permitiendo al usuario visualizar sus datos en un modal profesional antes de finalizar.

---

## 🛠️ Arquitectura y Funcionamiento Detallado

A continuación, se presenta el código de `formulario2.py` desglosado por bloques técnicos con su explicación correspondiente.

### 1. Configuración de la Ventana
El punto de entrada configura el lienzo de la aplicación.

```python
import flet as ft

def main(page: ft.Page):
    # Propiedades de la página (Canvas principal)
    page.title = "Registro de Estudiantes - Tópicos Avanzados"
    page.bgcolor = "#FDFBE3"            # Color crema sofisticado
    page.padding = 30                    # Espaciado interno generoso
    page.theme_mode = ft.ThemeMode.LIGHT # Interfaz clara por defecto
```
> [!NOTE]
> La elección del color `#FDFBE3` busca reducir la fatiga visual y dar un aspecto tipo "papel" premium al formulario.

### 2. Declaración de Controles (Componentes UI)
Aquí es donde definimos cada elemento de interacción. Note cómo cada campo tiene su propia etiqueta de error asociada.

```python
    # Campo de Nombre con su etiqueta de error
    txt_nombre = ft.TextField(label="Nombre", border_color="#4D2A32", expand=True, value="")
    txt_error_nombre = ft.Text("", color="red", size=12, visible=False)
    col_nombre = ft.Column([txt_nombre, txt_error_nombre], spacing=2)

    # Campo de Número de Control
    txt_control = ft.TextField(label="Numero de control", border_color="#4D2A32", expand=True, value="")
    txt_error_control = ft.Text("", color="red", size=12, visible=False)
    col_control = ft.Column([txt_control, txt_error_control], spacing=2)

    # Campo de Email con validación de formato
    txt_email = ft.TextField(label="Email", border_color="#4D2A32", value="")
    txt_error_email = ft.Text("", color="red", size=12, visible=False)
    col_email = ft.Column([txt_email, txt_error_email], spacing=2)

    # Dropdowns para Carrera y Semestre
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

    # Grupo de Radio Buttons para Género
    rg_genero = ft.RadioGroup(content=ft.Row([
        ft.Radio(value="masculino", label="Masculino", fill_color="#4D2A32"),
        ft.Radio(value="femenino", label="Femenino", fill_color="#4D2A32")
    ]))
```

### 3. Sistema de Validación Exhaustivo
Esta función encapsula toda la inteligencia de negocio para prevenir el envío de datos erróneos.

```python
    def validar_campos():
        es_valido = True
        # Validación de Nombre: No vacío
        if not txt_nombre.value or txt_nombre.value.strip() == "":
            txt_nombre.border_color = "red"
            txt_error_nombre.value = "Ingresa tu nombre"
            txt_error_nombre.visible = True
            es_valido = False
        else:
            txt_nombre.border_color = "#4D2A32"
            txt_error_nombre.visible = False

        # Validación de Email: Formato con '@'
        if not txt_email.value or "@" not in txt_email.value:
            txt_email.border_color = "red"
            txt_error_email.value = "Ingresa un correo electrónico válido"
            txt_error_email.visible = True
            es_valido = False
        else:
            txt_email.border_color = "#4D2A32"
            txt_error_email.visible = False

        # Validación de Dropdowns: Opción seleccionada
        if not dd_carrera.value:
            dd_carrera.error_text = "Dato requerido"
            es_valido = False
        if not dd_semestre.value:
            dd_semestre.error_text = "Dato requerido"
            es_valido = False

        return es_valido
```

### 4. Procesamiento de Datos y Ventana de Resultados (AlertDialog)
Esta es la fase final donde el sistema confirma al usuario que su registro fue exitoso mediante una ventana modal dinámica. A diferencia de métodos tradicionales (como imprimir en consola), utilizamos el componente `ft.AlertDialog` para una experiencia inmersiva.

```python
    def enviar_datos(e):
        # Primero validamos que no haya errores
        if not validar_campos():
            page.update()
            return

        # Captura de datos finales de los controles
        nombre = txt_nombre.value.strip()
        control = txt_control.value.strip()
        email = txt_email.value.strip()
        carrera = dd_carrera.value
        semestre = dd_semestre.value
        genero = rg_genero.value

        # Definición del componente de Ventana Modal (AlertDialog)
        dlg_datos = ft.AlertDialog(
            title=ft.Text("Verificación de Datos", weight=ft.FontWeight.BOLD, color="#4D2A32", size=20),
            content=ft.Column([
                ft.Divider(color="#4D2A32"),
                ft.Text(f"👤 Estudiante: {nombre}", size=15),
                ft.Text(f"🆔 Control: {control}", size=15),
                ft.Text(f"✉️ Email: {email}", size=15),
                ft.Text(f"🎓 Carrera: {carrera}", size=15),
                ft.Text(f"📅 Semestre: {semestre}", size=15),
                ft.Text(f"🚻 Género: {genero}", size=15),
            ], tight=True, spacing=10),
            actions=[
                ft.TextButton("Cerrar", on_click=lambda _: setattr(dlg_datos, 'open', False))
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )

        # Inserción del diálogo en el objeto 'page' y apertura
        page.dialog = dlg_datos
        dlg_datos.open = True
        page.update()
```

#### 📋 Desglose del Método de Visualización
*   **Recopilación:** Se extraen los valores actuales de cada control mediante la propiedad `.value` una vez superada la validación.
*   **Construcción Dinámica:** El `ft.AlertDialog` se genera en tiempo de ejecución, permitiendo inyectar los datos del usuario directamente en el cuerpo del mensaje.
*   **Interactividad y Cierre:** Se integra un `ft.TextButton` que gestiona el estado de la ventana (`open = False`), garantizando que la interfaz vuelva a su estado original tras la confirmación.
*   **Estética:** Se utiliza una `ft.Column` con `tight=True` y divisores para que el modal sea visualmente agradable y se ajuste al contenido.

---

## ✨ Funcionalidades Clave
*   ✅ **Validación Estricta:** Impide envíos incompletos mediante semáforos visuales (Colores).
*   ✅ **Diseño Responsivo:** Uso de `expand=True` para adaptar el formulario al ancho de la pantalla.
*   ✅ **Arquitectura Limpia:** Separación total entre la UI (`page.add`) y la Lógica (`validar_campos`).
*   ✅ **Feedback Profesional:** Uso de `ft.AlertDialog` (Modal) en lugar de simples impresiones en consola.

---

## 📦 Instalación y Uso

1. **Clonar el Repositorio**:
   ```bash
   git clone https://github.com/IKERD11/U1-PROYECTO-INTEGRADOR.git
   ```
2. **Instalar Dependencias**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Ejecutar Aplicación**:
   ```bash
   python formulario2.py
   ```

---
**Desarrollado con ❤️ por:** [IKERD11](https://github.com/IKERD11)
**Materia:** Tópicos Avanzados de Programación
**Docente:** Unidad 1
