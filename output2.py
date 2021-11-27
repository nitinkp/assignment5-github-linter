import main

shortExceptions = ['c', 'd', 'e', 'g', 'i', 'in', 'inOut', 'j', 'k', 'm', 'n', 'o', 'out', 't', 'x', 'y', 'z']

codes = main.py_ids

# if code in shortExceptions:
for code in codes:
    outs = ""
    outs += "Short identifier names \n\n"

    for c in code:
        if len(c) < 8 and c not in shortExceptions:
            # print(code)
            outs += c + "\n"
            file1 = open(main.out2, 'w')
            # print(file_out)

            file1.write(outs)
            file1.close()

# if either starting or ending with _
for code in codes:
    outs = ""
    for c in code:
        if c[0] == '_' or c[len(c) - 1] == '_':
            outs += c + "\n"
            file1 = open(main.out2, "w")

            file1.write(outs)
            file1.close()

# print(main.list1)
