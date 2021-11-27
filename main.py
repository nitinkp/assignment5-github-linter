import requests
from tree_sitter import Language, Parser
import os
import re
from git import Repo
import stat


# print("gvwefvge")
# def rmtree(top):
#     for root, dirs, files in os.walk(top, topdown=False):
#         for name in files:
#             filename = os.path.join(root, name)
#             os.chmod(filename, stat.S_IWUSR)
#             os.remove(filename)
#         for name in dirs:
#             os.rmdir(os.path.join(root, name))
#     os.rmdir(top)
#
# rmtree('files_from_git')

site_name = input("enter public github site, remember to begin with https:// : ")
site = requests.get(site_name)
Repo.clone_from(site_name + '.git', 'files_from_git')
print(site.status_code)
py_paths = []
go_paths = []
js_paths = []
ruby_paths = []
for root, dirs, files in os.walk(r'files_from_git'):
    for file in files:
        if file.endswith('.py'):
            py_paths.append(os.path.join(root, file))
        if file.endswith('.go'):
            go_paths.append(os.path.join(root, file))
        if file.endswith('.js'):
            js_paths.append(os.path.join(root, file))
        if file.endswith('.rb'):
            ruby_paths.append(os.path.join(root, file))
# out=site.text
i = 0
print(py_paths)

py_codes = []
while (i < len(py_paths)):
    with open(py_paths[i]) as op:
        try:
            contents = op.read()

            py_codes.append(contents)
        except:
            pass
    i = i + 1


ruby_codes = []
while (i < len(ruby_paths)):
    with open(ruby_paths[i]) as rb:
        try:
            conts = rb.read()

            ruby_codes.append(conts)
        except:
            pass
    i = i + 1
js_codes = []
print(js_paths)
while (i<len(js_paths)):
    with open(js_paths[i]) as f:
        try:
            cont = f.read()
            js_codes.append(cont)
        except:
            pass
    i=i+1
go_codes = []
while (i < len(go_paths)):
    with open(go_paths[i]) as go:
        try:
            conts = go.read()

            go_codes.append(conts)
        except:
            pass
    i = i + 1

def rmtree(top):
    for root, dirs, files in os.walk(top, topdown=False):
        for name in files:
            filename = os.path.join(root, name)
            os.chmod(filename, stat.S_IWUSR)
            os.remove(filename)
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    os.rmdir(top)


rmtree('files_from_git')

Language.build_library('build/my-languages.so',
                       ['tree-sitter-go', 'tree-sitter-javascript', 'tree-sitter-python', 'tree-sitter-ruby'])
py_parser = Parser()
PYTHON_LANGUAGE = Language('build/my-languages.so', 'python')
py_parser.set_language(PYTHON_LANGUAGE)

ruby_parser = Parser()
RUBY_LANGUAGE = Language('build/my-languages.so', 'ruby')
ruby_parser.set_language(RUBY_LANGUAGE)

js_parser = Parser()
JS_LANGUAGE = Language('build/my-languages.so', 'javascript')
js_parser.set_language(JS_LANGUAGE)

go_parser = Parser()
GO_LANGUAGE = Language('build/my-languages.so', 'go')
go_parser.set_language(GO_LANGUAGE)


def parsing(source, parser):
    li = []

    def parseNode(root):
        if (len(root.children) == 0):
            return
        else:
            for i in root.children:
                if (i.type == 'identifier'):
                    li.append(i)

                parseNode(i)

    tree = parser.parse(bytes(source, "utf8"))
    root_node = tree.root_node
    parseNode(root_node)
    return li

py_ids=[]
for i in range(len(py_codes)):
    print("output for", py_paths[i])
    li = parsing(py_codes[i], py_parser)
    code = py_codes[i].split('\n')
    ids = []
    for e in li:
        row_no = e.start_point[0]
        col_no = e.start_point[1]
        print(code[row_no][col_no:e.end_point[1]], "Row No", row_no, " Column No", col_no)
        ids.append(code[row_no][col_no:e.end_point[1]])
    py_ids.append(ids)
    print("-----------------------------------------------------------------------------------")
    print('\n')

for i in range(len(ruby_codes)):
    print("output for", ruby_paths[i])
    li = parsing(ruby_codes[i], ruby_parser)
    code = ruby_codes[i].split('\n')
    ids = []
    for e in li:
        row_no = e.start_point[0]
        col_no = e.start_point[1]
        print(code[row_no][col_no:e.end_point[1]], "Row No", row_no, " Column No", col_no)
    print("-----------------------------------------------------------------------------------")
    print('\n')

for i in range(len(js_codes)):
    print("output for", js_paths[i])
    li = parsing(js_codes[i], js_parser)
    code = js_codes[i].split('\n')
    ids = []
    for e in li:
        row_no = e.start_point[0]
        col_no = e.start_point[1]
        print(code[row_no][col_no:e.end_point[1]], "Row No", row_no, " Column No", col_no)
    print("-----------------------------------------------------------------------------------")
    print('\n')

for i in range(len(go_codes)):
    print("output for", go_paths[i])
    li = parsing(go_codes[i], go_parser)
    code = go_codes[i].split('\n')
    ids = []
    for e in li:
        row_no = e.start_point[0]
        col_no = e.start_point[1]
        print(code[row_no][col_no:e.end_point[1]], "Row No", row_no, " Column No", col_no)
    print("-----------------------------------------------------------------------------------")
    print('\n')

# for id in py_ids:
#     for i in id:
#         if len(id)>

# language=input("enter programming language : ")
# allowed=['python','ruby','javascript','ruby','go']
# if language in allowed:
#  print("allowed")
#
# else:
#     print("language not in allowed list of languages")
#
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
