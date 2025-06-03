import flet as ft
from time import sleep


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.title = "Tela de Login"

    def mudar_tema(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
            theme_icon.icon = "light_mode"
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
            theme_icon.icon = "dark_mode"
        page.update()

    theme_icon = ft.IconButton(
        icon='dark_mode',
        tooltip="Alternar tema",
        on_click=mudar_tema
    )

    page.appbar = ft.AppBar(
        title=ft.Text("Login", size=24, weight="bold"),
        bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
        center_title=True,
        actions=[
            theme_icon
        ]
    )

    email_input = ft.TextField(label="E-mail", width=300)
    senha_input = ft.TextField(
        label="Senha", password=True, can_reveal_password=True, width=300)

    status_text = ft.Text("", color="red")

    dialog = ft.AlertDialog(
        title=ft.Text(
            "Login realizado com sucesso! \nAguarde um momento, você está sendo redirecionado",
            size=16,
            text_align=ft.TextAlign.CENTER
        ),
        on_dismiss=lambda e: print("Dialogo fechado")
    )

    def validar_login(e):
        email = email_input.value.strip()
        senha = senha_input.value.strip()

        if not email or not senha:
            status_text.value = "Preencha todos os campos."
        elif "@" not in email:
            status_text.value = "E-mail inválido."
        elif len(senha) < 6:
            status_text.value = "A senha deve ter pelo menos 6 caracteres."
        else:
            status_text.value = ""
            sleep(2)
            page.open(dialog)
        page.update()

    botao_login = ft.ElevatedButton("Entrar", on_click=validar_login)

    page.add(
        ft.Column(
            [
                email_input,
                senha_input,
                botao_login,
                status_text
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )


ft.app(target=main)
