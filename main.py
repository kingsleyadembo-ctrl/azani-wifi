import flet as ft
import random

ADMIN_PASS = {"admin": "1234", "cashier": "0000"}

# PACKAGES: [Jina, Bei, Mins, SMS]
PACKAGES = {
    "1": ["1 Hour", 5, 60, 10],
    "2": ["3 Hours", 15, 180, 20], 
    "3": ["24 Hours", 30, 1440, 50],
    "4": ["7 Days", 100, 10080, 200],
    "5": ["30 Days", 250, 43200, 500],
}

USERS_DB = {} # {voucher: {mins: 120, sms: 50, phone: "07.."}}

def main(page: ft.Page):
    page.title = "AZANI WIFI v6.9"
    page.theme_mode = ft.ThemeMode.DARK
    page.scroll = ft.ScrollMode.AUTO

    sms_field = ft.TextField(label="Namba ya Simu 07...", width=300, prefix_text="+254")

    def login_view():
        user = ft.TextField(label="Username", width=300)
        pw = ft.TextField(label="Password", password=True, width=300)
        def do_login(e):
            if ADMIN_PASS.get(user.value) == pw.value:
                page.go("/home")
            else:
                page.snack_bar = ft.SnackBar(ft.Text("Wrong Password!"), bgcolor=ft.colors.RED)
                page.snack_bar.open = True
                page.update()
        return ft.View("/login", [
            ft.Column([
                ft.Icon(ft.icons.WIFI, size=70, color=ft.colors.CYAN),
                ft.Text("AZANI WIFI HOTSPOT", size=22, weight=ft.FontWeight.BOLD),
                user, pw, 
                ft.ElevatedButton("LOGIN", on_click=do_login, width=300)
            ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=15)
        ])

    def generate_voucher(pkg_key):
        name, price, mins, sms = PACKAGES[pkg_key]
        voucher_code = f"AZANI-{random.randint(1000, 9999)}"
        USERS_DB[voucher_code] = {"mins": mins, "sms": sms, "phone": sms_field.value, "price": price}
        return voucher_code, name, mins, sms

    def send_sms(phone, code, mins, sms):
        page.snack_bar = ft.SnackBar(
            ft.Text(f"IME-TUMA: 0{phone}\nCode: {code}\nMins: {mins}, SMS: {sms}"), 
            bgcolor=ft.colors.GREEN
        )
        page.snack_bar.open = True
        page.update()

    def home_view():
        voucher_result = ft.Text("", size=16, weight=ft.FontWeight.BOLD, color=ft.colors.YELLOW)
        add_result = ft.Text("", color=ft.colors.GREEN)

        def create_voucher(e):
            pkg = pkg_dropdown.value
            if not pkg: return
            code, name, mins, sms = generate_voucher(pkg)
            voucher_result.value = f"VOUCHER: {code}\n{name}\nMins: {mins} | SMS: {sms}"
            
            if sms_field.value:
                send_sms(sms_field.value, code, mins, sms)
            page.update()

        def add_bundle(e):
            user_code = add_user_field.value
            pkg = add_pkg_dropdown.value
            if user_code in USERS_DB and pkg:
                added_mins = PACKAGES[pkg][2]
                added_sms = PACKAGES[pkg][3]
                USERS_DB[user_code]["mins"] += added_mins
                USERS_DB[user_code]["sms"] += added_sms
                add_result.value = f"Imeongezewa: {added_mins} Mins + {added_sms} SMS\nTotal: {USERS_DB[user_code]['mins']} Mins | {USERS_DB[user_code]['sms']} SMS"
            else:
                add_result.value = "Voucher haipatikani!"
            page.update()

        pkg_dropdown = ft.Dropdown(
            label="Chagua Bundle", width=300,
            options=[ft.dropdown.Option(key, f"{v[0]} - Ksh {v[1]} | {v[2]}Mins + {v[3]}SMS") for key, v in PACKAGES.items()]
        )
        add_pkg_dropdown = ft.Dropdown(
            label="Ongeza Bundle", width=300,
            options=[ft.dropdown.Option(key, f"{v[0]} - Ksh {v[1]} | {v[2]}Mins + {v[3]}SMS") for key, v in PACKAGES.items()]
        )
        add_user_field = ft.TextField(label="Weka Voucher Code", width=300)

        return ft.View("/home", [
            ft.Column([
                ft.Text("DASHBOARD", size=20, weight=ft.FontWeight.BOLD),
                
                ft.Text("1. TENGENEZA VOUCHER", weight=ft.FontWeight.BOLD),
                pkg_dropdown,
                sms_field,
                ft.ElevatedButton("Generate + Tuma SMS", on_click=create_voucher, width=300),
                voucher_result,
                
                ft.Divider(),
                ft.Text("2. ONGEZA BUNDLE", weight=ft.FontWeight.BOLD),
                add_user_field,
                add_pkg_dropdown,
                ft.ElevatedButton("Ongeza Mins + SMS", on_click=add_bundle, width=300),
                add_result,

                ft.Divider(),
                ft.ElevatedButton("LOGOUT", on_click=lambda e: page.go("/login"), style=ft.ButtonStyle(bgcolor=ft.colors.RED))
            ], alignment=ft.MainAxisAlignment.START, horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=15)
        ])

    def route_change(e):
        page.views.clear()
        page.views.append(login_view())
        if page.route == "/home":
            page.views.append(home_view())
        page.update()

    page.on_route_change = route_change
    page.go("/login")

ft.run(target=main)
