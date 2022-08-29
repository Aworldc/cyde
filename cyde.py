import os, sys, subprocess
import pyi_splash as sp
sp.update_text("patching...")
def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

binpaths = '{};{};{};{};{};'.format(
    resource_path("bin/git/bin"),
    resource_path("bin/node"),
    resource_path("bin/python"),
    resource_path("bin/vscodium"),
    resource_path("bin/vscodium/bin")
)

envi = os.environ.copy()
envi["PATH"] = binpaths + envi["PATH"]

sp.update_text("starting vsloader...")
subprocess.Popen(resource_path("bin/vsloader.cmd"), env=envi, shell=True).wait()