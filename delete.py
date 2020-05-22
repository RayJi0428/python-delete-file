import codecs
import os

delete_file = codecs.open(os.path.join(os.getcwd(),'delete.txt'), 'r', encoding='utf-8')
delete_list = delete_file.read().split(",")
delete_file.close()

def removeFile(delete_path):
    print('delete:' + delete_path)
    if os.path.exists(delete_path):
        os.remove(delete_path)

for v in delete_list:
    if v == '':
        print('無刪除目標')
        break
    abs_path = os.path.join(os.getcwd(), v)
    removeFile(abs_path)

    ext = os.path.basename(abs_path).split('.')[1]
    if ext == 'jpg':
        removeFile(abs_path.replace('.jpg', '.webp'))
    elif ext == 'png':
        removeFile(abs_path.replace('.png', '.webp'))

input('刪除完畢')
