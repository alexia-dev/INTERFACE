from pathlib import Path


def test_nexa_source_exists():
    assert Path("main.py").exists()
    assert Path("app.py").exists()
    assert Path("build.py").exists()


def test_mobile_build_files_exist():
    assert Path("buildozer.spec").exists()
    assert Path(".github/workflows/build-apk.yml").exists()


def test_windows_build_file_exists():
    assert Path(".github/workflows/build-windows.yml").exists()
    assert Path("ui/theme.kv").exists()


def test_modular_frontend_exists():
    for path in (
        "ui/theme.kv",
        "ui/app.kv",
        "ui/home.kv",
        "ui/instrua.kv",
        "ui/bill.kv",
        "ui/admin.kv",
        "ui/central.kv",
        "screens/instrua.py",
        "screens/bill.py",
        "repositories/appointments.py",
        "repositories/billing.py",
        "core/database.py",
    ):
        assert Path(path).exists()


def test_public_repo_does_not_embed_real_patient_data():
    forbidden = ["cpf", "rg", "cns", "patient_document", "document_number"]
    targets = [
        Path("main.py"),
        Path("README.md"),
        Path(".github/workflows/ci.yml"),
    ]
    text = "\n".join(
        p.read_text(encoding="utf-8")
        for p in targets
        if p.exists()
    ).lower()
    import re

    for token in forbidden:
        # Match identifier-like tokens, not arbitrary substrings such as "rg"
        # inside unrelated words like "organizações".
        assert re.search(rf"(?<![a-z0-9_]){re.escape(token)}(?![a-z0-9_])", text) is None
