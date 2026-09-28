import os
import ctypes
import winreg
from pathlib import Path

def get_desktop_path():
    try:
        with winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\User Shell Folders"
        ) as key:
            desktop = winreg.QueryValueEx(key, "Desktop")[0]
            expanded = os.path.expandvars(desktop)
            if os.path.isdir(expanded):
                return expanded
    except Exception:
        pass

    for candidate in (
        Path.home() / "Desktop",
        Path.home() / "OneDrive" / "Desktop",
        Path.home() / "OneDrive" / "Área de Trabalho",
        Path("C:/Users/Public/Desktop"),
        Path.home(),
    ):
        if candidate.is_dir():
            return str(candidate)
    return os.getcwd()

def criar_atalho(executavel="NEXA.exe", nome_atalho="NEXA.lnk"):
    try:
        import win32com.client
    except ImportError:
        print("pywin32 não está instalado.")
        return

    executavel_path = None
    for local in (Path("dist") / executavel, Path(executavel)):
        if local.exists():
            executavel_path = str(local.resolve())
            break

    if not executavel_path:
        print("Executável não encontrado.")
        return

    destino = os.path.join(get_desktop_path(), nome_atalho)
    shell = win32com.client.Dispatch("WScript.Shell")
    atalho = shell.CreateShortCut(destino)
    atalho.TargetPath = executavel_path
    atalho.WorkingDirectory = os.path.dirname(executavel_path)
    atalho.IconLocation = executavel_path
    atalho.Description = "NEXA — Plataforma de Gestão para Clínicas"
    atalho.save()
    print(f"Atalho criado: {destino}")

if __name__ == "__main__":
    criar_atalho()
