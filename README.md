# WebP Image Generator CLI

一個用於產生指定尺寸、背景顏色的 WebP 測試圖片的命令列工具。圖片中央會顯示固定文字 `TEST IMAGE`，適用於網站圖片處理、上傳、轉檔、縮圖等功能測試。

## 功能特色

- 自訂圖片尺寸（寬度、高度）
- 多種預設背景顏色
- 自動置中顯示測試文字
- 輸出 WebP 格式
- 可打包為獨立執行檔

## 安裝

### 環境要求

- Python 3.8 以上
- Pillow 套件

### 安裝依賴

```bash
pip install -r requirements.txt
```

## 使用方式

### 基本執行

```bash
python webp_generate_cli.py [--width 寬度] [--height 高度] [--bg 背景顏色] [--out 輸出檔名]
```

### 參數說明

| 參數 | 型別 | 預設值 | 說明 |
|------|------|--------|------|
| `--width` | 整數 | 1160 | 圖片寬度（像素） |
| `--height` | 整數 | 624 | 圖片高度（像素） |
| `--bg` | 字串 | white | 背景顏色（限定選項） |
| `--out` | 字串 | test_image.webp | 輸出檔案名稱 |

### 可用背景顏色

| 顏色名稱 | RGB 值 |
|----------|--------|
| white | (255, 255, 255) |
| black | (0, 0, 0) |
| gray | (128, 128, 128) |
| blue | (0, 120, 215) |
| red | (200, 30, 30) |
| green | (0, 158, 47) |
| yellow | (255, 221, 0) |

## 使用範例

### 使用預設值產生圖片

```bash
python webp_generate_cli.py
```

### 指定尺寸與背景顏色

```bash
python webp_generate_cli.py --width 1024 --height 768 --bg gray
```

### 完整指定所有參數

```bash
python webp_generate_cli.py --width 640 --height 480 --bg green --out images/test_640x480.webp
```

## 打包成執行檔

若需要打包成 Windows 執行檔：

```bash
pip install pyinstaller
pyinstaller --onefile webp_generate_cli.py
```

產生後的執行檔位於 `dist/webp_generate_cli.exe`。

執行打包後的執行檔：

```bash
# Windows PowerShell
./webp_generate_cli.exe --width 800 --height 600 --bg blue
```

## 輸出結果

- 產生一張 `.webp` 格式圖片
- 圖片尺寸符合指定的寬度與高度
- 背景顏色符合指定的顏色
- 圖片中央顯示黑色文字 `TEST IMAGE`

## 注意事項

- `--bg` 參數僅接受預定義的顏色，輸入其他值會顯示錯誤並結束程式
- `--width` 或 `--height` 應為正整數
- 若輸出路徑不存在或無寫入權限，檔案將無法產生
- 當背景色為 `black` 時，文字顏色仍為黑色，可能無法辨識

## License

MIT License
