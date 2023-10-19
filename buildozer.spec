[app]
# Title of your application
title = IP Lookup

# Package name
package.name = iplookup

# Main python source file
source.main = main.py

# Minimum SDK version
android.minapi = 21

# Required permissions
android.permissions = INTERNET, ACCESS_NETWORK_STATE, ACCESS_WIFI_STATE

# Buildozer spec inheritance
inherit = buildozer.spec

# Kivy requirements
requirements = kivy==2.0.0,kivymd==0.104.2,hostpython3

# Android arch to build for
android.arch = armeabi-v7a

# Fullscreen
fullscreen = 1

# Icon
icon.filename = k1.png

# Loading image
android.loading_img = k2.png

# Splash image
android.splash_img = k3.png

# Android API target
android.api = 33

# OUYA Console support
#android.ouya.icon.filename = %(source.dir)s/data/ouya_icon.png
#android.ouya.launcher_header.filename = %(source.dir)s/data/ouya_launcher_header.png
#android.ouya.banner.filename = %(source.dir)s/data/ouya_banner.png

# Android NDK build
#android.ndk = 19c

# Android NDK API level
#android.ndk_api = 21

# Android SDK version
#android.sdk = 33

# ANT+ support
#android.ant = True

# If False, do not autorun the app after build
#android.ephemeral = True

# Blacklist some devices
android.blacklist = samsung-GT-I9100,samsung-SGH-T989,lge-LG-P925

# List of Java .jar files to include
#android.add_jars = foo.jar,bar.jar

# List of Java packages to include
#android.add_src = org.foo,org.foo.bar

# Disables compilation with pycrystax, only works with Hostpython
#android.crystax_ignore = True

# File extensions for which compression should not be used
#android.no_compress_ext = .ogg, .wav, .mp3

# Source directory (your Python script location)
source.dir = .

# Version number (static version)
version = 1.0
