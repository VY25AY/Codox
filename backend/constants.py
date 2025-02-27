LANGUAGE_VERSIONS = {
    "javascript": "18.15.0",
    "python": "3.10.0",
    "java": "15.0.2",
    "cpp": "10.2.0",
}

CODE_SNIPPETS = {
    "javascript": '''\nfunction greet(name) {\n\tconsole.log("Hello, " + name + "!");\n}\n\ngreet("Word");\n''',
    "python": '''\ndef greet(name):\n\tprint("Hello, " + name + "!")\n\ngreet("World")\n''',
    "java": '''\npublic class HelloWorld {\n\tpublic static void main(String[] args) {\n\t\tSystem.out.println("Hello World");\n\t}\n}\n''',
    "cpp": '''#include <iostream>

int main() {
    // Write C++ code here
    std::cout << "Hello World";

    return 0;
}'''
}
