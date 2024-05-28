"""Este módulo es un jemplo de Flet con valores aleatorios"""
import random
import time
from threading import Thread
import flet as ft

def setup_threads(func):
    """Crea un hilo para ejecutar la función función"""
    arduino_thread = Thread(target=func)
    arduino_thread.start()
    return arduino_thread


def main(page: ft.Page):
    """Función principal de la aplicación"""
    page.title = "Ejemplo de Flet con valores aleatorios"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)
    txt_humedad = ft.TextField(value="Humedad")
    txt_temperatura = ft.TextField(value="",label="Temperatura")

    def update_arduino_values():
        while True:
            txt_humedad.value = f"Humedad: {random.randint(10, 100)}%"
            txt_temperatura.value = f"Temperatura: {random.randint(10, 100)}°C"
            page.update()
            time.sleep(1)

    def minus_click(e):
        print(e)
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        print(e)
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            [
                txt_humedad,
                txt_temperatura
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
    )
    setup_threads(func=update_arduino_values)


ft.app(main)
