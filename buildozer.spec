[app]

# (str) Title of your application
title = My Calculator

# (str) Package name
package.name = mycalculator

# (str) Package domain (needed for android packaging)
package.domain = com.calculator

# (list) Source files to include (let it empty to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 23

# (str) Android NDK version to use
android.ndk = 25b

android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
