import sys

import pyglet
import pyglet.app
import pyglet.extlibs
import pyglet.libs

# Skip to avoid having to install audio drivers.
# import pyglet.media.drivers.openal
# import pyglet.media.drivers.pulse

# Upstream library loader doesn't consider CONDA_PREFIX
if sys.platform not in ['darwin', 'linux']:
    import pyglet.media.codecs.ffmpeg

# Tests currently don't work the Linux CI systems:
# pyglet.window.xlib.XlibException: Could not create UTF8 text property
if sys.platform != 'linux':
    import pyglet.media
    import pyglet.media.drivers
    import pyglet.font
    import pyglet.gl
    import pyglet.graphics
    import pyglet.image
    import pyglet.image.codecs
    import pyglet.input
    import pyglet.text
    import pyglet.text.formats
    import pyglet.window

# Platform-specific tests.
if sys.platform == 'win32':
    import pyglet.libs.win32
    import pyglet.window.win32
    import pyglet.media.drivers.directsound
elif sys.platform == 'darwin':
    import pyglet.libs.darwin
    import pyglet.libs.darwin.cocoapy
    import pyglet.window.cocoa
elif sys.platform == 'linux':
    import pyglet.libs.x11

    # Regression test for conda-forge/pyglet-feedstock#116: libGL must be
    # provided by the conda environment.
    import pyglet.lib
    pyglet.lib.load_library('GL')

    # Disabled:
    # pyglet.window.xlib.XlibException: Could not create UTF8 text property

    # import pyglet.window.xlib
