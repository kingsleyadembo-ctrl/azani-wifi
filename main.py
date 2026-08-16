import flet as ft
from jnius import autoclass
import time

def main(page: ft.Page):
    page.title = "Azani WiFi Scanner v1.3"
    page.bgcolor = "#0F172A"
    page.padding = 20
    page.scroll = "auto"

    title = ft.Text("Azani WiFi Scanner v1.3", size=24, weight="bold", color="white")
    status = ft.Text("Bofya Scan kutafuta WiFi", color="#94A3B8")
    wifi_list = ft.Column(spacing=10)

    def scan_wifi(e):
        status.value = "Inascan... ngoja sekunde 3"
        wifi_list.controls.clear()
        page.update()

        try:
            Context = autoclass('android.content.Context')
            PythonActivity = autoclass('org.flet.fletapp.FletActivity')
            activity = PythonActivity.mActivity
            wifi_service = activity.getSystemService(Context.WIFI_SERVICE)
            
            wifi_service.startScan()
            time.sleep(2)
            results = wifi_service.getScanResults()
            
            if results.size() == 0:
                wifi_list.controls.append(ft.Text("Hakuna WiFi zozote", color="red"))
            else:
                for i in range(results.size()):
                    result = results.get(i)
                    ssid = result.SSID
                    signal = result.level
                    wifi_list.controls.append(
                        ft.Card(
                            content=ft.Container(
                                content=ft.Column([
                                    ft.Text(ssid if ssid else "Hidden WiFi", size=16, weight="bold", color="white"),
                                    ft.Text(f"Signal: {signal} dBm", size=12, color="#94A3B8"),
                                ]),
                                padding=10
                            ),
                            bgcolor="#1E293B"  # <-- HAPA NDO TUMEBADILISHA color -> bgcolor
                        )
                    )
            status.value = f"Imemaliza: {results.size()} networks"
        except Exception as err:
            status.value = "Error: Ruhusu Location Permission kwenye Settings"
            wifi_list.controls.append(ft.Text(str(err), color="red", size=10))
        
        page.update()

    scan_btn = ft.ElevatedButton("Scan WiFi", on_click=scan_wifi, bgcolor="#3B82F6", color="white")
    page.add(title, status, scan_btn, wifi_list)

ft.app(target=main)
