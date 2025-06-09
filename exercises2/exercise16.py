# tlf = input("Introduce tu numero de empresa (+XX-0123456789-XX): ")
# # Aplicamos un split para que separe el str original por el caracter '-'
# tlfSplit = tlf.split('-')
# # Printamos el valor del medio que es el que continene el numero
# print(tlfSplit[1])

tlf = input("Introduce tu numero de empresa (+XX-0123456789-XX): ")

# i = 0
# flag = 0
# num = ""
# while i < len(tlf):
#     if tlf[i] == '-':
#         flag = 1
#     if flag == 1 and tlf[i] >= '0' and tlf[i] <= '9':
#         num += tlf[i]
#         if (i + 1) < len(tlf) and tlf[i + 1] == '-':
#             break
#     i += 1


num = ""
flag = False

for c in tlf:
    if c == '-' and not flag:# == False:
        flag = True
        continue
    if flag:
        if c == '-':
            break
        if c.isdigit():# c >= '0' and c <= '9':
            num += c

print(num)