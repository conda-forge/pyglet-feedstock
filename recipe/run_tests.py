import sys

import pyglet
import pyglet.app
import pyglet.canvas
import pyglet.extlibs
import pyglet.libs
import pyglet.image
import pyglet.image.codecs
import pyglet.input
import pyglet.media
import pyglet.media.drivers
if sys.platform != 'darwin':  # FIXME: Upstream library loader doesn't consider CONDA_PREFIX
    import pyglet.media.codecs.ffmpeg
import pyglet.window
import pyglet.text
import pyglet.text.formats

# Skip to avoid having to install audio drivers.
# import pyglet.media.drivers.openal
# import pyglet.media.drivers.pulse

# Test currently doesn't work on the Linux CI systems
if sys.platform != 'linux':
    import pyglet.font
    import pyglet.gl
    import pyglet.graphics

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
    import pyglet.window.xlib
