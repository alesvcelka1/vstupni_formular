import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def validate_text(text):
    # Zde můžete provést jakoukoliv validaci textového řetězce
    return True

def validate_number(number):
    try:
        int(number)  # Zde můžete použít další validaci čísla, například rozsah
        return True
    except ValueError:
        return False

def on_entry_activate(entry, text_entry, number_entry, label):
    text = text_entry.get_text()
    number = number_entry.get_text()

    if validate_text(text) and validate_number(number):
        label.set_text(f"Text: {text}, Číslo: {number}")

def main():
    Gtk.init(None)

    # Vytvoření okna
    window = Gtk.Window()
    window.set_default_size(300, 200)
    window.set_title("Vstupní formulář")
    window.connect("destroy", Gtk.main_quit)

    # Vytvoření formuláře
    form_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    window.add(form_box)

    text_entry = Gtk.Entry()
    text_entry.set_placeholder_text("Zadejte text")
    form_box.pack_start(text_entry, True, True, 0)

    number_entry = Gtk.Entry()
    number_entry.set_placeholder_text("Zadejte číslo")
    form_box.pack_start(number_entry, True, True, 0)

    label = Gtk.Label()
    form_box.pack_start(label, True, True, 0)

    text_entry.connect("activate", on_entry_activate, text_entry, number_entry, label)
    number_entry.connect("activate", on_entry_activate, text_entry, number_entry, label)

    # Zobrazení okna
    window.show_all()
    Gtk.main()

if __name__ == "__main__":
    main()
