import re

def generate(name):
    makefile = open("{}/Makefile".format(name), 'w')
    makefile.write("""\
#=======================================================================
# Basic C++: makefile example to use as a reminder or as a template
#-----------------------------------------------------------------------
# Julien DeAntoni --- No Copyright 2016
# $Id: convenient Makefile but muist be tuned for templated project 
#      v0.2 2016/09/06
#=======================================================================

#only ok for project with no templated classes

#compiler
COMPILER = g++
#linker
LINKER =g++

#options for linker and compiler
FLAGS =-g -ansi -Wall -Wextra -Wold-style-cast -Woverloaded-virtual -D_DEBUG_ -std=c++11

EXE_NAME= {0}.exe

#can have several ones separated by spaces, only cpp files
SOURCES = main_{0}.cpp


#PATH to extra header used in the project (when using libs not installed in the OS)
INC_PATHS= -I

#extra libs used in the project (for instance -lpthread)
LIBS	= -L 

LINKOBJ	= $(SOURCES:.cpp=.o)
SOURCEHEADERS = $(SOURCES:.cpp=.h)

all: $(EXE_NAME)

$(EXE_NAME): $(LINKOBJ)
\t$(LINKER) $(LINKOBJ) $(INC_PATHS) $(LIBS) -o $(EXE_NAME) $(FLAGS)

%.o: %.cpp %.h
\t$(COMPILER) -g -c $< -o $@ $(INC_PATHS) $(FLAGS)

# cleanup
clean:
\trm -f $(LINKOBJ)
""".format(name))
    makefile.close()


def update_sources(name_list):
    makefile = open("Makefile", 'r')
    makefile_str = makefile.readlines()
    makefile.close()

    src_regex = r"(SOURCES = .*)"

    for i in xrange(len(makefile_str)):
        if re.match(src_regex, makefile_str[i]):
            files = " ".join("{}.cpp".format(name) for name in name_list)
            makefile_str[i] = re.sub(src_regex, "\\1 " + files, makefile_str[i])

    makefile = open("Makefile", 'w')
    makefile.writelines(makefile_str)
    makefile.close()