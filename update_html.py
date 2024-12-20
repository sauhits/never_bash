import sys

# template_HTMLファイルのパス
template_file_path = './site/template.html'
html_file_path ='./site/index.html'

# 置き換える値
insert_something_value = str(sys.argv[1])  # 例えば、'ls'を挿入する場合

# HTMLファイルを開いて読み込む
with open(template_file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# プレースホルダーを置き換える
updated_html_content = html_content.replace('{insert_something}', insert_something_value)

# HTMLファイルを上書き保存
with open(html_file_path, 'w', encoding='utf-8') as file:
    file.write(updated_html_content)

print("HTMLファイルが更新されました。")
