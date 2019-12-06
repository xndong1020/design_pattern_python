class Bitmap:
    def __init__(self, filename):
        print("Bitmap initialized")
        self.filename = filename

    def draw(self):
        print(f"Start drawing bitmap loaded from {self.filename}")


class LazyBitmapProxy:
    def __init__(self, filename):
        self.filename = filename
        self._instance = None

    def draw(self):
        if self._instance is None:
            self._instance = Bitmap(self.filename)
        print(f"Start drawing bitmap loaded from {self.filename}")


def draw_image(image):
    print("About to draw image")
    image.draw()
    print("Done drawing image")


if __name__ == "__main__":
    bmp = LazyBitmapProxy("emoji.png")
    draw_image(bmp)

    """
    OUTPUT:
    About to draw image
    Bitmap initialized
    Start drawing bitmap loaded from emoji.png
    Done drawing image
    """

