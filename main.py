import flet as ft
import wifi  # kwa kuscan wifi
from wifi import Cell

def main(page: ft.Page):
    page.title = "Azani WiFi Scanner"
    page.bgcolor = "#0F172A"
    page.padding = 20
    page.scroll = "auto"

    title = ft.Text("Azani WiFi Scanner v1.1", size=24, weight="bold", color="white")
    status = ft.Text("Bofya Scan kutafuta WiFi", color="#94A3B8")
    wifi_list = ft.Column(spacing=10)

    def scan_wifi(e):
        status.value = "Inascan... ngoja sekunde 3"
        wifi_list.controls.clear()
        page.update()

        try:
            # Scan WiFi networks
            cells = [cell for cell in Cell.all('wlan0')]
            if not cells:
                wifi_list.controls.append(ft.Text("Hakuna WiFi zozote zilizopatikana", color="red"))
            else:
                for cell in cells:
                    wifi_list.controls.append(
                        ft.Card(
                            content=ft.Container(
                                content=ft.Column([
                                    ft.Text(cell.ssid, size=16, weight="bold", color="white"),
                                    ft.Text(f"Signal: {cell.signal} dBm", size=12, color="#94A3B8"),
                                    ft.Text(f"Encrypted: {'Ndiyo' if cell.encrypted else 'Hapana'}", size=12, color="#94A3B8")
                                ]),
                                padding=10
                            ),
                            color="#1E293B"
                        )
                    )
            status.value = f"Imemaliza: {len(cells)} networks zimepatikana"
        except Exception as err:
            status.value = "Error: Ruhusu Location kwenye simu yako"
            wifi_list.controls.append(ft.Text(str(err), color="red", size=10))
        
        page.update()

    scan_btn = ft.ElevatedButton("Scan WiFi", on_click=scan_wifi, bgcolor="#3B82F6", color="white")
    page.add(title, status, scan_btn, wifi_list)

ft.app(target=main)
