# バルセロナ音楽報酬質問紙（日本語版 J-BMRQ）体験ページ

授業で，学生が自分のスマホで，音楽報酬の感じやすさを測る体験ページです。20項目に1〜5で答えると，6つの得点（全体と5つの側面）が，五線の上の音符で表示されます。

- 回答は，端末の中だけで計算されます（送信も保存もしません）。
- 外部への通信や，ブラウザの保存機能は，使っていません。
- ファイルは `index.html` の1つだけです（そのままGitHub Pagesで公開できます）。

## 公開の手順（GitHub Pages。コマンドは使いません）

1. GitHubにログインし，右上の「＋」→「New repository」を選ぶ。
2. 名前を入れる（例：`jbmrq`）。**Public**を選び，「Create repository」を押す（無料のアカウントでは，Pagesの公開にPublicが必要です）。
3. 作ったページの「uploading an existing file」を押し，このフォルダの中身（`index.html`，`.nojekyll`，`README.md`，`tools`フォルダ）を，ドラッグして，「Commit changes」を押す。
4. 上のメニューの「Settings」→ 左の「Pages」を開く。「Build and deployment」の「Source」を「Deploy from a branch」にし，「Branch」を `main`，フォルダを `/ (root)` にして，「Save」を押す。
5. 数分待つと，次のアドレスで開けるようになる：
   `https://（アカウント名）.github.io/（リポジトリ名）/`

## スライドに貼るQRコード

- 上のアドレスで，QRコードを作ります。QRコード作成サイトを使うか，`tools/make_qr.py` を使います（Python：`pip install "qrcode[pil]"` のあと，`python make_qr.py アドレス`）。
- できた画像（`qr.png`）を，PART 4 の「体験」のスライド（QRコードの枠）に貼ります。

## 採点の方法

得点計算ファイル（ScoreCalculator.xlsm）のマクロと，同じ計算です。

1. 各項目 j を標準化する：z_j ＝（回答 − 項目の平均）÷ 項目の標準偏差
2. 側面ごとの重みを掛けて，足し合わせる
3. 得点 ＝ 四捨五入（合計 × 10 ＋ 50）　（平均50，標準偏差10の標準化得点）

6つの得点：音楽の探索（Musical Seeking），感情の喚起（Emotion Evocation），気分の調整（Mood Regulation），感覚運動（Sensory-Motor），社会的報酬（Social Reward），音楽報酬（全体）。

Excelファイルのサンプル4人分の結果と，このページの計算結果が，すべて一致することを確認しています。標準化した値なので，0より小さくなったり，100を超えたりすることもあります。

## 注意

- 授業での体験用です。診断や評価のためのものではありません。
- 側面の日本語名と，各側面の短い説明は，英語名と項目の内容にもとづいて付けたものです。
- 得点の基準（平均50）は，得点計算ファイルの標準化にもとづきます。
- 質問紙の項目と得点計算ファイルは，日本語版の論文の公開ページ（Open Science Framework）のものです。公開や配布の条件は，配布元で確認してください。このリポジトリには，コードのライセンスを付けていません。

## 出典

- 日本語版：Honda, S., Mas-Herrero, E., Isoda, M., Muraki, M., Lorenzo-Seva, U., Kitayama, Y., Savage, P. E., & Fujii, S. (2026). The Japanese version of the Barcelona Music Reward Questionnaire (J-BMRQ) confirms the cross-cultural generalizability of the "five-factor" model. *PLOS ONE*, 21(2), e0340700. https://doi.org/10.1371/journal.pone.0340700
- 原版：Mas-Herrero, E., Marco-Pallarés, J., Lorenzo-Seva, U., Zatorre, R. J., & Rodriguez-Fornells, A. (2013). Individual differences in music reward experiences. *Music Perception*, 31(2).
