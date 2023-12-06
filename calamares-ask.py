import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject
import subprocess
import threading
import sys

class InstallerApp(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Calamares Installer")
        self.set_default_size(300, 150)

        # Label
        label = Gtk.Label(label="Do you want to start the Calamares installer?")

        # Buttons
        button_yes = Gtk.Button(label="Yes")
        button_yes.connect("clicked", self.on_yes_clicked)

        button_no = Gtk.Button(label="No")
        button_no.connect("clicked", self.on_no_clicked)

        # Vertical box container
        vbox = Gtk.VBox(spacing=10)
        vbox.set_margin_top(20)
        vbox.add(label)
        vbox.add(button_yes)
        vbox.add(button_no)

        self.add(vbox)

    def on_yes_clicked(self, widget):
        # Run the Calamares installer in a separate thread
        threading.Thread(target=self.run_calamares_installer).start()

    def run_calamares_installer(self):
        subprocess.call(["install-debian"])
        sys.exit(0)

    def on_no_clicked(self, widget):
        # Close the application
        sys.exit(0)

def on_destroy(widget, data=None):
    Gtk.main_quit()

win = InstallerApp()
win.connect("destroy", on_destroy)
win.show_all()

# Start GTK main loop
GObject.threads_init()
Gtk.main()

