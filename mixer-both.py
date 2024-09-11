import tkinter as tk
from tkinter import colorchooser

class ColorMixerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Diffie-Hellman Color Mixer")

        
        # Define labels for users
        self.label_public_color = tk.Label(root, text="Public Base Color (RGB):")
        self.label_public_color.grid(row=0, column=0, padx=10, pady=10)

        self.label_alice_private = tk.Label(root, text="Alice's Private Color (RGB):")
        self.label_alice_private.grid(row=1, column=0, padx=10, pady=10)

        self.label_bob_private = tk.Label(root, text="Bob's Private Color (RGB):")
        self.label_bob_private.grid(row=2, column=0, padx=10, pady=10)

        # Buttons for selecting colors
        self.button_select_public = tk.Button(root, text="Select Public Color", command=self.select_public_color)
        self.button_select_public.grid(row=0, column=1, padx=10, pady=10)

        self.button_select_alice_private = tk.Button(root, text="Select Alice's Color", command=self.select_alice_private)
        self.button_select_alice_private.grid(row=1, column=1, padx=10, pady=10)

        self.button_select_bob_private = tk.Button(root, text="Select Bob's Color", command=self.select_bob_private)
        self.button_select_bob_private.grid(row=2, column=1, padx=10, pady=10)

        # Labels to display colors
        self.public_color_display = tk.Label(root, width=20, height=2, bg="white")
        self.public_color_display.grid(row=0, column=2, padx=10, pady=10)

        self.alice_color_display = tk.Label(root, width=20, height=2, bg="white")
        self.alice_color_display.grid(row=1, column=2, padx=10, pady=10)

        self.bob_color_display = tk.Label(root, width=20, height=2, bg="white")
        self.bob_color_display.grid(row=2, column=2, padx=10, pady=10)

        # Entry fields for RGB values
        self.public_color_entry = tk.Entry(root, width=20)
        self.public_color_entry.grid(row=0, column=3, padx=10, pady=10)
        self.public_color_entry.bind("<Return>", lambda event: self.enter_public_color())

        self.alice_color_entry = tk.Entry(root, width=20)
        self.alice_color_entry.grid(row=1, column=3, padx=10, pady=10)
        self.alice_color_entry.bind("<Return>", lambda event: self.enter_alice_color())

        self.bob_color_entry = tk.Entry(root, width=20)
        self.bob_color_entry.grid(row=2, column=3, padx=10, pady=10)
        self.bob_color_entry.bind("<Return>", lambda event: self.enter_bob_color())

        # Result Labels
        self.label_alice_mixed = tk.Label(root, text="Alice's Shared Color (RGB):")
        self.label_alice_mixed.grid(row=3, column=0, padx=10, pady=10)

        self.label_bob_mixed = tk.Label(root, text="Bob's Shared Color (RGB):")
        self.label_bob_mixed.grid(row=4, column=0, padx=10, pady=10)

        self.alice_mixed_color_display = tk.Label(root, width=20, height=2, bg="white")
        self.alice_mixed_color_display.grid(row=3, column=2, padx=10, pady=10)

        self.bob_mixed_color_display = tk.Label(root, width=20, height=2, bg="white")
        self.bob_mixed_color_display.grid(row=4, column=2, padx=10, pady=10)

        self.alice_mixed_color_rgb = tk.Label(root, text="(255, 255, 255)")
        self.alice_mixed_color_rgb.grid(row=3, column=3, padx=10, pady=10)

        self.bob_mixed_color_rgb = tk.Label(root, text="(255, 255, 255)")
        self.bob_mixed_color_rgb.grid(row=4, column=3, padx=10, pady=10)

        # Secret Shared Color Label
        self.label_shared_secret = tk.Label(root, text="Common Secret Color (RGB):")
        self.label_shared_secret.grid(row=5, column=0, padx=10, pady=10)

        self.shared_secret_color_display = tk.Label(root, width=20, height=2, bg="white")
        self.shared_secret_color_display.grid(row=5, column=2, padx=10, pady=10)

        self.shared_secret_color_rgb = tk.Label(root, text="(255, 255, 255)")
        self.shared_secret_color_rgb.grid(row=5, column=3, padx=10, pady=10)

        # Placeholder for colors
        self.public_color = None
        self.alice_private_color = None
        self.bob_private_color = None

    def select_public_color(self):
        color = colorchooser.askcolor()[0]
        if color:  # Check if a color is selected
            self.public_color_display.config(bg=self.rgb_to_tkcolor(color))
            self.public_color_entry.delete(0, tk.END)
            self.public_color_entry.insert(0, str(color))
            self.public_color = color
            self.update_colors()

    def select_alice_private(self):
        color = colorchooser.askcolor()[0]
        if color:  # Check if a color is selected
            self.alice_color_display.config(bg=self.rgb_to_tkcolor(color))
            self.alice_color_entry.delete(0, tk.END)
            self.alice_color_entry.insert(0, str(color))
            self.alice_private_color = color
            self.update_colors()

    def select_bob_private(self):
        color = colorchooser.askcolor()[0]
        if color:  # Check if a color is selected
            self.bob_color_display.config(bg=self.rgb_to_tkcolor(color))
            self.bob_color_entry.delete(0, tk.END)
            self.bob_color_entry.insert(0, str(color))
            self.bob_private_color = color
            self.update_colors()

    def enter_public_color(self):
        rgb_color = self.parse_rgb(self.public_color_entry.get())
        if rgb_color:
            self.public_color_display.config(bg=self.rgb_to_tkcolor(rgb_color))
            self.public_color = rgb_color
            self.update_colors()

    def enter_alice_color(self):
        rgb_color = self.parse_rgb(self.alice_color_entry.get())
        if rgb_color:
            self.alice_color_display.config(bg=self.rgb_to_tkcolor(rgb_color))
            self.alice_private_color = rgb_color
            self.update_colors()

    def enter_bob_color(self):
        rgb_color = self.parse_rgb(self.bob_color_entry.get())
        if rgb_color:
            self.bob_color_display.config(bg=self.rgb_to_tkcolor(rgb_color))
            self.bob_private_color = rgb_color
            self.update_colors()

    def parse_rgb(self, rgb_string):
        """Parse a string into an RGB tuple."""
        try:
            return tuple(map(int, rgb_string.strip("() ").split(",")))
        except ValueError:
            return None

    def update_colors(self):
        if self.public_color and self.alice_private_color and self.bob_private_color:
            # Mix public color with both private colors
            mixed_public_with_alice = self.mix_colors(self.public_color, self.alice_private_color)
            mixed_public_with_bob = self.mix_colors(self.public_color, self.bob_private_color)

            # Calculate the shared secret colors
            shared_secret = self.mix_colors(mixed_public_with_alice, mixed_public_with_bob)

            # Display the final shared secret color
            self.shared_secret_color_display.config(bg=self.rgb_to_tkcolor(shared_secret))
            self.shared_secret_color_rgb.config(text=str(shared_secret))
            
            # Display colors mixed by Alice and Bob
            self.alice_mixed_color_display.config(bg=self.rgb_to_tkcolor(mixed_public_with_alice))
            self.alice_mixed_color_rgb.config(text=str(mixed_public_with_alice))

            self.bob_mixed_color_display.config(bg=self.rgb_to_tkcolor(mixed_public_with_bob))
            self.bob_mixed_color_rgb.config(text=str(mixed_public_with_bob))

    def mix_colors(self, color1, color2):
        """Mix two colors by averaging their RGB values."""
        return tuple(int((c1 + c2) / 2) for c1, c2 in zip(color1, color2))

    def rgb_to_tkcolor(self, rgb):
        """Convert an RGB tuple to a format suitable for Tkinter."""
        return "#%02x%02x%02x" % (int(rgb[0]), int(rgb[1]), int(rgb[2]))

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = ColorMixerApp(root)
    root.mainloop()
