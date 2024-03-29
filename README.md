# name-generator
かっこいい競走馬の名前を考えてくれる

文字数改良版→https://github.com/yasu-a/name-generator/tree/shorter-words

# 原理
【Wikipediaから拾ってきた実在する競走馬の名前】と【学習済みword2vec】から，実在する競争馬の名前に使われている横文字を似た横文字に置き換えることでランダムにそれらしい名前を生成する。

実在する競走馬の名前のデータは[names.html](./names.html)に格納されていて，モジュール[names.py](./names.py)により読み込まれる。

# 使い方
1. [ここ](https://www.cl.ecei.tohoku.ac.jp/~m-suzuki/jawiki_vector/)から.tar.bz2形式のw2vデータをダウンロードしてくる。
2. ダウンローした.tar.bz2ファイルを7zipなどのアプリで展開，中のファイル`entity_vector.model.bin`をスクリプトの階層に配置する。
3. [data_gen.py](./data_gen.py)を実行して横文字だけのベクトルデータ[data.pickle](./data.pickle)を生成する。
4. [main.py](./main.py)を実行するたびに[data.pickle](./data.pickle)から名前が生成される。

[data.pickle](./data.pickle)はリポジトリのファイルに含まれているので上記1.～3.はスキップ可


# 出力例
[main.py](./main.py)実行で256個名前を考えて[out.txt](./out.txt)に出力してくれる

```text
サーヴァ フクロウ
イオンマーケット センジェ
ゴロー デストピア
ムラサキ デュアル
トウショウ アウトラン
ガリア リッチーリッチ
カワセミ ビバリー
クマロボ コインランドリー
デフォレスト クリスエス
フコヒドロラーゼ アシモフ
コーフィールド ジョンワトソン
イェスンゲ ピュレ
オーロ エボジアミン
キルモント カルピスソーダ
ユリ メジロデュレン
タカラスチール バロネス
チク ルネマグリット
デイシイ ミュッケ
リーデ カワウソ
ゴイサギ マギー
リュウ ハーリーレイス
テルテンリュウ ジャジル
ツカ ベアトリーチェ
デイシイ トリートメント
ソーンクウェー アシモフ
ソーンバック スコアラー
チョンチョン ダニーホッジ
リウィアユリア ヴィム
ホワイトベアー シャーン
ファ セクシーゾーン
シイ アーレス
ハローフーヅ フラム
セオドアホール シャンペリ
セオドア デルタフォース
ビッグハウス トゥッリアーコ
ズミルックス ズミルックス
インザムード テツ
ロドス ヤンサン
スパルダ ジェイプレイス
クライシス トップネス
レオーネ グリーン
ブリタニア ハドソンホーク
スクリーン ヒーロー
アオイ ネヴァーベンド
シュロ ホセサナブリア
グラスファイバー クーポン
グンティン ハムバッキング
チョンチョン ヘッドハンターズ
スミレ グリーンビル
コルシカ クルーレス
トロピカル シエラボーゲス
ミドリ バッドサンタ
サキ ョウ
イワカガミ ギンリョウソウ
イラクサ ホセサナブリア
ファ セクシーゾーン
イッツ アニエスベー
ティーエムエヌ シーエル
ツェツィーリア シカ
ツィ ルイアラゴン
シックスティー ネイキッド
アリス ジョンライドン
ボスキャラクター ラフマジュン
マルハ イトキン
ネイションズ サークル
チョンチョン ヘッドハンターズ
タクティー アドベンチャーズ
ヒカリ エンプーサ
ツィ ルイアラゴン
キオス フォールームス
ヴォーチェ ソシエテ
マツモトトモ オキソフラン
アッカービルク スペツナズ
プレーリードッグ プレフィックス
アリシドン テツノカチドキ
エンポリオ ミュッケ
オオルリ イニャキ
ダレル ビートル
ケインジアン ブラックシープ
レギウム メンテナンス
ユリーカ サモアジョー
パイサ テューレーン
バグジー カルバージョ
シーホース クリーンナップ
トト コンウェイ
ズミルックス セイファート
オルソスコピック レシート
ナフトール ゴツ
ツィ ゴルトン
フーズ グレイシア
ウイン オイジュス
テイエム ゴッド
リファー ヘビ
ピエリア ビトウィーン
マイネル エンジェル
カハ インザシティ
ダイコン ベストセラーズ
ダイダイ デュアル
カバブ ゴーストザッパー
ジェイアイエヌ グルコサミニル
アキラ ボスエネミー
リーダーズ サークル
ワンダフル ニザームルムルク
マグダレナ リミニ
マテバシイ コロリ
テン クロフォード
フランクテート エスピー
ブレイクアウト デルタフォース
ダエーワ アカショウビン
チョンチョン サプレザ
マチカネ ランスハワード
クルミ スズキ
フコヒドロラーゼ アミュクラース
リキエイカン ヘンリエッテ
アルキダモス シャンペリ
カラ クズリ
ハチ アブリコ
ショコラ トガイ
イム アサギリ
タカラスチール パープル
ラーイ ウェーブ
バグジー シャーン
カボチヤ ビボ
ランゲラント ヒョウ
モウセンゴケ スズメノエンドウ
ヒカリ ドゥッカ
ユリーカ サプレザ
エヌジー タック
ミー ピリカ
サキ ブランドン
スミレ ヒガンフグ
グレゴリー セイバー
アレ ピリカ
ソーブレスド アテーナー
シュロ エルシグノ
シュウ サモアジョー
エドウィナ アナログ
メモリーズ バルバダス
ソラ ボスエネミー
オネスティ コリィ
ホワイトナルビー バロネス
モノキニ エルフィックス
ネイションズ サークル
エグジット ドラッグセガミ
マシュー ゾルタウ
トウコウ ディス
プシコース マズ
グンゼ スーパーバッド
ライダーズ テスラ
トウコウ ストームバード
ラヌッチオ ジェルミナル
スマイルビット ビーフ
ミツグ ダークマッチ
フードサービス フェナリナーサ
アペプ シンジュ
ムサシ レッドタイガー
エフエスビー ナイ
グク ラブクラフト
ドウシシャ ブランズ
ジョンワトソン ダチョウ
マキタ クァンミョン
シックスティー ネイキッド
サイコビリー ダンスナンバー
ビューティフル アハシュエロス
チャル チーター
リョウ オルクス
カービュー シャーン
デルケンハイム ダッジ
ディーサイド ロン
リウィアユリア アナログ
エウレカベイビー アソビモ
ソード ブルマー
ソリッド ヘルツイェズ
ウェインライト エース
キジ ヘンダーソンビル
ゴクミ クリスエス
ドバヴィエール レディパステル
リホ インドミタブル
ファイヤー スカート
ソーンバック リードオフマン
オーテモン サプレザ
チョンチョン マイトガイン
タケル オルクス
プリティ アハシュエロス
オセ トラ
コードフリーク ション
マサ マサ
トラブルイン アニエスベー
イーグル ヴィリャンディ
カルガモ ヘプバーン
メジロライアン ドラコ
ミッチェル ニンジャ
ゲームウオッチ ドラディション
キシルロース セイ
トドマツ モービー
シャヒン リッジ
デシベル ニシャンジュ
サキ メリディアン
カヌリ ウルフガイ
レギュレイターズ サターン
デイヴィッド ミラージュ
レメディオス サスカチュワン
スギ オナニーマシーン
トウショウ マーズ
タケル オルガコルブト
ホワイト コップ
ユリ ムムタズマハル
タイトル アルピトレリ
ミカ アフリカン
マチカネ ヘンリエッテ
ゲームウオッチ ディーパー
アイティフォー モンラッシェ
ゼットワン ジアゴニスト
ダーティー グレッグハウ
モリタ フェナリナーサ
クモ サワラ
ナメクジ ハクジラ
ナミ トウコウエルザ
スモーキー ジーノスミス
ベコ リーチザクラウン
リーダーズ サークル
フェラン ペガァマガボウ
サスケ ケイダブ
マチカネ セサールソト
クモ サワラ
チク アンリマティス
スクリーン ヒーロー
シカゴ カフェ
プレスボーン エルピー
イグサ エルシグノ
ユリ エウダミダス
シイ カリーナ
オーテモン ワイアー
ヤエ リーハイバレー
マイネル マリーアンヌ
コウ リングス
バスター パンツ
ーセ ラウエ
プランテン タカ
カワセミ ブクログ
クロマツ スケボーキング
ゲームウオッチ レオンホワイト
メーダー チャンジン
クリストファー ミュッケ
イザベラ デジタル
イザベラ ハヤトコバヤシ
テーベ メインテナンス
クモ タイラギ
イオンマーケット アジャリス
イーシーエヌ ゾルタウ
リーフストーム ニックデニス
リュウ ブランドソール
オコン タック
ホッカイ ゴスホークケン
デスリベンジ ミュッケ
ヤエ ハイスピード
```
