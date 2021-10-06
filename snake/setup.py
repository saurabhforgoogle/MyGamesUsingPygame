import cx_Freeze
executables=[cx_Freeze.Executable("snake_game.py")]
cx_Freeze.setup(
    name="snake game",
    options={"build_exe":{"packages":["pygame"],"include_files":["apple2.png","snakehead.png","snaketail.png"]}},
    description="snake game ver 1.0.3",
    executables=executables
)
