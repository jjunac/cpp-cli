def generate_main(name):
    main_cpp = open("{0}/main_{0}.cpp".format(name), 'w')
    main_cpp.write("""#include <iostream>
#include <string>

using std::string;
using std::cout;
using std::cin;
using std::endl;

int main() {{

    cout << \"{}\" << endl;

    return 0;
}}
""".format(name))
    main_cpp.close()


def generate_class(name):
    cpp = open("{}.cpp".format(name), 'w')
    cpp.write("""#include "{}.h"
""".format(name))
    cpp.close()


def generate_header(name):
    header = open("{}.h".format(name), 'w')
    define = "{}_H_".format("".join(map(lambda c: c.upper() if c.islower() else "_" + c, name)))
    header.write("""#ifndef {0}
#define {0}

class {1} {{

}};

#endif
""".format(define, name))
    header.close()