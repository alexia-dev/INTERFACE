from pathlib import Path
import os
import winreg

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
    return str(Path.home())

def criar_atalho(executavel="NEXA.exe", nome_atalho="NEXA.lnk"):
    caminho_executavel = next(
        (str(p.resolve()) for p in (Path(executavel), Path("dist") / executavel) if p.exists()),
        None,
    )
    if not caminho_executavel:
        return "Executável não encontrado."

    try:
        import win32com.client
        destino = os.path.join(get_desktop_path(), nome_atalho)
        shell = win32com.client.Dispatch("WScript.Shell")
        atalho = shell.CreateShortCut(destino)
        atalho.TargetPath = caminho_executavel
        atalho.WorkingDirectory = os.path.dirname(caminho_executavel)
        atalho.IconLocation = caminho_executavel
        atalho.save()
        return f"Atalho criado em: {destino}"
    except ImportError:
        return "pywin32 não está instalado."

if __name__ == "__main__":
    print(criar_atalho())
