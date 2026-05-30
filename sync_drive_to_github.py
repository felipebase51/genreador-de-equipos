#!/usr/bin/env python3
"""
Script para sincronizar cambios de Google Drive a GitHub automáticamente
Ejecutar: python3 sync_drive_to_github.py
"""

import os
import subprocess
import time
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class GitAutoCommitHandler(FileSystemEventHandler):
    """Detecta cambios y hace commits automáticos"""
    
    def __init__(self, repo_path):
        self.repo_path = repo_path
        self.last_commit_time = time.time()
        self.debounce_seconds = 5  # Espera 5 segundos antes de hacer commit
    
    def on_modified(self, event):
        if event.is_directory or '.git' in event.src_path:
            return
        
        # Evita múltiples commits en poco tiempo
        current_time = time.time()
        if current_time - self.last_commit_time < self.debounce_seconds:
            return
        
        self.last_commit_time = current_time
        self.auto_commit(event.src_path)
    
    def on_created(self, event):
        if event.is_directory or '.git' in event.src_path:
            return
        
        current_time = time.time()
        if current_time - self.last_commit_time < self.debounce_seconds:
            return
        
        self.last_commit_time = current_time
        self.auto_commit(event.src_path)
    
    def auto_commit(self, file_path):
        """Hace commit y push automático"""
        try:
            os.chdir(self.repo_path)
            
            # Agrega el archivo
            subprocess.run(['git', 'add', file_path], check=True)
            
            # Commit con timestamp
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            commit_msg = f"Auto-sync: {os.path.basename(file_path)} - {timestamp}"
            
            result = subprocess.run(['git', 'commit', '-m', commit_msg], 
                                  capture_output=True, text=True)
            
            if result.returncode == 0:
                # Push a GitHub
                push_result = subprocess.run(['git', 'push'], 
                                           capture_output=True, text=True)
                print(f"✓ Sincronizado: {commit_msg}")
                if push_result.returncode != 0:
                    print(f"⚠ Error en push: {push_result.stderr}")
            else:
                print(f"ℹ Sin cambios para: {file_path}")
        
        except Exception as e:
            print(f"✗ Error en auto-commit: {e}")

def main():
    repo_path = os.path.dirname(os.path.abspath(__file__))
    
    print(f"🔄 Sincronización Google Drive ↔ GitHub iniciada")
    print(f"📁 Carpeta monitoreada: {repo_path}")
    print(f"⏸  Presiona Ctrl+C para detener\n")
    
    event_handler = GitAutoCommitHandler(repo_path)
    observer = Observer()
    observer.schedule(event_handler, path=repo_path, recursive=True)
    observer.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n🛑 Sincronización detenida")
        observer.stop()
    observer.join()

if __name__ == '__main__':
    main()
