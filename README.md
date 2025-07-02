# 🎵 音楽探索AIアプリ (Music Discovery AI)

## 概要
好きなアーティスト名を入力すると、AIがそのアーティストの概要、影響関係、関連アーティストなどを自動で分析・表示してくれるWebアプリケーションです。

## ✨ 主な機能
🎧 アーティスト概要: アーティストの簡単な紹介と代表作をリストアップします。

🏷️ ジャンルタグ: 音楽性を表すジャンルをハッシュタグ形式で表示します。

🗺️ 音楽マップ:

そのアーティストに影響を与えたアーティスト

そのアーティストと似ているアーティスト

そのアーティストが影響を与えたアーティスト

📚 参考文献: Google検索APIを利用し、分析の根拠となった可能性のあるWeb上の記事を提示します。

🔥 AIレコメンド: あなたが「今」聴くべきアーティストを、AIが情熱的に推薦します。

## 🚀 セットアップと実行方法
### 1. 前提条件
Python 3.9 以上

Git

### 2. インストール
まず、このリポジトリをローカル環境にクローン（ダウンロード）します。

Bashバッシュ

git clone https://github.com/あなたのユーザー名/music-discovery-app.git
cd music-discovery-app
次に、Pythonの仮想環境を作成し、必要なライブラリをインストールします。

Bashバッシュ

#### 仮想環境の作成
python -m venv venv

#### 仮想環境のアクティベート(Mac / Linux)
source venv/bin/activate
#### 仮想環境のアクティベート(Windows)
.\venv\Scripts\activate

#### 必要なライブラリのインストール
pip install -r requirements.txt

### 3. APIキーの設定
このアプリケーションを実行するには、3種類のAPIキーが必要です。
プロジェクトのルートディレクトリ（main.pyと同じ場所）に.envという名前のファイルを作成し、以下の内容を記述してください。

コード スニペット

'''

# .env
# Google AI (Gemini) のAPIキー
GOOGLE_API_KEY="ここにGoogle AIのAPIキーを貼り付け"

# Google Search APIのキー
GOOGLE_API_KEY_SEARCH="ここにGoogle SearchのAPIキーを貼り付け"

# Programmable Search Engine のID
GOOGLE_CSE_ID="ここにCSE IDを貼り付け"
GOOGLE_API_KEY: Google AI Studio から取得できます。

GOOGLE_API_KEY_SEARCH と GOOGLE_CSE_ID: Google Cloud Console と Programmable Search Engine から取得できます。

重要: .gitignoreファイルに.envが記載されているため、このファイルがGitHubに公開されることはありません。

'''

#### 4. アプリケーションの実行
以下のコマンドで、Streamlitアプリケーションを起動します。

Bashバッシュ

streamlit run main.py
ブラウザが自動的に開き、アプリケーションが表示されます。

## ⚠️ 注意事項
本アプリケーションの利用には、Google Cloud PlatformのAPI利用料金が発生する可能性があります。個人の責任においてご利用ください。

AIによって生成される情報は、必ずしも正確性を保証するものではありません。