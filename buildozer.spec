[app]
# (str) Title of your application
title = "HeartRateApp"

# (str) Package name
package.name = "heartrateapp"

# (str) Package domain (e.g. org.example)
package.domain = org.example

# (str) Source code directory (where your main.py is located)
source.dir = /workspace/heartrate-tracker/

# (list) List of source files to include (e.g. *.py, sound/*.wav)
source.include_patterns = *.py, sound/*.wav

# (list) List of directories to include (e.g. assets, sound)
source.include_dirs = 

# (str) Application versioning (method 1)
version = 1.0

# (str) Application versioning (method 2)
# version.code = 1

# (str) Application icon (relative to source.dir)
icon.filename = %(source.dir)s/icon.png

# (str) Supported orientations (one of landscape, sensorLandscape, sensorPortrait, portrait)
orientation = portrait

# (bool) List all the requirements for your app
requirements = python3,kivy,requests,playsound

# (list) List of Python packages to include (in addition to requirements)
# Note: add packages here that are required for your app
# e.g., numpy, pandas, etc.
# requirements = python3,kivy,playsound,numpy

# (bool) Include all dependencies
# e.g., https://github.com/kivy/kivy/blob/master/tools/android/requirements.txt
# e.g., kivy_deps.glew,kivy_deps.sdl2,kivy_deps.gstreamer
# requirements = python3,kivy,playsound

# (str) Path to custom Python file (e.g. custom start point)
# default is main.py
# # main.py

# (str) Path to the folder containing your icons
# # icon.filename = %(source.dir)s/icon.png

# (str) Path to the folder containing your sounds
# # sounds_dir = %(source.dir)s/sounds

# (str) Path to the folder containing your images
# # images_dir = %(source.dir)s/images

# (bool) Whether to include custom icons in the build
# # include_icons = True

# (list) List of package names to exclude from the build
# e.g., somepackage, anotherpackage
# excludes = 

# (bool) Whether to use the provided requirements (e.g., kivy_deps.glew,kivy_deps.sdl2)
# default is False
# use_deps = True

# (list) List of requirements to use (e.g., kivy_deps.glew,kivy_deps.sdl2)
# requirements = kivy_deps.glew,kivy_deps.sdl2,kivy_deps.gstreamer

# (bool) Whether to enable debug mode
# default is False
# debug = True

# (bool) Whether to use logcat to capture Android logs
# default is False
# logcat = True

# (bool) Whether to include all files in the build
# default is True
# include_all = True

# (bool) Whether to use a custom build path
# default is False
# use_custom_build_path = False

# (str) Path to the custom build path
# custom_build_path = %(source.dir)s/build

# (bool) Whether to use ADB to deploy the app to a device
# default is False
# deploy = True

# (bool) Whether to run the app on the device after deployment
# default is False
# run = True

# (bool) Whether to include test requirements in the build
# default is False
# include_test_requirements = False

# (bool) Whether to include testing files in the build
# default is False
# include_test_files = False

# (bool) Whether to include documentation files in the build
# default is False
# include_docs = False

# (bool) Whether to use a custom Python interpreter
# default is False
# custom_python = False

# (str) Path to the custom Python interpreter
# custom_python_path = /path/to/python

# (bool) Whether to enable verbose logging
# default is False
# verbose = True

# (str) Path to the custom Android SDK
# default is the default SDK path
# sdk_path = /path/to/sdk

# (str) Path to the custom Android NDK
# default is the default NDK path
# ndk_path = /path/to/ndk

# (str) Path to the custom Android Build Tools
# default is the default Build Tools path
# build_tools_path = /path/to/build-tools

# (str) Path to the custom Android Platform Tools
# default is the default Platform Tools path
# platform_tools_path = /path/to/platform-tools

# (str) Path to the custom Android Support Repository
# default is the default Support Repository path
# support_repo_path = /path/to/support-repo

# (bool) Whether to include custom Java files in the build
# default is False
# include_java_files = False

# (bool) Whether to include custom Kotlin files in the build
# default is False
# include_kotlin_files = False

# (bool) Whether to enable signing for APKs
# default is False
# signing = False

# (str) Path to the custom keystore
# keystore = /path/to/keystore

# (str) Path to the custom keystore alias
# keystore_alias = my_alias

# (str) Path to the custom keystore password
# keystore_password = my_password

# (str) Path to the custom keystore key password
# key_password = my_key_password

# (bool) Whether to enable ProGuard for APKs
# default is False
# proguard = False

# (str) Path to the custom ProGuard configuration
# proguard_config = /path/to/proguard-config

# (bool) Whether to enable obfuscation for APKs
# default is False
# obfuscation = False

# (str) Path to the custom obfuscation configuration
# obfuscation_config = /path/to/obfuscation-config

# (str) Path to the custom AndroidManifest.xml
# default is the default manifest path
# manifest_path = /path/to/AndroidManifest.xml

# (str) Path to the custom gradle.properties
# default is the default gradle.properties path
# gradle_properties_path = /path/to/gradle.properties

# (str) Path to the custom gradle-wrapper.properties
# default is the default gradle-wrapper.properties path
# gradle_wrapper_properties_path = /path/to/gradle-wrapper.properties
