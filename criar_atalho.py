# criar_atalho.py
import os
import sys
import ctypes
import winreg
import shutil
from pathlib import Path

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def get_desktop_path():
    """Obtém o caminho correto da área de trabalho com fallbacks"""
    try:
        # Tenta via registro do Windows
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, 
                           r"Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders") as key:
            desktop = winreg.QueryValueEx(key, "Desktop")[0]
            expanded = os.path.expandvars(desktop)
            if os.path.isdir(expanded):
                return expanded
    except:
        pass
    
    # Fallbacks
    locais = [
        Path.home() / "Desktop",
        Path.home() / "OneDrive" / "Desktop",
        Path.home() / "OneDrive" / "Área de Trabalho",
        Path("C:/Users/Public/Desktop"),
        Path.home()
    ]
    
    for local in locais:
        if local.is_dir():
            return str(local)
    
    return str(Path.home())

def criar_atalho():
    # Configurações
    nome_atalho = "Sistema de Relatórios.lnk"
    nome_executavel = "SistemaRelatorios.exe"
    
    # 1. Localizar o executável
    caminho_executavel = None
    
    # Tenta na pasta atual
    if Path(nome_executavel).exists():
        caminho_executavel = os.path.abspath(nome_executavel)
    else:
        # Tenta na pasta dist
        dist_path = Path("dist") / nome_executavel
        if dist_path.exists():
            caminho_executavel = str(dist_path.resolve())
    
    if not caminho_executavel:
        print("ERRO: Executável não encontrado!")
        print("Execute primeiro o build.py para criar o executável")
        return
    
    # 2. Obter caminho da área de trabalho
    desktop_path = get_desktop_path()
    caminho_atalho = os.path.join(desktop_path, nome_atalho)
    
    # 3. Se não for admin, tentar criar na pasta do usuário
    if not is_admin():
        try:
            user_path = Path.home() / "AppData" / "Roaming" / "Microsoft" / "Windows" / "Start Menu" / "Programs"
            user_path.mkdir(parents=True, exist_ok=True)
            caminho_atalho = os.path.join(user_path, nome_atalho)
        except Exception:
            pass
    
    # 4. Criar atalho usando diferentes métodos
    try:
        # Método 1: Usando win32com (mais confiável)
        import win32com.client
        shell = win32com.client.Dispatch("WScript.Shell")
        atalho = shell.CreateShortCut(caminho_atalho)
        atalho.TargetPath = caminho_executavel
        atalho.WorkingDirectory = os.path.dirname(caminho_executavel)
        atalho.IconLocation = caminho_executavel
        atalho.save()
        return f"Atalho criado em: {caminho_atalho}"
    
    except ImportError:
        # Método 2: Se win32com não estiver disponível
        try:
            # Cria um arquivo .bat como fallback
            bat_path = os.path.join(desktop_path, "Iniciar_Sistema.bat")
            with open(bat_path, "w") as f:
                f.write(f'@echo off\nstart "" "{caminho_executavel}"\npause')
            
            return f"Arquivo BAT criado em: {bat_path}"
        
        except Exception as e:
            return f"Erro ao criar alternativa: {str(e)}"
    
    except Exception as e:
        return f"Erro ao criar atalho: {str(e)}"

if __name__ == "__main__":
    resultado = criar_atalho()
    print(resultado)
    input("Pressione Enter para sair...")