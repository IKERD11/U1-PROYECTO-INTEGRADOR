# 🎓 Proyecto Integrador - Unidad 1: Desarrollo de Interfaces de Usuario

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flet](https://img.shields.io/badge/Flet-0.80.5-00599C?style=for-the-badge&logo=flutter&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completado-success?style=for-the-badge)

Este repositorio alberga el **Proyecto Integrador de la Unidad 1**, enfocado en la creación de interfaces de usuario robustas, interactivas y validadas mediante el framework **Flet**. 

---

## 📋 Tabla de Contenidos
- [🚀 Descripción del Proyecto](#-descripción-del-proyecto)
- [🛠️ Arquitectura y Funcionamiento](#️-arquitectura-y-funcionamiento)
  - [1. Configuración de la Ventana](#1-configuración-de-la-ventana)
  - [2. Controles de Entrada](#2-controles-de-entrada)
  - [3. Sistema de Validación](#3-sistema- de-validación)
  - [4. Procesamiento y Modal](#4-procesamiento-y-modal)
- [📦 Instalación y Uso](#-instalación-y-uso)
- [✨ Funcionalidades Clave](#-funcionalidades-clave)

---

## 🚀 Descripción del Proyecto
La aplicación implementa un formulario de registro académico diseñado bajo principios de usabilidad y diseño limpio. No es solo una interfaz de captura; integra un motor de validación que garantiza que la información recogida sea veraz y completa.

---

## 🛠️ Arquitectura y Funcionamiento

A continuación, se detalla el código de `formulario2.py` segmentado por responsabilidades técnicas.

### 1. Configuración de la Ventana
El punto de entrada define el entorno de ejecución de la interfaz.

```python
import flet as ft

def main(page: ft.Page):
    # Configuración de alta fidelidad
    page.title = "Registro de Estudiantes - TAP"
    page.bgcolor = "#FDFBE3"  # Paleta sofisticada (Crema)
    page.padding = 30
    page.theme_mode = ft.ThemeMode.LIGHT
```
> [!NOTE]
> Se utiliza una paleta de colores personalizada para alejar el diseño de los estilos genéricos de sistema.

### 2. Controles de Entrada (UI Components)
Cada componente ha sido configurado para ser intuitivo y accesible.

```python
    # Definición de campos con feedback visual reactivo
    txt_nombre = ft.TextField(label="Nombre", border_color="#4D2A32", expand=True)
    dd_carrera = ft.Dropdown(
        label="Carrera",
        options=[ft.dropdown.Option(c) for c in ["Sistemas", "Civil", "Industrial"]]
    )
    rg_genero = ft.RadioGroup(content=ft.Row([
        ft.Radio(value="m", label="Masculino"),
        ft.Radio(value="f", label="Femenino")
    ]))
```

### 3. Sistema de Validación (Logic Layer)
Implementa una validación exhaustiva antes de cualquier procesamiento de datos.

```python
    def validar_campos():
        es_valido = True
        # Validación de campos obligatorios
        if not txt_nombre.value or not txt_nombre.value.strip():
            txt_nombre.border_color = "red"
            txt_error_nombre.visible = True
            es_valido = False
        
        # Validación semántica de correo
        if "@" not in txt_email.value:
            txt_email.border_color = "red"
            es_valido = False
            
        return es_valido
```

### 4. Procesamiento y AlertDialog (Output Layer)
Tras la validación, los datos se presentan de manera estructurada en una ventana modal.

```python
    def enviar_datos(e):
        if not validar_campos():
            page.update()
            return
            
        # Despliegue de AlertDialog según requerimientos
        page.dialog = ft.AlertDialog(
            title=ft.Text("Registro Exitoso", weight="bold"),
            content=ft.Text(f"Bienvenido, {txt_nombre.value}"),
            actions=[ft.TextButton("Cerrar", on_click=lambda _: setattr(page.dialog, 'open', False))]
        )
        page.dialog.open = True
        page.update()
```

---

## ✨ Funcionalidades Clave

*   ✅ **Validación en Tiempo Real:** Feedback visual instantáneo mediante colores y mensajes de error.
*   ✅ **Dropdowns Dinámicos:** Selección de semestre generada mediante algoritmos para facilitar la escalabilidad.
*   ✅ **Interfaz Premium:** Uso de sombras, bordes redondeados y una paleta de colores cohesiva.
*   ✅ **Alertas Modales:** Uso de `ft.AlertDialog` para una confirmación de datos limpia y sin distracciones.

---

## 📦 Instalación y Uso

Sigue estos pasos para ejecutar el proyecto en tu entorno local:

1. **Clonar**: `git clone https://github.com/IKERD11/U1-PROYECTO-INTEGRADOR.git`
2. **Dependencias**: Instala los requisitos técnicos:
   ```bash
   pip install -r requirements.txt
   ```
3. **Ejecutar**: Lanza el servidor de la aplicación:
   ```bash
   python formulario2.py
   ```

---
**Desarrollado con ❤️ por:** [IKERD11](https://github.com/IKERD11)
**Materia:** Tópicos Avanzados de Programación
**Docente:** Unidad 1
