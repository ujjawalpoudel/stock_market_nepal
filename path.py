import os

path_parent = os.path.dirname(os.getcwd())
os.chdir(path_parent)

parent_folder_path = os.path.join(os.getcwd(), 'stock_excel')

if not os.path.isdir(parent_folder_path):
    os.mkdir(parent_folder_path)