# 🎓 Proyecto Integrador - Unidad 1: Desarrollo de Interfaces de Usuario

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flet](https://img.shields.io/badge/Flet-0.80.5-00599C?style=for-the-badge&logo=flutter&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completado-success?style=for-the-badge)

Este repositorio alberga el **Proyecto Integrador de la Unidad 1**, enfocado en la creación de interfaces de usuario robustas, interactivas y validadas mediante el framework **Flet**. 

---

## 📋 Tabla de Contenidos
- [🚀 Descripción del Proyecto](#-descripción-del-proyecto)
- [🛠️ Arquitectura y Funcionamiento Detallado del Código](#️-arquitectura-y-funcionamiento-detallado-del-código)
  - [1. Función Principal: `main`](#1-función-principal-mainpage-ftpage)
  - [2. Función Lógica: `validar_campos`](#2-función-lógica-validar_campos)
  - [3. Función Controladora de Eventos: `enviar_datos`](#3-función-controladora-de-eventos-enviardatose)
- [📦 Instalación y Uso](#-instalación-y-uso)
- [✨ Funcionalidades Clave](#-funcionalidades-clave)

---

## 🚀 Descripción del Proyecto
La aplicación implementa un formulario de registro académico diseñado bajo principios de usabilidad y diseño limpio. Integra un motor de validación que garantiza que la información recogida sea veraz y completa, permitiendo al usuario visualizar sus datos en un modal profesional antes de finalizar.

---

## 🛠️ Arquitectura y Funcionamiento Detallado del Código

El archivo principal `formulario2.py` está estructurado en torno a una función principal (`main`) que actúa como el ciclo de vida de la aplicación, y funciones anidadas que manejan la lógica de validación y eventos. A continuación, se detalla el funcionamiento exacto de cada una de estas funciones clave:

### 1. Función Principal: `main(page: ft.Page)`
Esta es la función de punto de entrada requerida por el framework Flet. Su objetivo principal es inicializar el lienzo de la aplicación (la "página"), definir todos los componentes de la interfaz de usuario (UI), e integrarlos en la jerarquía visual de Flet.

```python
import flet as ft

def main(page: ft.Page):
    # Propiedades de la página (Canvas principal)
    page.title = "Registro de Estudiantes - Tópicos Avanzados"
    page.bgcolor = "#FDFBE3"            # Color crema sofisticado
    page.padding = 30                    # Espaciado interno generoso
    page.theme_mode = ft.ThemeMode.LIGHT # Interfaz clara por defecto
    
    # ... (Instanciación de controles) ...
```


**Funcionamiento detallado:**
*   **Configuración del Canvas:** Recibe un objeto `page` de tipo `ft.Page`. Modifica propiedades globales como `page.title` (título de la ventana), `page.bgcolor` (color de fondo crema tipo papel premium `#FDFBE3`), `page.padding` (márgenes internos) y `page.theme_mode` (fijado en modo claro).
*   **Instanciación de Componentes UI:** Se encarga de instanciar cada uno de los controles interactivos:
    *   `TextField`: Para el ingreso de texto libre (Nombre, Número de control, Email). Se configuran con propiedades como `expand=True` para diseño elástico y bordes temáticos.
    *   `Dropdown`: Menús desplegables para Carrera y Semestre, asegurando que el usuario elija de un set de opciones predefinido limitando los errores de escritura.
    *   `RadioGroup` y `Radio`: Agrupación de botones de opción única interconectados para definir el Género del estudiante.
*   **Inicialización del Sistema de Alertas (Gestión de Errores):** Por cada control de entrada que define, también inicializa paralelamente un componente de texto de error asociado (ocultos inicialmente con `visible=False` y de color rojo). Estos actuarán como contenedores que se volverán visibles dinámicamente si el usuario comete equivocaciones.
*   **Bindeo de Eventos:** Se definen los manejadores lógicos y se asocian a las acciones del usuario, siendo el más crucial la asociación de la función `enviar_datos` a la propiedad `on_click` del botón "Enviar".
*   **Ensamblado (DOM de Flet):** Finalmente, inyecta todos estos componentes individuales y contenedores previamente definidos dentro del árbol visual utilizando columnas (`ft.Column`) y filas (`ft.Row`) para estructurar el documento verticalmente, enviándolos a renderizar mediante la orden `page.add(...)`.

### 2. Función Lógica: `validar_campos()`
Es una función anidada directamente en la memoria local de la función `main()`. Se encarga completamente de la validación del lado del cliente (frontend) en Flet antes de recolectar los datos u operar con ellos. Implementa la "inteligencia de negocio" para garantizar la integridad y fiabilidad del registro.

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
            
        # ... (Resto de validaciones) ...
        return es_valido
```


**Funcionamiento detallado:**
*   **Mecanismo de Bandera (Flag State):** Inicializa de forma optimista una variable booleana actuando como bandera: `es_valido = True`. En cada uno de sus bloques condicionales, evalúa rigurosamente en secuencia cada campo. Si una evaluación se rechaza, la bandera cambia a `False` pero la función continúa iterando para encontrar otros campos vacíos u omitidos y mostrarlos todos en pantalla a la vez.
*   **Validación de Cadenas Limpias:** Comprueba que cada control de texto no reciba valores nulos o constituidos únicamente de espacios en blanco aplicando la sanitización mediante el método nativo en Python `.strip()`.
*   **Validación de Formato Elemental:** Para el objeto `txt_email`, además de verificar su no-nulidad, implementa una revisión rudimentaria requiriendo de forma innegociable la existencia del carácter arroba (`@`).
*   **Validación en Tiempo Real y Mutación Directa UI:** Este es el núcleo dinámico de su ejecución. Cada falla sobreescribe inmediatamente las propiedades visuales del control del componente original de UI de Flet; inyecta un color punitivo en el borde (`border_color = "red"`), imprime un mensaje de ayuda en la visibilidad de la etiqueta de error (`visible = True`). Si el error se repara en un intento posterior, invierte estas mutaciones visuales para limpiar la pantalla. Al final retorna la bandera `es_valido`.

### 3. Función Controladora de Eventos: `enviar_datos(e)`
Este método funciona como el "listener" (oyente) disparador asociado al clic del botón Enviar. Trabaja como el concentrador final del sistema, interconectando la validación y el procesamiento para el usuario.

```python
    def enviar_datos(e):
        # Primero validamos que no haya errores
        if not validar_campos():
            page.update()
            return

        # Captura de datos finales de los controles
        nombre = txt_nombre.value.strip()
        # ... (captura del resto de campos) ...

        # Definición del componente de Ventana Modal (AlertDialog)
        dlg_datos = ft.AlertDialog(
            title=ft.Text("Verificación de Datos", weight=ft.FontWeight.BOLD, color="#4D2A32", size=20),
            content=ft.Column([
                # ... (texto con los datos recopilados) ...
            ], tight=True, spacing=10),
            # ...
        )

        page.dialog = dlg_datos
        dlg_datos.open = True
        page.update()
```


**Funcionamiento detallado:**
*   **Invocación Transaccional y Bloqueo Seguro:** Su primera acción lógica es interconectar la función con la respuesta final de la función local `validar_campos()`. Si recibe un estado falso, bloquea un envío indebido solicitando una actualización obligatoria a la pantalla con `page.update()` para aplicar los estilos de error y usa la instrucción `return` para interrumpir limpiamente cualquier operación futura.
*   **Extracción de Valores Finales:** Si el filtro principal anterior se declara limpio (favorable), extrae toda la información final consultando a los objetos locales de Flet (usando `.value`) y las almacena en variables nativas de Python, aplicando `.strip()` para saneamiento final.
*   **Construcción de Interfaz Modal Autónoma (AlertDialog):** Crea las barreras visuales de interacción instanciando el widget emergente interactivo `ft.AlertDialog()`. Lo enriquece inyectando divisiones de línea y múltiples componentes de texto `ft.Text()` estructurados mediante f-strings, mostrando un resumen fiel de los registros recolectados. **Nota Importante:** Aquí se utilizó intencionadamente este método avanzado (`ft.AlertDialog`) para mostrar los datos recogidos directamente en la interfaz gráfica (GUI) como un pop-up elegante, en lugar de utilizar un método básico y poco profesional como imprimir las variables en la consola de comandos (`print()`).
*   **Definición de Función de Cierre (`cerrar_dialogo(e)`):** Alojado adentro, declara en memoria un pequeño controlador que mutará únicamente el estado del diálogo. Sobrescribe su propiedad (`dlg_datos.open = False`) para cerrar la ventana modal y refrescar la pantalla tras revisarlo.
*   **Renderización Forzada de Diálogos:** Finaliza asociando físicamente la variable a la propiedad reservada natural de la página con `page.dialog = dlg_datos`. Sobrescribe a un valor verdadero su apertura nativa (`dlg_datos.open = True`) y despacha la orden de re-dibujar la interfaz final invocando `page.update()`, permitiendo al cliente confirmar su inscripción asegurada.

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
