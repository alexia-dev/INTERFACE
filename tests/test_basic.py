from pathlib import Path

def test_sifac_source_exists():
    assert Path("main.py").exists()

def test_mobile_build_files_exist():
    assert Path("buildozer.spec").exists()
    assert Path(".github/workflows/build-apk.yml").exists()
