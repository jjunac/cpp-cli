# C++ CLI
#### CLI for C++ project by Jeremy Junac

## Prerequisites
The CLI itself hasn't any dependencies, but if you want to use all the functionalities, you need :
* make
* gcc/g++
* gdb
* VSCode 

## Usage

### Generating a new project with Makefile and VSCode settings file
```bash
cpp-cli new PROJECT-NAME
```
This command generate a basic main with and hello world and the setting file for build, debug and launch your project, using make, gcc and gdb.

### Generating Class
You can use the ~~`cpp-cli generate`~~ (or just `cpp-cli g`) command to generate C++ classes:
```bash
#cpp-cli generate class MyClass (not working atm)
cpp-cli g class MyClass         # using the alias
```
This command create a basic cpp and header file. **The CLI will add dependency in the Makefile automatically.**<br/>
You can also create several class with one command:
```bash
#cpp-cli generate class MyFirstClass MySecondClass MyThirdClass (not working atm)
cpp-cli g class MyFirstClass MySecondClass MyThirdClass         # using the alias
```

## VSCode shortcuts

### Building

### Debugging

### Launching without debug