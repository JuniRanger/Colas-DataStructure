import os
import subprocess
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

script = "main.py"  # Tu archivo principal de Tkinter

class ChangeHandler(FileSystemEventHandler):
    def __init__(self, process):
        self.process = process

    def on_modified(self, event):
        if event.src_path.endswith(".py"):
            print(f"Archivo modificado: {event.src_path}. Reiniciando aplicación...")
            self.restart_app()

    def restart_app(self):
        # Termina el proceso actual
        if self.process is not None:
            self.process.terminate()
            self.process.wait()
        # Inicia de nuevo el script de Tkinter
        self.process = subprocess.Popen(["python", script])

def start_watching():
    # Inicializa el primer proceso de Tkinter
    process = subprocess.Popen(["python", script])
    
    # Configura watchdog para monitorear el directorio actual
    event_handler = ChangeHandler(process)
    observer = Observer()
    observer.schedule(event_handler, path=".", recursive=True)
    
    # Inicia el watcher
    observer.start()
    
    try:
        while True:
            time.sleep(1)  # Mantén el watcher en ejecución
    except KeyboardInterrupt:
        observer.stop()
        if process is not None:
            process.terminate()
    observer.join()

if __name__ == "__main__":
    start_watching()
