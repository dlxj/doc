
Super Nario GC
http://d.hatena.ne.jp/authorNari/20080422/1208880928

を Haskell/HSDL で作る



* 操作
	カーソルキー, ijkl
		上下左右

	スペースキー, z
		ジャンプ（Aボタン）

	シフトキー
		ダッシュ（Bボタン）

	エスケープキー
		終了



* ファイル構成
	data
		データ
	data/img
		画像データ



* ビルド
- 必要なもの
	Haskell コンパイラ

	SDL
	http://www.libsdl.org/

	Graphics.UI.SDL
	http://hackage.haskell.org/cgi-bin/hackage-scripts/package/SDL

	Graphics.UI.SDL.Mixer
	http://hackage.haskell.org/cgi-bin/hackage-scripts/package/SDL-mixer

　- ビルド
	make

　- 実行
	できた実行ファイルを起動する、または
	make run



* 参考
	Super Nario GC
	http://d.hatena.ne.jp/authorNari/20080422/1208880928

	1-1 マップ
	http://www.geocities.co.jp/SiliconValley-Sunnyvale/6160/newtech/m11.htm

	フォント
	http://qtchicks.hp.infoseek.co.jp/fonts-nintendo.html

	unsafeInterleaveIO
	http://d.hatena.ne.jp/tanakh/20040803#p1

	存在型
	http://d.hatena.ne.jp/keigoi/20080805/p2

	Haskellの循環import問題 - ABAの日誌
	http://d.hatena.ne.jp/ABA/20060627#p1

	サウンド素材
	http://utm-game-web.hp.infoseek.co.jp/free-sound.htm
