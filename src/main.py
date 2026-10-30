

# utils
from utils.system import entry

# constants
from core.constants import ENV_FILE


class Main:
    def __init__(self):
        self.running = True

    def startup(self):
        self.dispatch()

    def dispatch(self):
        while self.running:
            entries = entry()

            print(entries)


if __name__ == '__main__':
    try:
        app = Main()
        app.startup()

    except KeyboardInterrupt:
        print("finalizando...")
