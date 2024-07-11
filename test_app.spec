# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['src\\win.py'],
    pathex=[],
    binaries=[],
    datas=[('src\\public\\icon.ico', '.')],
    hiddenimports=['numpy', 'pandas', 'numpy.core._methods', 'numpy.lib.format'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['PyQt5', 'tensorflow', 'torch', 'pyinstaller', 'pip'],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='text_dash0711_console',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    uac_admin=True,
    icon=['src\\public\\icon.ico'],
)
