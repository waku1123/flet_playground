import time

import flet as ft


def control(page: ft.Page):
    text = ft.Text(value="Hello World", color="green")
    page.controls.append(text)
    page.update()


def count_up(page: ft.Page):
    t = ft.Text()
    page.add(t)

    for i in range(10):
        t.value = f"Step {i}"
        page.update()
        time.sleep(1)


def container(page: ft.Page):
    row = ft.Row(controls=[ft.Text("A"), ft.Text("B"), ft.Text("C")])
    column = ft.Column(controls=[row, ft.Text("D")])
    page.add(column)


def event_handler(page: ft.Page):
    first_name = ft.TextField(label="First Name", autofocus=True)
    last_name = ft.TextField(label="Last Name")
    greetings = ft.Column()

    def on_click(e):
        greetings.controls.append(ft.Text(f"Hello, {first_name.value} {last_name.value}!"))
        first_name.value = ""
        last_name.value = ""
        page.update()
        first_name.focus()

    page.add(first_name, last_name, ft.ElevatedButton(text="Click me", on_click=on_click), greetings)


def reference(page: ft.Page):
    first_name = ft.Ref[ft.TextField]()
    last_name = ft.Ref[ft.TextField]()
    greetings = ft.Ref[ft.Column]()

    def on_click(e):
        greetings.current.controls.append(ft.Text(f"Hello, {first_name.current.value} {last_name.current.value}!"))
        first_name.current.value = ""
        last_name.current.value = ""
        page.update()
        first_name.current.focus()

    page.add(
        ft.TextField(ref=first_name, label="First Name", autofocus=True),
        ft.TextField(ref=last_name, label="Last Name"),
        ft.ElevatedButton("Say hello!", on_click=on_click),
        ft.Column(ref=greetings),
    )


# ft.app(target=control)
# ft.app(target=count_up)
# ft.app(target=container)
# ft.app(target=event_handler)
ft.app(target=reference)
