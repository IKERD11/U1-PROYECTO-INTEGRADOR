# Proyecto Integrador - Unidad 1: Desarrollo de Interfaces de Usuario

Este repositorio contiene la implementación detallada del proyecto integrador de la Unidad 1. Se ha desarrollado una interfaz gráfica de usuario (GUI) utilizando **Flet**, un framework basado en Flutter que permite crear aplicaciones interactivas en Python.

## 🚀 Descripción General
La aplicación es un sistema de registro de estudiantes que aplica validaciones en tiempo real y muestra los resultados en una interfaz moderna y profesional.

---

## 🛠️ Estructura del Código y Funcionamiento Detallado

El archivo principal `formulario2.py` está estructurado de manera lógica para separar la configuración de la interfaz, la lógica de validación y el manejo de eventos.

### 1. Variables y Controles (Componentes de la UI)
Se utilizan diversos controles de Flet para capturar la información del usuario. Aquí se muestra cómo se definen los campos principales:

```python
# Ejemplo de definición de campos de texto y dropdowns
txt_nombre = ft.TextField(label="Nombre", border_color="#4D2A32", expand=True)
txt_email = ft.TextField(label="Email", border_color="#4D2A32")

dd_carrera = ft.Dropdown(
    label="Carrera",
    expand=True,
    options=[
        ft.dropdown.Option("Ingeniería en Sistemas"),
        ft.dropdown.Option("Ingeniería Civil"),
        ft.dropdown.Option("Ingeniería Industrial"),
    ]
)
```

*   **Campos de Texto (`ft.TextField`):** Capturan datos como nombre, número de control y email.
*   **Listas Desplegables (`ft.Dropdown`):** Facilitan la selección de Carrera y Semestre.
*   **Botones de Radio (`ft.RadioGroup`):** Aseguran una única opción para el género.

### 2. Lógica de Validación: Función `validar_campos()`
Esta función asegura que los datos cumplan con los requisitos antes de ser procesados.

```python
def validar_campos():
    es_valido = True
    # Validación de campo vacío
    if txt_nombre.value is None or txt_nombre.value.strip() == "":
        txt_nombre.border_color = "red"
        txt_error_nombre.visible = True
        es_valido = False
    
    # Validación de formato de email
    if "@" not in txt_email.value:
        txt_email.border_color = "red"
        txt_error_email.value = "Ingresa una dirección válida"
        es_valido = False
        
    return es_valido
```

*   **Validación de Vacíos:** Verifica que no se envíen entradas vacas usando `.strip()`.
*   **Validación de Email:** Comprueba la existencia del `@`.
*   **Feedback Visual:** Cambia el color del borde y muestra mensajes de error en rojo.

### 3. Manejo de Eventos: Función `enviar_datos(e)`
Gestiona la acción del botón de envío y la recopilación de datos finales.

```python
def enviar_datos(e):
    if not validar_campos():
        page.update()
        return

    # Recopilación de datos validados
    nombre = txt_nombre.value.strip()
    carrera = dd_carrera.value
    genero = rg_genero.value

    # Construcción y visualización del AlertDialog
    dlg_datos = ft.AlertDialog(
        title=ft.Text("Datos del Estudiante"),
        content=ft.Column([
            ft.Text(f"Nombre: {nombre}"),
            ft.Text(f"Carrera: {carrera}"),
            ft.Text(f"Género: {genero}"),
        ], tight=True),
        actions=[ft.TextButton("Cerrar", on_click=cerrar_dialogo)]
    )
    page.dialog = dlg_datos
    dlg_datos.open = True
    page.update()
```

### 4. Visualización de Datos: `ft.AlertDialog`
Los datos se muestran en una ventana modal emergente para confirmar que la información fue recibida correctamente.

---

## 📦 Dependencias
El proyecto requiere **Flet**. Puedes instalarlas usando:
```bash
pip install -r requirements.txt
```

## ⚙️ Cómo Ejecutar
1. Instala Python 3.
2. Ejecuta el comando:
   ```bash
   python formulario2.py
   ```

---
**Desarrollado por:** IKERD11
**Materia:** Tópicos Avanzados de Programación
**Unidad:** 1
