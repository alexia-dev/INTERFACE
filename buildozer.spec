[app]

title = NEXA
package.name = nexa
package.domain = org.nexa
source.dir = .
source.include_exts = py,kv,png,jpg,jpeg,atlas,ico
version = 0.2.0
entrypoint = main.py
source.include_patterns = assets/*,data/*
source.exclude_patterns = .git/*,.github/*,bin/*,.buildozer/*,__pycache__/*
orientation = portrait
android.archs = arm64-v8a
name = NEXA
requirements = python3,kivy==2.3.0,kivymd==1.2.0

[buildozer]

log_level = 2
warn_on_root = 1

[app:android]

android.api = 35
android.minapi = 23
android.ndk = 27c
android.ndk_api = 23
fullscreen = 0
android.entrypoint = org.kivy.android.PythonActivity
android.private_storage = True
android.copy_libs = 1
