def generate_launch(name):
    launch = open("{}/.vscode/launch.json".format(name), 'w')
    launch.write("""{{
    "version": "0.2.0",
    "configurations": [
        {{
            "name": "(gdb) Launch",
            "type": "cppdbg",
            "request": "launch",
            "program": "${{workspaceRoot}}/{}.exe",
            "args": [],
            "stopAtEntry": false,
            "cwd": "${{workspaceRoot}}",
            "environment": [],
            "externalConsole": true,
            "MIMode": "gdb",
            "setupCommands": [
                {{
                    "description": "Enable pretty-printing for gdb",
                    "text": "-enable-pretty-printing",
                    "ignoreFailures": true
                }}
            ],
            "preLaunchTask": "build"
        }}
    ]
}}
""".format(name))
    launch.close()


def generate_tasks(name):
    tasks = open("{}/.vscode/tasks.json".format(name), 'w')
    tasks.write("""{
    // See https://go.microsoft.com/fwlink/?LinkId=733558
    // for the documentation about the tasks.json format
    "version": "2.0.0",
    "tasks": [
        {
            "taskName": "build",
            "type": "shell",
            "command": "make",
            "group": {
                "kind": "build",
                "isDefault": true
            },
            "presentation": {
                "reveal": "silent",
                "focus": true
            }
        }
    ]
}
""")
    tasks.close()


def generate_properties(name):
    cpp_properties = open("{}/.vscode/c_cpp_properties.json".format(name), 'w')
    cpp_properties.write("""{
    "configurations": [
        {
            "name": "Mac",
            "includePath": [
                "/usr/include",
                "/usr/local/include",
                "${workspaceRoot}"
            ],
            "defines": [],
            "intelliSenseMode": "clang-x64",
            "browse": {
                "path": [
                    "/usr/include",
                    "/usr/local/include",
                    "${workspaceRoot}"
                ],
                "limitSymbolsToIncludedHeaders": true,
                "databaseFilename": ""
            },
            "macFrameworkPath": [
                "/System/Library/Frameworks",
                "/Library/Frameworks"
            ]
        },
        {
            "name": "Linux",
            "includePath": [
                "/usr/include/c++/7",
                "/usr/local/include",
                "/usr/include",
                "${workspaceRoot}",
                "/usr/include/c++/7/x86_64-redhat-linux",
                "/usr/include/linux"
            ],
            "defines": [],
            "intelliSenseMode": "clang-x64",
            "browse": {
                "path": [
                    "/usr/include/c++/7",
                    "/usr/local/include",
                    "/usr/include",
                    "${workspaceRoot}"
                ],
                "limitSymbolsToIncludedHeaders": true,
                "databaseFilename": ""
            }
        },
        {
            "name": "Win32",
            "includePath": [
                "C:/Program Files (x86)/Microsoft Visual Studio 14.0/VC/include",
                "${workspaceRoot}"
            ],
            "defines": [
                "_DEBUG",
                "UNICODE"
            ],
            "intelliSenseMode": "msvc-x64",
            "browse": {
                "path": [
                    "C:/Program Files (x86)/Microsoft Visual Studio 14.0/VC/include/*",
                    "${workspaceRoot}"
                ],
                "limitSymbolsToIncludedHeaders": true,
                "databaseFilename": ""
            }
        }
    ],
    "version": 3
}
""")
    cpp_properties.close()

def generate_settings(name):
    settings = open("{}/.vscode/settings.json".format(name), 'w')
    settings.write("""{
    "files.associations": {
        "*.tcc": "cpp",
        "cctype": "cpp",
        "clocale": "cpp",
        "cmath": "cpp",
        "cstdint": "cpp",
        "cstdio": "cpp",
        "cstdlib": "cpp",
        "cwchar": "cpp",
        "cwctype": "cpp",
        "exception": "cpp",
        "initializer_list": "cpp",
        "iosfwd": "cpp",
        "iostream": "cpp",
        "istream": "cpp",
        "limits": "cpp",
        "new": "cpp",
        "ostream": "cpp",
        "stdexcept": "cpp",
        "streambuf": "cpp",
        "string_view": "cpp",
        "system_error": "cpp",
        "type_traits": "cpp",
        "typeinfo": "cpp"
    },
    "files.exclude": {
        "**/.git": true,
        "**/.svn": true,
        "**/.hg": true,
        "**/CVS": true,
        "**/.DS_Store": true,
        "**/*.o": true,
        "**/*.exe": true
    }
}
""")
    settings.close()