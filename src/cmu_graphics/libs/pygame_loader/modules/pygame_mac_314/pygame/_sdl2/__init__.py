if __import__("sys").platform not in ("wasi", "emscripten"):
    from ........src.cmu_graphics.libs.pygame_loader.modules.pygame_mac_314.pygame._sdl2.audio import *  # pylint: disable=wildcard-import; lgtm[py/polluting-import]
    from ........src.cmu_graphics.libs.pygame_loader.modules.pygame_mac_314.pygame._sdl2.sdl2 import *  # pylint: disable=wildcard-import; lgtm[py/polluting-import]
    from ........src.cmu_graphics.libs.pygame_loader.modules.pygame_mac_314.pygame._sdl2.video import *  # pylint: disable=wildcard-import; lgtm[py/polluting-import]
