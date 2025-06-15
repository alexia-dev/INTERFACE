import os
import sys
import ctypes
import winreg
from pathlib import Path

def is_admin():
    """Verifica se o script está sendo executado como administrador"""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def get_desktop_path():
    """Obtém o caminho da área de trabalho com múltiplos fallbacks"""
    # 1. Tentar via registro do Windows
    try:
        with winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders"
        ) as key:
            desktop = winreg.QueryValueEx(key, "Desktop")[0]
            expanded = os.path.expandvars(desktop)
            if os.path.isdir(expanded):
                return expanded
    except Exception:
        pass
    
    # 2. Tentar caminhos comuns
    caminhos_tentativas = [
        Path.home() / "Desktop",  # Área de trabalho padrão
        Path.home() / "OneDrive" / "Desktop",  # OneDrive (inglês)
        Path.home() / "OneDrive" / "Área de Trabalho",  # OneDrive (português)
        Path("C:/Users/Public/Desktop"),  # Área de trabalho pública
        Path.home() / "Desktop",  # Tentar novamente
        Path.home()  # Último recurso: pasta do usuário
    ]
    
    for caminho in caminhos_tentativas:
        if caminho.is_dir():
            return str(caminho)
    
    # 3. Se nada funcionar, usar o diretório atual
    return os.getcwd()

def criar_atalho():
    """Cria um atalho na área de trabalho com ícone personalizado"""
    # Importar win32com.client aqui para evitar erro se não estiver instalado
    try:
        import win32com.client
    except ImportError:
        print("❌ ERRO: pywin32 não está instalado. Não é possível criar o atalho.")
        return

    # Configurações principais
    nome_atalho = "Sistema de Relatórios.lnk"
    nome_executavel = "SistemaRelatorios.exe"
    caminho_icone = r"C:\Users\moony\OneDrive\Documentos\interface\INTERFACE\sistema-de-relat195179rios.ico"
    
    # 1. Localizar o executável
    caminho_executavel = None
    locais_executavel = [
        Path("dist") / nome_executavel,  # Pasta dist
        Path(nome_executavel),  # Pasta atual
        Path("..") / "dist" / nome_executavel,  # Pasta dist superior
        Path("..") / nome_executavel  # Pasta superior
    ]
    
    for local in locais_executavel:
        if local.exists():
            caminho_executavel = str(local.resolve())
            break
    
    if not caminho_executavel:
        print("❌ ERRO: Executável não encontrado!")
        print("Execute primeiro o build.py para criar o executável")
        return
    
    # 2. Verificar ícone
    if not os.path.exists(caminho_icone):
        print(f"⚠️ AVISO: Ícone não encontrado em {caminho_icone}")
        print("Usando ícone padrão do executável")
        caminho_icone = caminho_executavel
    
    # 3. Obter caminho da área de trabalho
    desktop_path = get_desktop_path()
    caminho_atalho = os.path.join(desktop_path, nome_atalho)
    
    print(f"• Executável: {caminho_executavel}")
    print(f"• Ícone: {caminho_icone}")
    print(f"• Local do atalho: {desktop_path}")
    
    # 4. Criar atalho
    try:
        shell = win32com.client.Dispatch("WScript.Shell")
        atalho = shell.CreateShortCut(caminho_atalho)
        atalho.TargetPath = caminho_executavel
        atalho.WorkingDirectory = os.path.dirname(caminho_executavel)
        atalho.IconLocation = caminho_icone
        atalho.Description = "Sistema de Relatórios"
        atalho.save()
        
        if os.path.exists(caminho_atalho):
            print(f"\n✅ ATALHO CRIADO COM SUCESSO!")
            print(f"   Caminho: {caminho_atalho}")
            print(f"   Ícone: {caminho_icone}")
            
            # Forçar atualização do ícone
            try:
                ctypes.windll.shell32.SHChangeNotify(0x08000000, 0x0000, None, None)
            except:
                pass
        else:
            print("\n⚠️ AVISO: O atalho não foi criado. Tentando método alternativo...")
            criar_atalho_alternativo(caminho_executavel, desktop_path)
    
    except Exception as e:
        print(f"\n❌ ERRO AO CRIAR ATALHO: {str(e)}")
        criar_atalho_alternativo(caminho_executavel, desktop_path)
def criar_atalho_alternativo(caminho_exec, desktop_path):
    """Cria um arquivo BAT como alternativa se o atalho falhar"""
    try:
        bat_path = os.path.join(desktop_path, "Iniciar_Sistema.bat")
        with open(bat_path, "w") as f:
            f.write(f'@echo off\n')
            f.write(f'echo Iniciando Sistema de Relatórios...\n')
            f.write(f'start "" "{caminho_exec}"\n')
            f.write(f'pause\n')
        
        print(f"✅ ARQUIVO BAT CRIADO COMO ALTERNATIVA:")
        print(f"   Caminho: {bat_path}")
        print("   Dobre-clique neste arquivo para iniciar o sistema")
    except Exception as e:
        print(f"❌ FALHA AO CRIAR ALTERNATIVA: {str(e)}")
        print("\nSOLUÇÃO MANUAL:")
        print(f"1. Clique com botão direito na área de trabalho")
        print(f"2. Selecione 'Novo' > 'Atalho'")
        print(f"3. No campo localização, cole:")
        print(f'   "{caminho_exec}"')
        print(f"4. Nomeie como 'Sistema de Relatórios'")
        print(f"5. Clique em 'Concluir'")
        print(f"6. Clique direito no novo atalho > Propriedades")
        print(f"7. Em 'Ícone', clique em 'Alterar ícone'")
        print(f"8. Cole este caminho e selecione o ícone:")
        print(f'   {r"C:\Users\moony\OneDrive\Documentos\interface\INTERFACE\sistema-de-relat195179rios.ico"}')

if __name__ == "__main__":
    print("="*50)
    print("CRIADOR DE ATALHO PARA SISTEMA DE RELATÓRIOS")
    print("="*50)
    
    # Verificar se pywin32 está instalado
    try:
        import win32com.client
    except ImportError:
        print("\n⚠️ AVISO: A biblioteca pywin32 não está instalada.")
        print("Instalando automaticamente...")
        try:
            import subprocess
            subprocess.check_call([sys.executable, "-m", "pip", "install", "pywin32"])
            print("✅ pywin32 instalado com sucesso!")
            import win32com.client  # Tentar importar novamente
        except Exception as e:
            print(f"❌ FALHA AO INSTALAR pywin32: {str(e)}")
            print("Criando alternativa sem atalho...")
    
    criar_atalho()
    
    print("\n" + "="*50)
    input("Pressione Enter para sair...")