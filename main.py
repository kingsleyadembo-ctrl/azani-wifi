import flet as ft

def main(page: ft.Page):
    page.title = "Azani WiFi Scanner v1.6 Demo"
    page.bgcolor = "#0F172A"
    page.padding = 20

    status = ft.Text("Demo Mode: APK ya kweli itascan", color="#94A3B8")
    
    def scan_wifi(e):
        status.value = "APK pekee ndio inaweza kuona WiFi za kweli"
        page.update()

    page.add(
        ft.Text("Azani WiFi Scanner v1.6", size=24, weight="bold", color="white"),
        status,
        ft.ElevatedButton("Scan WiFi", on_click=scan_wifi, bgcolor="#3B82F6", color="white"),
    )

ft.app(target=main)
