from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton, MDFillRoundFlatIconButton
from kivymd.uix.dialog import MDDialog
import socket
from kivy.lang import Builder
from kivy.core.clipboard import Clipboard

kv = """
MDScreen:
    MDTextField:
        id: ip_input
        hint_text: "Enter IP"
        pos_hint: {'center_x': 0.5, 'top': 0.8}
        size_hint_x: 0.8

    MDTextField:
        id: results
        hint_text: "Results will appear here..."
        pos_hint: {'center_x': 0.5, 'top': 0.6}
        size_hint_y: None
        height: 200

    MDRaisedButton:
        text: "Lookup"
        pos_hint: {'center_x': 0.5, 'y': 0.4}
        on_release: app.lookup_ip()

    MDFillRoundFlatIconButton:
        text: "Copy"
        icon: "content-copy"
        pos_hint: {'center_x': 0.3, 'y': 0.1}
        on_release: app.copy_results()

    MDFillRoundFlatIconButton:
        text: "Save"
        icon: "content-save"
        pos_hint: {'center_x': 0.7, 'y': 0.1}
        on_release: app.save_results()

    MDRaisedButton:
        text: "About"
        pos_hint: {'center_x': 0.2, 'y': 0.1}
        on_release: app.show_about()
"""

class IPLookupApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.screen = Builder.load_string(kv)
        return self.screen

    def lookup_ip(self):
        ip = self.screen.ids.ip_input.text

        if ip:
            self.screen.ids.results.text = "START SEARCHING...\nPLEASE WAIT..."

            results = ""

            ip_parts = ip.split(".")
            ip_base = ".".join(ip_parts[:-1]) + "."

            for last_octet in range(1, 255):
                address = ip_base + str(last_octet)

                try:
                    hostname = socket.gethostbyaddr(address)[0]
                    results += f"\n{address} - {hostname}"

                except socket.herror:
                    continue

            if not results:
                self.screen.ids.results.text = "NO HOSTS FOUND"
            else:
                self.screen.ids.results.text = results

    def copy_results(self):
        if self.screen.ids.results.text:
            Clipboard.copy(self.screen.ids.results.text)
            self.show_copy_message()

    def show_copy_message(self):
        MDDialog(
            text="Results copied to clipboard.",
            buttons=[
                MDRaisedButton(
                    text="OK",
                    on_release=lambda x: self.copy_result_dialog.dismiss()
                )
            ],
        ).open()

    def save_results(self):
        if self.screen.ids.results.text:
            # Implement saving logic here, for example, save to a file
            self.show_save_message()

    def show_save_message(self):
        MDDialog(
            text="Results saved to a file.",
            buttons=[
                MDRaisedButton(
                    text="OK",
                    on_release=lambda x: self.save_result_dialog.dismiss()
                )
            ],
        ).open()

    def show_about(self):
        about_text = """
        Welcome to the IP Lookup Tool

This tool allows you to find the IP addresses corresponding to a base IP.  

How to use:

- Enter the end of the IP like 192.168.1.0
- Click Lookup to start searching IPs
- Results will be displayed here

Please subscribe for updates: 

t.me/kaizonova

Contact:

t.me/kaizokua
        """

        MDDialog(
            title='About',
            text=about_text,
            size_hint=(0.8, 1),
        ).open()

if __name__ == '__main__':
    IPLookupApp().run()
