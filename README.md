# media-organizer 📸

Python project to automatically organize images and videos into folders categorized by **Year and Month** based on their modification date.

## 🛠 Technologies

* **Python 3**
* **OS & Shutil** (Standard libraries)

## 📁 Features

* **Date-based organization**: Automatically sorts files into folders like `2023/05 - May/`.
* **Automatic Folder Creation**: Creates the necessary directory structure if it doesn't exist.
* **Error Handling**: Skips directories and handles processing errors individually.
* **Clean Console Feedback**: Displays the total count and success messages for each file.

## ▶️ How to run

1. **Clone this repository**.
2. **Configure the path**: Open main.py and change the caminho_de_origem variable.
   ```python
   caminho_de_origem = "C:/Seu/Caminho/Aqui"
   ```
```bash
python main.py
```
