[app]

title = NEXA Clínica
package.name = nexa
package.domain = br.com.nexa
source.dir = .
source.include_exts = py,kv,png,jpg,jpeg,atlas,ico
source.include_patterns = assets/*,data/*
source.exclude_patterns = .git/*,.github/*,bin/*,.buildozer/*,__pycache__/*,tests/*
version = 0.3.0
entrypoint = main.py
orientation = portrait
fullscreen = 0

# Python-for-Android dependencies
# Pin Python 3.12 to avoid the current Python 3.14/API 23
# preadv/pwritev compilation failure in the Docker toolchain.
requirements = python3==3.12.10,kivy==2.3.0,kivymd==1.2.0

# Use the stable p4a branch compatible with Python 3.12.
p4a.branch = master

# Android
android.archs = arm64-v8a
android.api = 35
android.sdk = 35
android.build_tools_version = 35.0.0
android.accept_sdk_license = True
android.minapi = 23
android.ndk = 27c
android.ndk_api = 23
android.entrypoint = org.kivy.android.PythonActivity
android.private_storage = True
android.copy_libs = 1
android.permissions = INTERNET

[buildozer]

log_level = 2
warn_on_root = 1
