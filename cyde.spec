# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['C:/Users/Phill-Al/Desktop/code/cyde/cyde.py'],
    pathex=[],
    binaries=[],
    datas=[('C:/Users/Phill-Al/Desktop/code/cyde/bin', 'bin/')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
splash = Splash(
    'C:/Users/Phill-Al/Desktop/code/cyde/splash.png',
    binaries=a.binaries,
    datas=a.datas,
    text_pos=(10, 420),
    text_size=12,
    text_color='black',
    minify_script=True,
    always_on_top=True,
)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    splash,
    splash.binaries,
    [],
    name='cyde',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='C:\\Users\\Phill-Al\\Desktop\\code\\cyde\\logo.ico',
)
