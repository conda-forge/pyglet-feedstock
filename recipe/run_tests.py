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
import pyglet.window
import pyglet.text
import pyglet.text.formats


# Platform-specific tests.
import sys

if sys.platform == 'win32':
    import pyglet.libs.win32
    import pyglet.window.win32
    import pyglet.media.drivers.directsound

    # skip to avoid installing audio drivers on Windows, see
    # https://www.openal.org/platforms/
    # import pyglet.media.drivers.openal
    # pyglet.media.drivers.pulse

if sys.platform == 'darwin':
    import pyglet.libs.darwin
    import pyglet.libs.darwin.cocoapy
    import pyglet.window.cocoa
    # import pyglet.media.drivers.pulse

if sys.platform == 'linux':
    import pyglet.libs.x11
    import pyglet.window.xlib
    # import pyglet.media.drivers.openal
    # import pyglet.media.drivers.pulse
