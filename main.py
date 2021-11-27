import requests
from tree_sitter import Language, Parser
import os
from git import Repo
import stat

folder_name = 'files_from_git'

try:
    def folder_remover(foldername):
        for first, second, third in os.walk(foldername, topdown=False):
            for j in third:
                filename = os.path.join(first, j)
                os.chmod(filename, stat.S_IWUSR)
                os.remove(filename)
            for j in second:
                os.rmdir(os.path.join(first, j))

        os.rmdir(foldername)


    folder_remover(folder_name)

except:
    pass

site_name = input("enter public github site, remember to begin with https:// : ")
site = requests.get(site_name)
git_site = site_name + ".git"
Repo.clone_from(git_site, folder_name)
print(site.status_code)  # successful connection

extension = input("enter the file extension: whether .py or .js or .go or .rb:  ")
ex_allowed = ['.py', '.js', '.go', '.rb']
if extension in ex_allowed:
    print("allowed extension")
else:
    print("extension not in allowed list of extension")

language = input("enter programming language : ")
allowed = ['python', 'ruby', 'javascript', 'go']
if language in allowed:
    print("allowed language")
else:
    print("language not in allowed list of languages")

out1 = input("Enter the text file to write output 1:  ")
if len(out1) == 0:
    print("Please enter file for output1")

out2 = input("Enter the text file to write output 2:  ")
if len(out2) == 0:
    print("Please enter file for output2")

py_links = []
ruby_links = []
js_links = []
go_links = []

for f1, f2, f3 in os.walk(r'files_from_git'):
    for file in f3:
        if file.endswith('.py'):
            py_links.append(os.path.join(f1, file))
        if file.endswith('.go'):
            go_links.append(os.path.join(f1, file))
        if file.endswith('.js'):
            js_links.append(os.path.join(f1, file))
        if file.endswith('.rb'):
            ruby_links.append(os.path.join(f1, file))
# out=site.text
i = 0
# print(py_paths)

py_text = []
while i < len(py_links):
    with open(py_links[i]) as op:
        try:
            contents = op.read()

            py_text.append(contents)
        except:
            pass
    i = i + 1

ruby_text = []
i = 0
while i < len(ruby_links):
    with open(ruby_links[i]) as r:
        try:
            cons = r.read()

            ruby_text.append(cons)
        except:
            pass
    i = i + 1

js_text = []
# print(js_paths)
i = 0
while i < len(js_links):
    with open(js_links[i]) as f:
        try:
            cont = f.read()
            js_text.append(cont)
        except:
            pass
    i = i + 1

go_text = []
i = 0
while i < len(go_links):
    with open(go_links[i]) as g:
        try:
            con = g.read()
            go_text.append(con)
        except:
            pass
    i = i + 1


#
# print("helloo")
# print(go_codes)
# print(go_paths)

def folder_remover(folder_to_remove):
    for root, dirs, files in os.walk(folder_to_remove, topdown=False):
        for name in files:
            filename = os.path.join(root, name)
            os.chmod(filename, stat.S_IWUSR)
            os.remove(filename)
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    os.rmdir(folder_to_remove)


folder_remover(folder_name)

Language.build_library('build/my-languages.so',
                       ['tree-sitter-go', 'tree-sitter-javascript', 'tree-sitter-python', 'tree-sitter-ruby'])

# python
py_parser = Parser()
PYTHON_LANGUAGE = Language('build/my-languages.so', 'python')
py_parser.set_language(PYTHON_LANGUAGE)

# ruby
ruby_parser = Parser()
RUBY_LANGUAGE = Language('build/my-languages.so', 'ruby')
ruby_parser.set_language(RUBY_LANGUAGE)

# javascript
js_parser = Parser()
JS_LANGUAGE = Language('build/my-languages.so', 'javascript')
js_parser.set_language(JS_LANGUAGE)

# go
go_parser = Parser()
GO_LANGUAGE = Language('build/my-languages.so', 'go')
go_parser.set_language(GO_LANGUAGE)


def parser(source, parser1):
    list1 = []

    def node_parser(root1):
        if len(root1.children) != 0:
            for j in root1.children:
                if j.type == 'identifier':
                    list1.append(j)

                node_parser(j)
        else:
            return

    tree_name = parser1.parse(bytes(source, "utf8"))
    root_node = tree_name.root_node
    node_parser(root_node)
    # print(list1)
    return list1


py_ids = []


def py_printer():
    file_out = ""
    for i in range(len(py_text)):
        # print("output for", py_paths[i])
        py_list = parser(py_text[i], py_parser)
        code = py_text[i].split('\n')
        ids = []

        file_out += "\noutput for: " + str(py_links[i]) + "\n\n"
        for e in py_list:
            row = e.start_point[0]
            col = e.start_point[1]
            # print(code[row][col:e.end_point[1]], "Row Num", row, " Column Num", col)

            file_out += code[row][col:e.end_point[1]] + "   row num: " + str(row) + "   col num: " \
                        + str(col) + "\n"
            file1 = open(out1, 'w')
            # print(file_out)

            file1.write(file_out)
            file1.close()
            ids.append(code[row][col:e.end_point[1]])
        py_ids.append(ids)

        # file1 = open(out1, 'a')
        #
        # for id in py_ids:
        #
        #     for i in id:
        #         i=i+'\n'
        #         file1.write(i)

        # print("**********************************************")
        # print('\n')


# file1 = open(out1, 'w')
# for id in py_ids:
#     print(id)


def ruby_printer():
    file_out = ""
    for i in range(len(ruby_text)):
        file_out += "\noutput for: " + str(ruby_links[i]) + "\n\n"
        # print("output for", ruby_paths[i])
        ruby_list = parser(ruby_text[i], ruby_parser)
        code = ruby_text[i].split('\n')
        ids = []
        for e in ruby_list:
            row = e.start_point[0]
            col = e.start_point[1]
            file_out += code[row][col:e.end_point[1]] + "   row num: " + str(row) + "   col num: " \
                        + str(col) + "\n"
            # print(file_out)
            file1 = open(out1, 'w')
            # print(file_out)

            file1.write(file_out)
            file1.close()
        #     print(code[row][col:e.end_point[1]], "Row Num", row, " Column Num", col)
        # print("**********************************************")
        # print('\n')


def js_printer():
    file_out = ""
    for i in range(len(js_text)):
        file_out += "\noutput for: " + str(js_links[i]) + "\n\n"
        # print("output for", js_paths[i])
        js_list = parser(js_text[i], js_parser)
        code = js_text[i].split('\n')
        ids = []
        for e in js_list:
            row = e.start_point[0]
            col = e.start_point[1]
            file_out += code[row][col:e.end_point[1]] + "   row num: " + str(row) + "   col num: " \
                        + str(col) + "\n"
            file1 = open(out1, 'w')
            # print(file_out)

            file1.write(file_out)
            file1.close()
        #     print(code[row][col:e.end_point[1]], "Row Num", row, " Column Num", col)
        # print("**********************************************")
        # print('\n')


def go_printer():
    file_out = ""
    # print("nithin")
    # print(go_text)
    for i in range(len(go_text)):
        file_out += "\noutput for: " + str(go_links[i]) + "\n\n"
        # print("output for", go_paths[i])
        go_list = parser(go_text[i], go_parser)
        # print(go_list)
        code = go_text[i].split('\n')
        ids = []
        for e in go_list:
            row = e.start_point[0]
            col = e.start_point[1]
            file_out += code[row][col:e.end_point[1]] + "   row num: " + str(row) + "   col num: " \
                        + str(col) + "\n"
            file1 = open(out1, 'w')
            # print(file_out)

            file1.write(file_out)
            file1.close()
        #     print(code[row][col:e.end_point[1]], "Row Num", row, " Column Num", col)
        # print("**********************************************")
        # print('\n')


if language == "python":
    py_printer()
elif language == "ruby":
    ruby_printer()
elif language == "javascript":
    js_printer()
elif language == "go":
    # print("hello")
    go_printer()
else:
    print("Enter languages that are allowed")

# file1 = open(out1,'w')
# file1.write("haha")

# for id in py_ids:
#     for i in id:
#         if len(id)>


# violations=["Capitalisation","Double underscores","Dictionary words","excessive words","enum identifer","external underscores","long id names","naming convention anomally","number of words","numeric identifier","short identifier"]
#
# print("Create a file named newfile and newfile2 in the root directory C:/ in windows\n")
# print ("changing directory from \n")
# print(os.getcwd())
# print("to root directory")
# os.chdir("/")
# try:
#     file=open('newfile.txt',"r+")
#     file.write(out)
#     file2=open('newfile2.txt',"r+")
#     file2.write(violations)
# except:
#     print("create the files then try again")
# #query = PY_LANGUAGE.query
# ("""
# (function_definition
#   name: (identifier) @function.def)
#
# (call
#   function: (identifier) @function.call)
# """)
# #checks 100 lines of code for identifiers
# ##captures = query.captures(tree.root_node)
# ##assert len(captures) == 100
# ##assert captures[0][0] == function_name_node
# ##assert captures[0][99] == "function.def"
# print("violations from parsed file\n")
# for x in violations:
#
#     print(x,'\n')
