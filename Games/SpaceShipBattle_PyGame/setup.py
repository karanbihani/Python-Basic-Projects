import cx_Freeze

executables=[cx_Freeze.Executable('main.py')]

cx_Freeze.setup(
    name = "Main",
    option={'build_exe':{'packages':['pygame'],
                         'included_files':['hit.wav','gun.wav','spaceship_yellow.png','spaceship_red.png']}},
    executables=executables
    )
