<p align="right">
<img src="https://img.shields.io/badge/Licence-MIT-brightgreen">
<img src="https://shields.io/badge/python-3.12.8-green.svg?labelColor=3670A0&logo=python&logoColor=ffdd54">
<img src="https://shields.io/badge/pyinstaller-6.15.0-green.svg?logo=python&logoColor=ffdd54">
</p>

<p align="center">
<img width="329" height="206" alt="neverbash_logo" src="https://github.com/user-attachments/assets/f16505f1-2b13-4618-a50f-2c9a7a8598bc" />
</p>

## 🤩 never bash

**どんな名称のコマンドにもまとめサイトは存在する**

注：本スクリプトはジョークスクリプトです．

## 目次

- [🔧 技術スタック](#-技術スタック)
- [⚙️ 仕様](#️-仕様)
- [🚀 HowToUse](#-howtouse)
- [🗑️ 不要になったら](#️-不要になったら)
- [✅ template.html について](#-templatehtmlについて)

## 🔧 技術スタック

<img src="https://shields.io/badge/python-3670A0.svg?logo=python&style=for-the-badge&logoColor=ffdd54">
<img src="https://shields.io/badge/html-f06529.svg?logo=html5&style=for-the-badge&logoColor=white">
<img src="https://shields.io/badge/css-36c.svg?logo=css&style=for-the-badge">

<img src="https://shields.io/badge/gemini-ffffff.svg?logo=googlegemini&style=for-the-badge&logoColor=blue">
<img src="https://shields.io/badge/wsl2-000000.svg?logo=linux&style=for-the-badge">

## ⚙️ 仕様

wsl ターミナルにてコマンドのタイプミスをすると，タイプミスしたコマンドについての架空まとめサイトが開かれます．

## 🚀 HowToUse

1. `~/.bashrc`にスクリプトをコピーする

```sh
sudo vi ~/.bashrc
```

```sh
function command_not_found_handle {
    printf "%s: command not found\n" "$1" >&2
    printf "%sというコマンドは見つかりませんでした!\nいかがでしたか?\n" "$1" >&2
    ./update_html "$1"

    # WSL内のパスをWindows形式に変換
    windows_path=$(wslpath -w "index.html_full_path_in_wsl")

    # WindowsのExplorerでHTMLファイルを開く
    powershell.exe Start-Process "explorer.exe" "\"$windows_path\""
    return 127
}
```

2. ファイルパスを置換する

```sh
# index.htmlの絶対パスを取得する
sudo find / -type f -path "*/never_bash/site/index.html" 2>/dev/null
```

取得したパスを`index.html_full_path_in_wsl`と置換する．

3. `.bashrc`の有効化

```sh
source ~/.bashrc
```

## 🗑️ 不要になったら

不要になった際には，以下の様にしてください．

```sh
function command_not_found_handle {
    printf "%s: command not found\n" "$1" >&2
    printf "%sというコマンドは見つかりませんでした!\nいかがでしたか?\n" "$1" >&2
    return 127
}
```

#### また使いたいときが来るかもしれません!!!

## ✅ template.html について

`template.html`及び`styles.css`は偉大なる Mr.Gemini が作成したものです．
ご自由にアレンジして活用してください．
