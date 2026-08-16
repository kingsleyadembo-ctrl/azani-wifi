import flet as ft
import random

def main(page: ft.Page):
    page.title = "Azani WiFi Scanner v1.3 Demo"
    page.bgcolor = "#0F172A"
    page.padding = 20
    page.scroll = "auto"

    title = ft.Text("Azani WiFi Scanner v1.3", size=24, weight="bold", color="white")
    status = ft.Text("Hii ni Demo. APK ya kweli itascan WiFi", color="#94A3B8")
    wifi_list = ft.Column(spacing=10)

    def scan_wifi(e):
        status.value = "Inascan... Demo Mode"
        wifi_list.controls.clear()
        
        # DEMO DATA - Hii itaonekana tu
        demo_wifis = [
            {"ssid": "Azani-Home", "signal": -45},
            {"ssid": "Safaricom-4G", "signal": -62},
            {"ssid": "Faiba-WiFi", "signal": -70},
            {"ssid": "Hidden Network", "signal": -80},
        ]
        
        for wifi in demo_wifis:
            wifi_list.controls.append(
                ft.Card(
                    content=ft.Container(
                        content=ft.Column([
                            ft.Text(wifi["ssid"], size=16, weight="bold", color="white"),
                            ft.Text(f"Signal: {wifi['signal']} dBm", size=12, color="#94A3B8"),
                        ]),
                        padding=10
                    ),
                    color="#1E293B"
                )
            )
        status.value = f"Demo: {len(demo_wifis)} networks zimepatikana"
        page.update()

    scan_btn = ft.ElevatedButton("Scan WiFi", on_click=scan_wifi, bgcolor="#3B82F6", color="white")
    page.add(title, status, scan_btn, wifi_list)

ft.app(target=main)
