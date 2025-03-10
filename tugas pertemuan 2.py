#NAMA : BILQIS ROKHIMMATUL KHAJJAH MABRUROH
#NIM : 242410101051

#NOMOR 1
import re

def is_palindrome(s):
    
    cleaned = ''.join(filter(str.isalpha, s)).lower()
    
    if len(cleaned) <= 1:
        return True
    if cleaned[0] != cleaned[-1]:
        return False
    return is_palindrome(cleaned[1:-1])

user_input = input("Masukkan sebuah string: ")

if is_palindrome(user_input):
    print("String tersebut adalah palindrom.")
else:
    print("String tersebut bukan palindrom.")


#NOMOR 2
def build_menu_tree(menu_list):
    tree = {}
    for id, parent, label in menu_list:
        tree.setdefault(parent, []).append((id, label))
    return tree

def print_menu(tree, parent=0, indent=0):
    if parent in tree:
        for id, label in sorted(tree[parent]):
            print(" " * indent + label)
            print_menu(tree, id, indent + 4)

n = int(input("Masukkan jumlah menu: "))

menu_list = []
for _ in range(n):
    id, parent, label = input().split()
    menu_list.append((int(id), int(parent), label))

menu_tree = build_menu_tree(menu_list)
print_menu(menu_tree)
