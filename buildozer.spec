[app]

# (str) Title of your application
title = SIFAC

# (str) Package name
package.name = sifac

# (str) Package domain (needed for android/ios packaging)
package.domain = org.sifac

# (str) Source code where main.py lives
source.dir = .

# (list) Source files to include
source.include_exts = py,kv,png,jpg,jpeg,atlas,ico

# (str) Application version
version = 0.1.0

# (str) Application entry point
entrypoint = main.py

# (list) List of inclusions using pattern matching
source.include_patterns = assets/*,data/*

# (list) List of exclusions
source.exclude_patterns = .git/*,.github/*,bin/*,.buildozer/*,__pycache__/*

# (str) Presplash of the application
# presplash.filename = %(source.dir)s/assets/presplash.png

# (str) Icon of the application
# icon.filename = %(source.dir)s/sistema-de-relat195179rios.ico

# (str) Supported orientation (one of landscape, sensor, portrait or all)
orientation = portrait

# (str) Supported architecture
# Leave empty to use the default supported architecture(s)
android.archs = arm64-v8a

# (str) Full name including Windows/macOS release
name = SIFAC


[buildozer]

# (int) Log level (0 = error, 1 = warning, 2 = info, 3 = debug)
log_level = 2

# (int) Warning about user data
warn_on_root = 1


[app:android]

# (str) Android API to use
android.api = 35

# (int) Minimum API supported
android.minapi = 23

# (str) Android NDK version
android.ndk = 27c

# (str) Android NDK API
android.ndk_api = 23

# (bool) Fullscreen
fullscreen = 0

# (str) Android entry point activity
android.entrypoint = org.kivy.android.PythonActivity

# (str) Android private storage
android.private_storage = True

# (str) Android shared storage
android.copy_libs = 1
