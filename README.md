🎵 音楽探索AIアプリ
好きなアーティスト名を入力すると、AIがそのアーティストの概要、影響関係、関連アーティストなどを自動で分析・表示してくれるWebアプリケーションです。

✨ 主な機能
アーティスト概要: 入力されたアーティストの簡単な紹介と代表作を表示します。

音楽ジャンルのタグ付け: アーティストの音楽性を表すジャンルをタグで表示します。

影響関係の可視化:

そのアーティストに影響を与えたアーティスト

そのアーティストと似ているアーティスト

そのアーティストが影響を与えたアーティスト

参考文献の提示: Google検索APIを利用して、分析の根拠となった可能性のあるインタビュー記事などを提示します。

AIによるレコメンド: あなたが「今」聴くべきアーティストを、AIが情熱的に推薦します。

🛠️ 使用技術
フロントエンド: Streamlit

AI連携: LangChain

言語モデル (LLM): Google Gemini 1.5 Pro

情報収集: Google Search API

言語: Python

🚀 セットアップと実行方法
1. 前提条件
Python 3.9 以上

Git

2. インストール
まず、このリポジトリをクローン（ダウンロード）します。

git clone https://github.com/あなたのユーザー名/music-discovery-app.git
cd music-discovery-app

次に、仮想環境を作成し、必要なライブラリをインストールします。

# 仮想環境の作成
python -m venv venv

# 仮想環境のアクティベート
# (Mac / Linux)
source venv/bin/activate
# (Windows)
.\venv\Scripts\activate

# 必要なライブラリのインストール
pip install -r requirements.txt

3. APIキーの設定
このアプリケーションを実行するには、3種類のAPIキーが必要です。プロジェクトのルートに.envという名前のファイルを作成し、以下の内容を記述してください。

# .env

# Google AI (Gemini) のAPIキー
GOOGLE_API_KEY="ここにGoogle AIのAPIキーを貼り付け"

# Google Search APIのキー
GOOGLE_API_KEY_SEARCH="ここにGoogle SearchのAPIキーを貼り付け"

# Programmable Search Engine のID
GOOGLE_CSE_ID="ここにCSE IDを貼り付け"

GOOGLE_API_KEY: Google AI Studio から取得できます。

GOOGLE_API_KEY_SEARCH と GOOGLE_CSE_ID: Google Cloud Console と Programmable Search Engine から取得できます。詳細は公式ドキュメントを参照してください。

4. アプリケーションの実行
以下のコマンドで、Streamlitアプリケーションを起動します。

streamlit run main.py

ブラウザが自動的に開き、アプリケーションが表示されます。

⚠️ 注意事項
本アプリケーションの利用には、Google Cloud PlatformのAPI利用料金が発生する可能性があります。個人の責任においてご利用ください。

AIによって生成される情報は、必ずしも正確性を保証するものではありません。