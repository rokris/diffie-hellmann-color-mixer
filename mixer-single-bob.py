import tkinter as tk
from tkinter import colorchooser


class ColorMixerAppBob:
    def __init__(self, root):
        self.root = root
        self.root.title("Diffie-Hellman Color Mixer - Bob")

        # Define labels for users
        self.label_public_color = tk.Label(root, text="Public Base Color (RGB):")
        self.label_public_color.grid(row=0, column=0, padx=10, pady=10)

        self.label_bob_input = tk.Label(root, text="Bob's Private Color (RGB):")
        self.label_bob_input.grid(row=1, column=0, padx=10, pady=10)

        self.label_alice_public = tk.Label(root, text="Alice's Public Color (RGB):")
        self.label_alice_public.grid(row=2, column=0, padx=10, pady=10)

        # Buttons for selecting colors
        self.button_select_public = tk.Button(
            root, text="Select Public Color", command=self.select_public_color
        )
        self.button_select_public.grid(row=0, column=1, padx=10, pady=10)

        self.button_select_bob_input = tk.Button(
            root, text="Select Bob's Color", command=self.select_bob_input
        )
        self.button_select_bob_input.grid(row=1, column=1, padx=10, pady=10)

        self.button_select_alice_public = tk.Button(
            root, text="Select Alice's Public Color", command=self.select_alice_public
        )
        self.button_select_alice_public.grid(row=2, column=1, padx=10, pady=10)

        # Labels to display colors
        self.public_color_display = tk.Label(root, width=20, height=2, bg="white")
        self.public_color_display.grid(row=0, column=2, padx=10, pady=10)

        self.bob_input_display = tk.Label(root, width=20, height=2, bg="white")
        self.bob_input_display.grid(row=1, column=2, padx=10, pady=10)

        self.alice_public_display = tk.Label(root, width=20, height=2, bg="white")
        self.alice_public_display.grid(row=2, column=2, padx=10, pady=10)

        # Entry fields for RGB values
        self.public_color_entry = tk.Entry(root, width=20)
        self.public_color_entry.grid(row=0, column=3, padx=10, pady=10)
        self.public_color_entry.bind(
            "<Return>", lambda event: self.enter_public_color()
        )

        self.bob_input_entry = tk.Entry(root, width=20)
        self.bob_input_entry.grid(row=1, column=3, padx=10, pady=10)
        self.bob_input_entry.bind("<Return>", lambda event: self.enter_bob_input())

        self.alice_public_entry = tk.Entry(root, width=20)
        self.alice_public_entry.grid(row=2, column=3, padx=10, pady=10)
        self.alice_public_entry.bind(
            "<Return>", lambda event: self.enter_alice_public()
        )

        # Result Labels
        self.label_bob_public = tk.Label(root, text="Bob's Public Color (RGB):")
        self.label_bob_public.grid(row=3, column=0, padx=10, pady=10)

        self.label_public_secret = tk.Label(root, text="Common Secret Color (RGB):")
        self.label_public_secret.grid(row=4, column=0, padx=10, pady=10)

        self.bob_public_color_display = tk.Label(root, width=20, height=2, bg="white")
        self.bob_public_color_display.grid(row=3, column=2, padx=10, pady=10)

        self.public_secret_color_display = tk.Label(
            root, width=20, height=2, bg="white"
        )
        self.public_secret_color_display.grid(row=4, column=2, padx=10, pady=10)

        self.bob_public_color_rgb = tk.Label(root, text="(255, 255, 255)")
        self.bob_public_color_rgb.grid(row=3, column=3, padx=10, pady=10)

        self.public_secret_color_rgb = tk.Label(root, text="(255, 255, 255)")
        self.public_secret_color_rgb.grid(row=4, column=3, padx=10, pady=10)

        # Placeholder for colors
        self.public_color = None
        self.bob_input_color = None
        self.alice_public_color = None

    def select_public_color(self):
        color = colorchooser.askcolor()[0]
        if color:  # Check if a color is selected
            self.public_color_display.config(bg=self.rgb_to_tkcolor(color))
            self.public_color_entry.delete(0, tk.END)
            self.public_color_entry.insert(0, str(color))
            self.public_color = color
            self.update_colors()

    def select_bob_input(self):
        color = colorchooser.askcolor()[0]
        if color:  # Check if a color is selected
            self.bob_input_display.config(bg=self.rgb_to_tkcolor(color))
            self.bob_input_entry.delete(0, tk.END)
            self.bob_input_entry.insert(0, str(color))
            self.bob_input_color = color
            self.update_colors()

    def select_alice_public(self):
        color = colorchooser.askcolor()[0]
        if color:  # Check if a color is selected
            self.alice_public_display.config(bg=self.rgb_to_tkcolor(color))
            self.alice_public_entry.delete(0, tk.END)
            self.alice_public_entry.insert(0, str(color))
            self.alice_public_color = color
            self.update_colors()

    def enter_public_color(self):
        rgb_color = self.parse_rgb(self.public_color_entry.get())
        if rgb_color:
            self.public_color_display.config(bg=self.rgb_to_tkcolor(rgb_color))
            self.public_color = rgb_color
            self.update_colors()

    def enter_bob_input(self):
        rgb_color = self.parse_rgb(self.bob_input_entry.get())
        if rgb_color:
            self.bob_input_display.config(bg=self.rgb_to_tkcolor(rgb_color))
            self.bob_input_color = rgb_color
            self.update_colors()

    def enter_alice_public(self):
        rgb_color = self.parse_rgb(self.alice_public_entry.get())
        if rgb_color:
            self.alice_public_display.config(bg=self.rgb_to_tkcolor(rgb_color))
            self.alice_public_color = rgb_color
            self.update_colors()

    def parse_rgb(self, rgb_string):
        """Parse a string into an RGB tuple."""
        try:
            return tuple(map(int, rgb_string.strip("() ").split(",")))
        except ValueError:
            return None

    def update_colors(self):
        if self.public_color and self.bob_input_color:
            # Mix public color with Bob's private color
            bob_public_color = self.mix_colors(self.public_color, self.bob_input_color)
            self.bob_public_color_display.config(
                bg=self.rgb_to_tkcolor(bob_public_color)
            )
            self.bob_public_color_rgb.config(text=str(bob_public_color))
        else:
            self.bob_public_color_display.config(bg="white")
            self.bob_public_color_rgb.config(text="(255, 255, 255)")

        if self.public_color and self.bob_input_color and self.alice_public_color:
            # Mix Bob's public color with Alice's public color to get the public secret
            bob_public_color = self.parse_rgb(self.bob_public_color_rgb.cget("text"))
            public_secret = self.mix_colors(bob_public_color, self.alice_public_color)
            # Display the final public secret color
            self.public_secret_color_display.config(
                bg=self.rgb_to_tkcolor(public_secret)
            )
            self.public_secret_color_rgb.config(text=str(public_secret))

    def mix_colors(self, color1, color2):
        """Mix two colors by averaging their RGB values."""
        return tuple(int((c1 + c2) / 2) for c1, c2 in zip(color1, color2))

    def rgb_to_tkcolor(self, rgb):
        """Convert an RGB tuple to a format suitable for Tkinter."""
        return "#%02x%02x%02x" % (int(rgb[0]), int(rgb[1]), int(rgb[2]))


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = ColorMixerAppBob(root)
    root.mainloop()
