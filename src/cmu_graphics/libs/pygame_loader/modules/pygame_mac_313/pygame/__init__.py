# pygame - Python Game Library
# Copyright (C) 2000-2001  Pete Shinners
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Library General Public
# License as published by the Free Software Foundation; either
# version 2 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Library General Public License for more details.
#
# You should have received a copy of the GNU Library General Public
# License along with this library; if not, write to the Free
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
# Pete Shinners
# pete@shinners.org
"""Pygame is a set of Python modules designed for writing games.
It is written on top of the excellent SDL library. This allows you
to create fully featured games and multimedia programs in the python
language. The package is highly portable, with games running on
Windows, MacOS, OS X, BeOS, FreeBSD, IRIX, and Linux."""

import sys
import os

# Choose Windows display driver
if os.name == "nt":
    pygame_dir = os.path.split(__file__)[0]

    # pypy does not find the dlls, so we add package folder to PATH.
    os.environ["PATH"] = os.environ["PATH"] + ";" + pygame_dir

    # windows store python does not find the dlls, so we run this
    if sys.version_info > (3, 8):
        os.add_dll_directory(pygame_dir)  # only available in 3.8+

    # cleanup namespace
    del pygame_dir

# when running under X11, always set the SDL window WM_CLASS to make the
#   window managers correctly match the pygame window.
elif "DISPLAY" in os.environ and "SDL_VIDEO_X11_WMCLASS" not in os.environ:
    os.environ["SDL_VIDEO_X11_WMCLASS"] = os.path.basename(sys.argv[0])


def _attribute_undefined(name):
    raise RuntimeError(f"{name} is not available")


class MissingModule:
    _NOT_IMPLEMENTED_ = True

    def __init__(self, name, urgent=0):
        self.name = name
        exc_type, exc_msg = sys.exc_info()[:2]
        self.info = str(exc_msg)
        self.reason = f"{exc_type.__name__}: {self.info}"
        self.urgent = urgent
        if urgent:
            self.warn()

    def __getattr__(self, var):
        if not self.urgent:
            self.warn()
            self.urgent = 1
        missing_msg = f"{self.name} module not available ({self.reason})"
        raise NotImplementedError(missing_msg)

    def __bool__(self):
        return False

    def warn(self):
        msg_type = "import" if self.urgent else "use"
        message = f"{msg_type} {self.name}: {self.info}\n({self.reason})"
        try:
            import warnings

            level = 4 if self.urgent else 3
            warnings.warn(message, RuntimeWarning, level)
        except ImportError:
            print(message)


# we need to import like this, each at a time. the cleanest way to import
# our modules is with the import command (not the __import__ function)
# isort: skip_file

# first, the "required" modules
from src.cmu_graphics.libs.pygame_loader.modules.pygame_mac_313.pygame.base import *  # pylint: disable=wildcard-import; lgtm[py/polluting-import]
from src.cmu_graphics.libs.pygame_loader.modules.pygame_mac_313.pygame.constants import *  # now has __all__ pylint: disable=wildcard-import; lgtm[py/polluting-import]
from src.cmu_graphics.libs.pygame_loader.modules.pygame_mac_313.pygame.version import *  # pylint: disable=wildcard-import; lgtm[py/polluting-import]
from src.cmu_graphics.libs.pygame_loader.modules.pygame_mac_313.pygame.rect import Rect
from src.cmu_graphics.libs.pygame_loader.modules.pygame_mac_313.pygame.rwobject import encode_string, encode_file_path
import src.cmu_graphics.libs.pygame_loader.modules.pygame_mac_313.pygame.surflock
import src.cmu_graphics.libs.pygame_loader.modules.pygame_mac_313.pygame.color

Color = src.cmu_graphics.libs.pygame_loader.modules.pygame_mac_313.pygame.color.Color
import src.cmu_graphics.libs.pygame_loader.modules.pygame_mac_313.pygame.bufferproxy

BufferProxy = src.cmu_graphics.libs.pygame_loader.modules.pygame_mac_313.pygame.bufferproxy.BufferProxy
import src.cmu_graphics.libs.pygame_loader.modules.pygame_mac_313.pygame.math

Vector2 = src.cmu_graphics.libs.pygame_loader.modules.pygame_mac_313.pygame.math.Vector2
Vector3 = src.cmu_graphics.libs.pygame_loader.modules.pygame_mac_313.pygame.math.Vector3

__version__ = ver

# next, the "standard" modules
# we still allow them to be missing for stripped down pygame distributions
if get_sdl_version() < (2, 0, 0):
    # cdrom only available for SDL 1.2.X
    try:
        import pygame.cdrom
    except (ImportError, OSError):
        cdrom = MissingModule("cdrom", urgent=1)

try:
    import src.cmu_graphics.libs.pygame_loader.modules.pygame_mac_313.pygame.display
except (ImportError, OSError):
    display = MissingModule("display", urgent=1)

try:
    import src.cmu_graphics.libs.pygame_loader.modules.pygame_mac_313.pygame.draw
except (ImportError, OSError):
    draw = MissingModule("draw", urgent=1)

try:
    import src.cmu_graphics.libs.pygame_loader.modules.pygame_mac_313.pygame.event
except (ImportError, OSError):
    event = MissingModule("event", urgent=1)

try:
    import src.cmu_graphics.libs.pygame_loader.modules.pygame_mac_313.pygame.image
except (ImportError, OSError):
    image = MissingModule("image", urgent=1)

try:
    import src.cmu_graphics.libs.pygame_loader.modules.pygame_mac_313.pygame.joystick
except (ImportError, OSError):
    joystick = MissingModule("joystick", urgent=1)

try:
    import src.cmu_graphics.libs.pygame_loader.modules.pygame_mac_313.pygame.key
except (ImportError, OSError):
    key = MissingModule("key", urgent=1)

try:
    import src.cmu_graphics.libs.pygame_loader.modules.pygame_mac_313.pygame.mouse
except (ImportError, OSError):
    mouse = MissingModule("mouse", urgent=1)

try:
    import src.cmu_graphics.libs.pygame_loader.modules.pygame_mac_313.pygame.cursors
    from src.cmu_graphics.libs.pygame_loader.modules.pygame_mac_313.pygame.cursors import Cursor
except (ImportError, OSError):
    cursors = MissingModule("cursors", urgent=1)

    def Cursor(*args):  # pylint: disable=unused-argument
        _attribute_undefined("pygame.Cursor")


try:
    import src.cmu_graphics.libs.pygame_loader.modules.pygame_mac_313.pygame.sprite
except (ImportError, OSError):
    sprite = MissingModule("sprite", urgent=1)

try:
    import src.cmu_graphics.libs.pygame_loader.modules.pygame_mac_313.pygame.threads
except (ImportError, OSError):
    threads = MissingModule("threads", urgent=1)

try:
    import src.cmu_graphics.libs.pygame_loader.modules.pygame_mac_313.pygame.pixelcopy
except (ImportError, OSError):
    pixelcopy = MissingModule("pixelcopy", urgent=1)


try:
    from src.cmu_graphics.libs.pygame_loader.modules.pygame_mac_313.pygame.surface import Surface, SurfaceType
except (ImportError, OSError):

    def Surface(size, flags, depth, masks):  # pylint: disable=unused-argument
        _attribute_undefined("pygame.Surface")

    SurfaceType = Surface

try:
    import src.cmu_graphics.libs.pygame_loader.modules.pygame_mac_313.pygame.mask
    from src.cmu_graphics.libs.pygame_loader.modules.pygame_mac_313.pygame.mask import Mask
except (ImportError, OSError):
    mask = MissingModule("mask", urgent=0)

    def Mask(size, fill):  # pylint: disable=unused-argument
        _attribute_undefined("pygame.Mask")


try:
    from src.cmu_graphics.libs.pygame_loader.modules.pygame_mac_313.pygame.pixelarray import PixelArray
except (ImportError, OSError):

    def PixelArray(surface):  # pylint: disable=unused-argument
        _attribute_undefined("pygame.PixelArray")


try:
    from pygame.overlay import Overlay
except (ImportError, OSError):

    def Overlay(format, size):  # pylint: disable=unused-argument
        _attribute_undefined("pygame.Overlay")


try:
    import src.cmu_graphics.libs.pygame_loader.modules.pygame_mac_313.pygame.time
except (ImportError, OSError):
    time = MissingModule("time", urgent=1)

try:
    import src.cmu_graphics.libs.pygame_loader.modules.pygame_mac_313.pygame.transform
except (ImportError, OSError):
    transform = MissingModule("transform", urgent=1)

# lastly, the "optional" pygame modules
if "PYGAME_FREETYPE" in os.environ:
    try:
        import src.cmu_graphics.libs.pygame_loader.modules.pygame_mac_313.pygame.ftfont as font

        sys.modules["pygame.font"] = font
    except (ImportError, OSError):
        pass
try:
    import src.cmu_graphics.libs.pygame_loader.modules.pygame_mac_313.pygame.font
    import src.cmu_graphics.libs.pygame_loader.modules.pygame_mac_313.pygame.sysfont

    src.cmu_graphics.libs.pygame_loader.modules.pygame_mac_313.pygame.font.SysFont = src.cmu_graphics.libs.pygame_loader.modules.pygame_mac_313.pygame.sysfont.SysFont
    src.cmu_graphics.libs.pygame_loader.modules.pygame_mac_313.pygame.font.get_fonts = src.cmu_graphics.libs.pygame_loader.modules.pygame_mac_313.pygame.sysfont.get_fonts
    src.cmu_graphics.libs.pygame_loader.modules.pygame_mac_313.pygame.font.match_font = src.cmu_graphics.libs.pygame_loader.modules.pygame_mac_313.pygame.sysfont.match_font
except (ImportError, OSError):
    font = MissingModule("font", urgent=0)

# try and load pygame.mixer_music before mixer, for py2app...
try:
    import src.cmu_graphics.libs.pygame_loader.modules.pygame_mac_313.pygame.mixer_music

    # del pygame.mixer_music
    # print("NOTE2: failed importing pygame.mixer_music in lib/__init__.py")
except (ImportError, OSError):
    pass

try:
    import src.cmu_graphics.libs.pygame_loader.modules.pygame_mac_313.pygame.mixer
except (ImportError, OSError):
    mixer = MissingModule("mixer", urgent=0)

try:
    import src.cmu_graphics.libs.pygame_loader.modules.pygame_mac_313.pygame.scrap
except (ImportError, OSError):
    scrap = MissingModule("scrap", urgent=0)

try:
    import src.cmu_graphics.libs.pygame_loader.modules.pygame_mac_313.pygame.surfarray
except (ImportError, OSError):
    surfarray = MissingModule("surfarray", urgent=0)

try:
    import src.cmu_graphics.libs.pygame_loader.modules.pygame_mac_313.pygame.sndarray
except (ImportError, OSError):
    sndarray = MissingModule("sndarray", urgent=0)

try:
    import src.cmu_graphics.libs.pygame_loader.modules.pygame_mac_313.pygame.fastevent
except (ImportError, OSError):
    fastevent = MissingModule("fastevent", urgent=0)

# there's also a couple "internal" modules not needed
# by users, but putting them here helps "dependency finder"
# programs get everything they need (like py2exe)
try:
    import pygame.imageext

    del pygame.imageext
except (ImportError, OSError):
    pass

# this internal module needs to be included for dependency
# finders, but can't be deleted, as some tests need it
try:
    import src.cmu_graphics.libs.pygame_loader.modules.pygame_mac_313.pygame.pkgdata

except (ImportError, OSError):
    pass


def packager_imports():
    """some additional imports that py2app/py2exe will want to see"""
    import atexit
    import numpy
    import OpenGL.GL
    import src.cmu_graphics.libs.pygame_loader.modules.pygame_mac_313.pygame.macosx
    import src.cmu_graphics.libs.pygame_loader.modules.pygame_mac_313.pygame.colordict


# make Rects pickleable

import copyreg


def __rect_constructor(x, y, w, h):
    return Rect(x, y, w, h)


def __rect_reduce(r):
    assert isinstance(r, Rect)
    return __rect_constructor, (r.x, r.y, r.w, r.h)


copyreg.pickle(Rect, __rect_reduce, __rect_constructor)


# make Colors pickleable
def __color_constructor(r, g, b, a):
    return Color(r, g, b, a)


def __color_reduce(c):
    assert isinstance(c, Color)
    return __color_constructor, (c.r, c.g, c.b, c.a)


copyreg.pickle(Color, __color_reduce, __color_constructor)

# Thanks for supporting pygame. Without support now, there won't be pygame later.
if "PYGAME_HIDE_SUPPORT_PROMPT" not in os.environ:
    print(
        "pygame {} (SDL {}.{}.{}, Python {}.{}.{})".format(  # pylint: disable=consider-using-f-string
            ver, *get_sdl_version() + sys.version_info[0:3]
        )
    )
    print("Hello from the pygame community. https://www.pygame.org/contribute.html")

# cleanup namespace
del src.cmu_graphics.libs.pygame_loader.modules.pygame_mac_313.pygame, os, sys, MissingModule, copyreg, packager_imports
