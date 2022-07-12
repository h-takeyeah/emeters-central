# emeters-central

[atorch-console](https://github.com/NiceLabs/atorch-console) の機能のうちメーターから PDU を受信する部分だけ

## 必要なもの

- Python >= 3.10 (タイプヒントまわりの要求からなので 3.9 でも大丈夫だと思う)
- [Bleak](https://github.com/hbldh/bleak) とそれに必要な諸々

## 実行方法

どちらか

### A. With [poetry](https://github.com/python-poetry/poetry)

```bash
poetry install
poetry run python emeters_central/main.py
```

### B. Without poetry

pyproject.toml の `tool.poetry.dependencies` テーブルに記載されているパッケージをインストールして main.py を実行する

- Windows(Powershell)

  ```pwsh
  python3 -m venv venv
  venv\Scripts\Activate.ps1
  pip install <必要なパッケージ>
  python emeters_central\main.py
  ```

- Mac/Linux/Windows(WSL)

  ```bash
  python3 -m venv venv
  . venv/bin/activate
  pip install <必要なパッケージ>
  python emeters_central/main.py
  ```

