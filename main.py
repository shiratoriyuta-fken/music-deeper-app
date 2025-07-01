# main.py
import streamlit as st
import os
# .envファイルを読み込むためにdotenvをインポート
from dotenv import load_dotenv
# Google Geminiを利用するためのライブラリをインポートします
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
# Google検索ツールを新しい推奨ライブラリからインポートします
from langchain_google_community import GoogleSearchAPIWrapper

# アプリケーションの開始時に.envファイルを読み込む
load_dotenv()

# --- App Information ---
# Streamlitのページ設定
st.set_page_config(
    page_title="音楽探索アプリ (Gemini版)",
    page_icon="🎵",
    layout="wide"
)

# --- .envファイルから各APIキーを読み込む ---
# ★ それぞれのキーを専用の変数に格納します
GEMINI_API_KEY = os.getenv("GOOGLE_API_KEY")
SEARCH_API_KEY = os.getenv("GOOGLE_API_KEY_SEARCH")
SEARCH_CSE_ID = os.getenv("GOOGLE_CSE_ID")


# --- Functions ---

def check_api_keys_loaded():
    """
    .envファイルから全てのAPIキーが読み込めているか確認します。
    """
    if GEMINI_API_KEY and SEARCH_API_KEY and SEARCH_CSE_ID:
        return True
    return False


def create_llm_chain():
    """
    Geminiを利用してLangChainのLLMChainオブジェクトを作成し、返します。
    """
    # ★ プロンプトテンプレートを更新し、概要・代表作・ジャンルのセクションを追加
    prompt_template_text = """
    あなたは世界中の音楽に精通した、情熱的な音楽評論家です。
    以下の参考情報とあなた自身の知識を基に、指定されたアーティストについて分析してください。
    特に「影響を与えたアーティスト」セクションでは、参考情報から関連する記述を見つけ、出典を明記してください。

    回答は必ず以下のMarkdown形式で、日本語で記述してください。

    ---
    **入力アーティスト:** {artist}
    ---

    ### 概要
    （ここにアーティストの簡潔な概要を記述してください）

    ### 代表作
    * （代表作を3曲挙げてください）
    * * ### ジャンル
    `#ジャンル1` `#ジャンル2` `#ジャンル3`

    ---

    ### 🎸 {artist} に影響を与えたアーティスト

    * **アーティスト名1:** (解説) [出典: 参考情報のタイトル]
    * **アーティスト名2:** (解説) [出典: 参考情報のタイトル]
    * **アーティスト名3:** (解説) [出典: 参考情報のタイトル]

    ### 🎧 {artist} と似ているアーティスト

    * **アーティスト名1:** (解説)
    * **アーティスト名2:** (解説)
    * **アーティスト名3:** (解説)

    ### 🌱 {artist} が影響を与えたアーティスト

    * **アーティスト名1:** (解説)
    * **アーティスト名2:** (解説)
    * **アーティスト名3:** (解説)
    
    ### 🔥 あなたが今聴くべきアーティスト

    * **アーティスト名:** (なぜ「今」聴くべきなのか、その理由を{artist}と関連付けながら情熱的に解説してください)
    """

    prompt = PromptTemplate(
        template=prompt_template_text,
        input_variables=["artist", "references"]
    )

    # ★ LLMモデルの初期化時に、Gemini専用のAPIキーを明示的に渡します
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-pro",
                             google_api_key=GEMINI_API_KEY,
                             temperature=0.7,
                             convert_system_message_to_human=True)

    chain = LLMChain(llm=llm, prompt=prompt)
    return chain

# --- Main Application UI ---

st.title("🎵 音楽探索アプリ (Gemini & Google検索)")
st.write("好きなアーティスト名を入力すると、AIが概要や関連アーティストをインタビュー記事などを基に分析してくれます。")

# .envからキーが読み込めているか確認
keys_ready = check_api_keys_loaded()

# サイドバーの表示
st.sidebar.header("設定")
if keys_ready:
    st.sidebar.success("APIキーは正常に読み込まれました。")
else:
    st.sidebar.error("`.env`ファイルに3種類のAPIキーを正しく設定してください。")


# メインコンテンツ
artist_name = st.text_input("好きなアーティストやバンド名を入力してください", placeholder="例: The Beatles, 宇多田ヒカル")

if st.button("分析を開始する"):
    if not keys_ready:
        st.error(".envファイルに全てのAPIキーを設定してください。")
    elif not artist_name:
        st.warning("アーティスト名を入力してください。")
    else:
        try:
            with st.spinner("関連情報を検索し、Geminiが分析中です..."):
                # ★ STEP 1: Google検索の実行時に、検索専用のキーとIDを明示的に渡します
                search = GoogleSearchAPIWrapper(
                    google_api_key=SEARCH_API_KEY,
                    google_cse_id=SEARCH_CSE_ID
                )
                query = f'"{artist_name}" 影響 ルーツ インタビュー'
                search_results = search.results(query, 5)

                references_text = ""
                if search_results:
                    for i, result in enumerate(search_results):
                        # 'snippet'がない場合もあるため、安全にアクセスします
                        snippet = result.get('snippet', 'スニペットなし')
                        references_text += f"[{i+1}] Title: {result.get('title', 'タイトルなし')}\n"
                        references_text += f"   Link: {result.get('link', 'リンクなし')}\n"
                        references_text += f"   Snippet: {snippet}\n\n"
                else:
                    references_text = "関連する参考情報は見つかりませんでした。"

                # STEP 2: LLMChainを生成し、検索結果を渡して実行
                chain = create_llm_chain()
                response = chain.run({
                    "artist": artist_name,
                    "references": references_text
                })

            # 結果の表示
            st.subheader(f"🔍 「{artist_name}」の音楽マップ")
            st.markdown(response)
            
            with st.expander("参考文献リストを見る"):
                st.write(references_text)

        except Exception as e:
            st.error(f"エラーが発生しました: {e}")
            st.info("APIキーが正しいか、各APIが有効になっているか、請求先アカウントが設定されているかをご確認ください。")

# --- Footer ---
st.sidebar.markdown("---")
st.sidebar.info(
    "このアプリはStreamlit、LangChain、Google Gemini、Google Search APIを利用して作成されています。"
)
