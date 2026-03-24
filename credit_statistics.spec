# -*- mode: python ; coding: utf-8 -*-
"""
PyInstaller spec for 哈工程学分统计系统.
No OCR runtime dependencies are bundled.
"""

a = Analysis(
    ["credit_statistics.py"],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[
        "requests",
        "urllib3",
        "certifi",
        "charset_normalizer",
        "idna",
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=["matplotlib", "scipy", "pandas", "IPython", "notebook"],
    noarchive=False,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name="CreditStatistics",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,          # 不显示控制台窗口
    disable_windowed_traceback=False,
    argv_emulation=False,   # macOS argv emulation
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,              # 如有 .ico 文件可指定
)
