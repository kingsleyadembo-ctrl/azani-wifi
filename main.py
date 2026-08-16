import flet as ft

def main(page: ft.Page):
    page.title = "Azani WiFi Scanner"
    page.bgcolor = "#0F172A"
    page.padding = 20

    title = ft.Text("Azani WiFi Scanner", size=24, weight="bold", color="white")
    status = ft.Text("Bofya Scan kutafuta WiFi", color="#94A3B8")
    wifi_list = ft.Column(spacing=10)

    def scan_wifi(e):
        status.value = "Inascan..."
        wifi_list.controls = [ft.Text("Feature ya kuscan itawekwa hapa v1.1", color="yellow")]
        page.update()

    scan_btn = ft.ElevatedButton("Scan WiFi", on_click=scan_wifi, bgcolor="#3B82F6", color="white")

    page.add(title, status, scan_btn, wifi_list)

ft.app(target=main)
