[app]

title = دفاع از جزیره خارک
package.name = khargdefense
package.domain = org.kharg
version = 1.0

source.dir = .
source.include_exts = py,png,ttf,wav,txt
source.exclude_dirs = tests,tools,bin,.github,.buildozer,__pycache__

requirements = python3,pygame

orientation = landscape
fullscreen = 1
icon.filename = %(source.dir)s/assets/icon.png
presplash.filename = %(source.dir)s/assets/presplash.png
android.presplash_color = #0a1322

android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a
android.accept_sdk_license = True
android.wakelock = True
android.allow_backup = False
android.permissions =

p4a.bootstrap = sdl2
p4a.branch = v2024.01.21

[buildozer]
log_level = 2
warn_on_root = 1
