# emeters-central

[atorch-console](https://github.com/NiceLabs/atorch-console) の機能のうちメーターから PDU を受信する部分だけ

## 必要なもの

- Bluetooth 機能のついた計算機
- Python >= 3.9 (タイプヒントまわりの要求 & 現行 RaspberryPi OS (bullseye) での最新バージョンが 3.9 なので)
- [Bleak](https://github.com/hbldh/bleak) Python で BLE を扱うパッケージ

## 実行方法

どちらか

### A. With poetry

以下のコマンドを実行すると(1) poetry を使ってプロジェクトに必要なパッケージを手元に持ってきて(2)実行できる

```bash
poetry install
poetry run python emeters_central/main.py
```

[**Poetry** a tool for dependency management and packaging in Python](https://github.com/python-poetry/poetry)

#### Windows 10 における注意

poetry は Microsoft Store からインストールするタイプの Python 3.x との相性問題があるようだ([参考1](https://github.com/python-poetry/poetry/issues/5331)、[参考2](https://github.com/python-poetry/poetry/issues/2629))

私がテストしたのは [Python 公式 (python.org) のダウンロードページ](https://www.python.org/downloads/) で入手できる Python だけなので、これを使うこと

もしまだ入手していない場合 [Python 3.9.13 のダウンロードページ](https://www.python.org/downloads/release/python-3913/) に行って **Windows installer (64-bit)** をダウンロードする

公式のものを一度でもダウンロードしてインストールしたことがあれば `py` コマンドが使えるはずなのでその有無で入手すべきかどうか判断してもよい

もし以前に Microsoft Store から Python をインストールしたことがあっても `py` コマンドを使えばそちらに優先して公式から入手した方が使用されるため必ずしも Microsoft Store の方の Python をアンインストールする必要はない

その上で Powershell (コマンドプロンプトではない)を起動し以下のコマンドを打つと poetry がインストールされる

```pwsh
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -3.9 -
```

Python 3.9 以外の Python.org からダウンロードした Python (注) を使うのであれば上記コマンドの`-3.9`の部分をそのバージョンに変更して実行すること

(注) Python.org からダウンロードした Python という呼び方はあまり正確ではなくて、Python 公式ドキュメント [4. Using Python on Windows](https://docs.python.org/3/using/windows.html) で *The full installer* と呼ばれているインストーラを使ってインストールした Python インタプリタ、と呼ぶのが正確で、つまるところ普通の Python

### B. Without poetry

次のコマンドを実行する

- Windows (Powershellでもできるが Execution Policy を気にしないといけない場合があるのでコマンドプロンプト推奨)

  ```plain
  py -3.9 -m venv venv
  venv\Scripts\activate
  pip install -r requirements.txt
  python emeters_central\main.py
  ```

- Mac / Linux / Windows (WSL)

  ```bash
  python -m venv venv
  . venv/bin/activate
  pip install -r requirements.txt
  python emeters_central/main.py
  ```

(メモ) requirements.txt は手動で `poetry export --dev --without-hashes -o requirements.txt` を実行して作成したので、もし poetry で管理するパッケージに変更があった場合は再度このコマンドで requirements.txt を更新する
