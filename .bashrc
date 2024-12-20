function command_not_found_handle {
    printf "%s: command not found\n" "$1" >&2
    printf "%sというコマンドは見つかりませんでした!\nいかがでしたか?\n" "$1" >&2
    python3 "(wsl)update_html" "$1"
    
    # WSL内のパスをWindows形式に変換
    windows_path=$(wslpath -w "(wsl)index.html")
    
    # WindowsのExplorerでHTMLファイルを開く
    powershell.exe Start-Process "explorer.exe" "\"$windows_path\""
    return 127
}