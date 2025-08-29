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