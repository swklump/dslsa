# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['application.py'],
             pathex=['C:\\Users\\sklump\\OneDrive - DOWL Exchange 365\\Soils Library'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=['certifi','etc','IPython','jedi','jsonschema','lxml','markupsafe','matplotlib','nbconvert','nbformat','notebook','PIL','scipy','share','shiboken2','tcl','tcl8','tk','tornado','wcwidth','zmq'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts, 
          [],
          exclude_binaries=True,
          name='application',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None , icon='png\\icon.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas, 
               strip=False,
               upx=True,
               upx_exclude=[],
               name='application')
