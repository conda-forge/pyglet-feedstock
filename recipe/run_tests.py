import pyglet
import pyglet.app
import pyglet.canvas
import pyglet.extlibs
import pyglet.libs
import pyglet.font
import pyglet.gl
import pyglet.graphics
import pyglet.image
import pyglet.image.codecs
import pyglet.input
import pyglet.media
import pyglet.media.drivers
import pyglet.media.codecs.ffmpeg
import pyglet.window
import pyglet.text
import pyglet.text.formats

# Skip to avoid having to install audio drivers.
# import pyglet.media.drivers.openal
# import pyglet.media.drivers.pulse

# Platform-specific tests.
import sys

if sys.platform == 'win32':
    import pyglet.libs.win32
    import pyglet.window.win32
    import pyglet.media.drivers.directsound

if sys.platform == 'darwin':
    import pyglet.libs.darwin
    import pyglet.libs.darwin.cocoapy
    import pyglet.window.cocoa

if sys.platform == 'linux':
    import pyglet.libs.x11
    import pyglet.window.xlib
