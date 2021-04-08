
# ffmpeg -i "F:\Downloads\[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no Koukousei The Animation [1280x720 x264 AAC MKV Sub(Chs,Jap)]\[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no ...he Animation - 01 [1280x720 x264 AAC Sub(Chs,Jap)].mkv" -map 0:s:0 out.srt
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c13/p06_executing_external_command_and_get_its_output.html

import os,subprocess
import re
import glob
import chardet
import MeCab
tagger = MeCab.Tagger()


"""
D:\GitHub\doc\lang\programming\postgresql summary.md
    docker exec -it centos7PG10 /bin/bash
        54322 port
    Install PG_Jieba [u](https://github.com/jaiminpan/pg_jieba)

pip install mecab-python3
pip install unidic-lite

pip install xmltodict
GFW
https://www.ishells.cn/archives/linux-ssr-server-client-install
"""


"""

SELECT pgroonga_tokenize('します','tokenizer', 'TokenMecab("use_base_form", true, "include_reading", true)')
 --> {"{\"value\":\"する\",\"position\":0,\"force_prefix_search\":false,\"metadata\":{\"reading\":\"シ\"}}","{\"value\":\"ます\",\"position\":1,\"force_prefix_search\":true,\"metadata\":{\"reading\":\"マス\"}}"}


CREATE OR REPLACE FUNCTION ja_reading (TEXT) RETURNS TEXT AS
$func$
DECLARE
  js      JSON;
  total   TEXT[] := '{}';
  reading TEXT;
BEGIN
  FOREACH js IN ARRAY pgroonga_tokenize($1,
    'tokenizer', 'TokenMecab("include_reading", true)')
  LOOP
    reading = (js -> 'metadata' ->> 'reading');

    IF reading IS NULL THEN
      total = total || (js ->> 'value');
    ELSE
      total = total || reading;
    END IF;
  END LOOP;

  RETURN array_to_string(total, '');
END;
$func$ LANGUAGE plpgsql IMMUTABLE;


SELECT ja_reading ('有');
-- 

/*
{"{\"value\":\"海\",\"position\":0,\"force_prefix_search\":false,\"metadata\":{\"reading\":\"ウミ\"}}"}
{"{\"value\":\"1\",\"position\":0,\"force_prefix_search\":false}"}
*/


{
  "force_prefix_search": false,
  "metadata": {
    "reading": "シ"
  },
  "position": 0,
  "value": "する"
}



SELECT string_to_array('xx~^~yy~^~zz', '~^~')
  --> {xx,yy,zz}


"""

"""

https://groonga.org/docs/reference/tokenizers/token_mecab.html

https://github.com/pgroonga/pgroonga/issues/171

My thought has become

CREATE TABLE dict.tatoeba (
  "id"            INT NOT NULL,
  "jpn"           TEXT,
  "eng"           TEXT NOT NULL,
  PRIMARY KEY ("id")
);

CREATE INDEX idx_tatoeba_jpn ON dict.tatoeba
  USING pgroonga ("jpn")
  WITH (
    tokenizer='TokenMecab("use_base_form", true, "include_form", true, "include_reading", true)',
    normalizer='NormalizerNFKC100("unify_kana", true)'
  );
CREATE INDEX idx_tatoeba_eng ON dict.tatoeba
  USING pgroonga ("eng")
  WITH (plugins='token_filters/stem', token_filters='TokenFilterStem');
Then

SELECT * FROM dict.tatoeba
WHERE jpn &@ 'うみ'
ORDER BY pgroonga_score(tableoid, ctid) DESC
LIMIT 10;
But it isn't comparable to 海.
"""

"""

&@ 单关键词的fulltext search

CREATE TABLE dict.tatoeba (
  "id"            INT NOT NULL,
  "jpn"           TEXT,
  "eng"           TEXT NOT NULL,
  PRIMARY KEY ("id")
);



CREATE INDEX idx_tatoeba_jpn_base_form ON dict.tatoeba
  USING pgroonga ((jpn || ''))
  WITH (
    tokenizer='TokenMecab("use_base_form", true)',
    normalizer='NormalizerNFKC100("unify_kana", true)'
  );

CREATE INDEX idx_tatoeba_jpn_reading ON dict.tatoeba
  USING pgroonga ((jpn || '' || ''))
  WITH (
    tokenizer='TokenMecab("use_reading", true)',
    normalizer='NormalizerNFKC100("unify_kana", true)'
  );

SELECT * FROM dict.tatoeba
WHERE (jpn || '')       &@~ ja_expand('海') -- search by base_form
   OR (jpn || '' || '') &@~ ja_expand('海') -- search by reading
LIMIT 10;
"""

"""
CREATE TABLE dict.tatoeba (
  "id"            INT NOT NULL,
  "jpn"           TEXT,
  "eng"           TEXT NOT NULL,
  PRIMARY KEY ("id")
);

CREATE OR REPLACE FUNCTION ja_reading (TEXT) RETURNS TEXT AS
$func$
DECLARE
  js      JSON;
  total   TEXT[] := '{}';
  reading TEXT;
BEGIN
  FOREACH js IN ARRAY pgroonga_tokenize($1,
    'tokenizer', 'TokenMecab("include_reading", true)')
  LOOP
    reading = (js -> 'metadata' ->> 'reading');

    IF reading IS NULL THEN
      total = total || (js ->> 'value');
    ELSE
      total = total || reading;
    END IF;
  END LOOP;

  RETURN array_to_string(total, '');
END;
$func$ LANGUAGE plpgsql IMMUTABLE;

CREATE OR REPLACE FUNCTION ja_expand (TEXT) RETURNS TEXT AS
$func$
BEGIN
  IF $1 ~ '[\u4e00-\u9fa5]' THEN
    RETURN  $1||' OR '||ja_reading($1);
  END IF;

  RETURN $1;
END;
$func$ LANGUAGE plpgsql IMMUTABLE;

SELECT * FROM dict.tatoeba
WHERE jpn &@~ ja_expand('海')
LIMIT 10;
"""


"""

CREATE OR REPLACE FUNCTION JPQ (TEXT) RETURNS TEXT AS
$func$
DECLARE
  js      JSON;
  total   TEXT[] := '{}';
  reading TEXT;
	s TEXT;
BEGIN
  FOREACH s IN ARRAY string_to_array($1, '|')
  LOOP
    
		FOREACH js IN ARRAY pgroonga_tokenize(s, 'tokenizer', 'TokenMecab("use_base_form", true, "include_reading", true)')
		LOOP
			reading = (js -> 'metadata' ->> 'reading');
			IF reading IS NULL THEN
					RETURN 0;
      END IF;
		
		END LOOP;
  END LOOP;
	
	RETURN 1;
	
END;
$func$ LANGUAGE plpgsql IMMUTABLE;

"""


import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import sqlite3 as sqlite # Python 自带的

from pymysql import escape_string
import glob

import json
import decimal
import datetime

import xmltodict



class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        elif isinstance(o, datetime.datetime):
            return str(o)
        super(DecimalEncoder, self).default(o)

def save_json(filename, dics):
    with open(filename, 'w', encoding='utf-8') as fp:
        json.dump(dics, fp, indent=4, cls=DecimalEncoder, ensure_ascii=False)
        fp.close()

def load_json(filename):
    with open(filename, encoding='utf-8') as fp:
        js = json.load(fp)
        fp.close()
        return js

def readstring(fname):
    with open(fname, "r", encoding="utf-8") as fp:
        data = fp.read()
        fp.close()
    return data

def writestring(fname, strs):
    with open(fname, "w", encoding="utf-8") as fp:
        fp.write(strs)
        fp.close()

# out_bytes = subprocess.check_output([r"ffmpeg", "-i", "F:\Downloads\[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no Koukousei The Animation [1280x720 x264 AAC MKV Sub(Chs,Jap)]\[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no ...he Animation - 01 [1280x720 x264 AAC Sub(Chs,Jap)].mkv", "-map", "0:s:0", "out.srt"])
# out_text = out_bytes.decode('utf-8')

# \u4e00-\u9fa5

def unchinese_remove(s):
    return re.sub(r"[^\u4e00-\u9fa5]", "", s, flags=re.UNICODE)

def chinese_remove(s):
    return re.sub(r"[\u4e00-\u9fa5]", "", s, flags=re.UNICODE)

def unjp_remove(s):
    return re.sub(r"[^\u0800-\u4e00]", "", s, flags=re.UNICODE)

def unhana_remove(s):
    return re.sub(r"[^\u3040-\u309F^\u30A0-\u30FF]", "", s, flags=re.UNICODE)

def hasHanaQ(s):
    return len( unhana_remove(s) ) > 0

def fanti():
  return                                                                                                                                                                                  "萬與醜專業叢東絲丟兩嚴喪個爿豐臨為麗舉麼義烏樂喬習鄉書買亂爭於虧雲亙亞產畝親褻嚲億僅從侖倉儀們價眾優夥會傴傘偉傳傷倀倫傖偽佇體餘傭僉俠侶僥偵側僑儈儕儂俁儔儼倆儷儉債傾傯僂僨償儻儐儲儺兒兌兗黨蘭關興茲養獸囅內岡冊寫軍農塚馮衝決況凍淨淒涼淩減湊凜幾鳳鳧憑凱擊氹鑿芻劃劉則剛創刪別剗剄劊劌剴劑剮劍剝劇勸辦務勱動勵勁勞勢勳猛勩勻匭匱區醫華協單賣盧鹵臥衛卻巹廠廳曆厲壓厭厙廁廂厴廈廚廄廝縣參靉靆雙發變敘疊葉號歎嘰籲後嚇呂嗎唚噸聽啟吳嘸囈嘔嚦唄員咼嗆嗚詠哢嚨嚀噝吒噅鹹呱響啞噠嘵嗶噦嘩噲嚌噥喲嘜嗊嘮啢嗩唕喚呼嘖嗇囀齧囉嘽嘯噴嘍嚳囁嗬噯噓嚶囑嚕劈囂謔團園囪圍圇國圖圓聖壙場阪壞塊堅壇壢壩塢墳墜壟壟壚壘墾坰堊墊埡墶壋塏堖塒塤堝墊垵塹墮壪牆壯聲殼壺壼處備複夠頭誇夾奪奩奐奮獎奧妝婦媽嫵嫗媯姍薑婁婭嬈嬌孌娛媧嫻嫿嬰嬋嬸媼嬡嬪嬙嬤孫學孿寧寶實寵審憲宮寬賓寢對尋導壽將爾塵堯尷屍盡層屭屜屆屬屢屨嶼歲豈嶇崗峴嶴嵐島嶺嶽崠巋嶨嶧峽嶢嶠崢巒嶗崍嶮嶄嶸嶔崳嶁脊巔鞏巰幣帥師幃帳簾幟帶幀幫幬幘幗冪襆幹並廣莊慶廬廡庫應廟龐廢廎廩開異棄張彌弳彎彈強歸當錄彠彥徹徑徠禦憶懺憂愾懷態慫憮慪悵愴憐總懟懌戀懇惡慟懨愷惻惱惲悅愨懸慳憫驚懼慘懲憊愜慚憚慣湣慍憤憒願懾憖怵懣懶懍戇戔戲戧戰戩戶紮撲扡執擴捫掃揚擾撫拋摶摳掄搶護報擔擬攏揀擁攔擰撥擇掛摯攣掗撾撻挾撓擋撟掙擠揮撏撈損撿換搗據撚擄摑擲撣摻摜摣攬撳攙擱摟攪攜攝攄擺搖擯攤攖撐攆擷擼攛擻攢敵斂數齋斕鬥斬斷無舊時曠暘曇晝曨顯晉曬曉曄暈暉暫曖劄術樸機殺雜權條來楊榪傑極構樅樞棗櫪梘棖槍楓梟櫃檸檉梔柵標棧櫛櫳棟櫨櫟欄樹棲樣欒棬椏橈楨檔榿橋樺檜槳樁夢檮棶檢欞槨櫝槧欏橢樓欖櫬櫚櫸檟檻檳櫧橫檣櫻櫫櫥櫓櫞簷檁歡歟歐殲歿殤殘殞殮殫殯毆毀轂畢斃氈毿氌氣氫氬氳彙漢汙湯洶遝溝沒灃漚瀝淪滄渢溈滬濔濘淚澩瀧瀘濼瀉潑澤涇潔灑窪浹淺漿澆湞溮濁測澮濟瀏滻渾滸濃潯濜塗湧濤澇淶漣潿渦溳渙滌潤澗漲澀澱淵淥漬瀆漸澠漁瀋滲溫遊灣濕潰濺漵漊潷滾滯灩灄滿瀅濾濫灤濱灘澦濫瀠瀟瀲濰潛瀦瀾瀨瀕灝滅燈靈災燦煬爐燉煒熗點煉熾爍爛烴燭煙煩燒燁燴燙燼熱煥燜燾煆糊溜愛爺牘犛牽犧犢強狀獷獁猶狽麅獮獰獨狹獅獪猙獄猻獫獵獼玀豬貓蝟獻獺璣璵瑒瑪瑋環現瑲璽瑉玨琺瓏璫琿璡璉瑣瓊瑤璦璿瓔瓚甕甌電畫暢佘疇癤療瘧癘瘍鬁瘡瘋皰屙癰痙癢瘂癆瘓癇癡癉瘮瘞瘺癟癱癮癭癩癬癲臒皚皺皸盞鹽監蓋盜盤瞘眥矓著睜睞瞼瞞矚矯磯礬礦碭碼磚硨硯碸礪礱礫礎硜矽碩硤磽磑礄確鹼礙磧磣堿镟滾禮禕禰禎禱禍稟祿禪離禿稈種積稱穢穠穭稅穌穩穡窮竊竅窯竄窩窺竇窶豎競篤筍筆筧箋籠籩築篳篩簹箏籌簽簡籙簀篋籜籮簞簫簣簍籃籬籪籟糴類秈糶糲粵糞糧糝餱緊縶糸糾紆紅紂纖紇約級紈纊紀紉緯紜紘純紕紗綱納紝縱綸紛紙紋紡紵紖紐紓線紺絏紱練組紳細織終縐絆紼絀紹繹經紿綁絨結絝繞絰絎繪給絢絳絡絕絞統綆綃絹繡綌綏絛繼綈績緒綾緓續綺緋綽緔緄繩維綿綬繃綢綯綹綣綜綻綰綠綴緇緙緗緘緬纜緹緲緝縕繢緦綞緞緶線緱縋緩締縷編緡緣縉縛縟縝縫縗縞纏縭縊縑繽縹縵縲纓縮繆繅纈繚繕繒韁繾繰繯繳纘罌網羅罰罷羆羈羥羨翹翽翬耮耬聳恥聶聾職聹聯聵聰肅腸膚膁腎腫脹脅膽勝朧腖臚脛膠脈膾髒臍腦膿臠腳脫腡臉臘醃膕齶膩靦膃騰臏臢輿艤艦艙艫艱豔艸藝節羋薌蕪蘆蓯葦藶莧萇蒼苧蘇檾蘋莖蘢蔦塋煢繭荊薦薘莢蕘蓽蕎薈薺蕩榮葷滎犖熒蕁藎蓀蔭蕒葒葤藥蒞蓧萊蓮蒔萵薟獲蕕瑩鶯蓴蘀蘿螢營縈蕭薩蔥蕆蕢蔣蔞藍薊蘺蕷鎣驀薔蘞藺藹蘄蘊藪槁蘚虜慮虛蟲虯蟣雖蝦蠆蝕蟻螞蠶蠔蜆蠱蠣蟶蠻蟄蛺蟯螄蠐蛻蝸蠟蠅蟈蟬蠍螻蠑螿蟎蠨釁銜補襯袞襖嫋褘襪襲襏裝襠褌褳襝褲襇褸襤繈襴見觀覎規覓視覘覽覺覬覡覿覥覦覯覲覷觴觸觶讋譽謄訁計訂訃認譏訐訌討讓訕訖訓議訊記訒講諱謳詎訝訥許訛論訩訟諷設訪訣證詁訶評詛識詗詐訴診詆謅詞詘詔詖譯詒誆誄試詿詩詰詼誠誅詵話誕詬詮詭詢詣諍該詳詫諢詡譸誡誣語誚誤誥誘誨誑說誦誒請諸諏諾讀諑誹課諉諛誰諗調諂諒諄誶談誼謀諶諜謊諫諧謔謁謂諤諭諼讒諮諳諺諦謎諞諝謨讜謖謝謠謗諡謙謐謹謾謫譾謬譚譖譙讕譜譎讞譴譫讖穀豶貝貞負貟貢財責賢敗賬貨質販貪貧貶購貯貫貳賤賁貰貼貴貺貸貿費賀貽賊贄賈賄貲賃賂贓資賅贐賕賑賚賒賦賭齎贖賞賜贔賙賡賠賧賴賵贅賻賺賽賾贗讚贇贈贍贏贛赬趙趕趨趲躉躍蹌蹠躒踐躂蹺蹕躚躋踴躊蹤躓躑躡蹣躕躥躪躦軀車軋軌軒軑軔轉軛輪軟轟軲軻轤軸軹軼軤軫轢軺輕軾載輊轎輈輇輅較輒輔輛輦輩輝輥輞輬輟輜輳輻輯轀輸轡轅轄輾轆轍轔辭辯辮邊遼達遷過邁運還這進遠違連遲邇逕跡適選遜遞邐邏遺遙鄧鄺鄔郵鄒鄴鄰鬱郤郟鄶鄭鄆酈鄖鄲醞醱醬釅釃釀釋裏钜鑒鑾鏨釓釔針釘釗釙釕釷釺釧釤鈒釩釣鍆釹鍚釵鈃鈣鈈鈦鈍鈔鍾鈉鋇鋼鈑鈐鑰欽鈞鎢鉤鈧鈁鈥鈄鈕鈀鈺錢鉦鉗鈷缽鈳鉕鈽鈸鉞鑽鉬鉭鉀鈿鈾鐵鉑鈴鑠鉛鉚鈰鉉鉈鉍鈹鐸鉶銬銠鉺銪鋏鋣鐃銍鐺銅鋁銱銦鎧鍘銖銑鋌銩銛鏵銓鉿銚鉻銘錚銫鉸銥鏟銃鐋銨銀銣鑄鐒鋪鋙錸鋱鏈鏗銷鎖鋰鋥鋤鍋鋯鋨鏽銼鋝鋒鋅鋶鐦鐧銳銻鋃鋟鋦錒錆鍺錯錨錡錁錕錩錫錮鑼錘錐錦鍁錈錇錟錠鍵鋸錳錙鍥鍈鍇鏘鍶鍔鍤鍬鍾鍛鎪鍠鍰鎄鍍鎂鏤鎡鏌鎮鎛鎘鑷鐫鎳鎿鎦鎬鎊鎰鎔鏢鏜鏍鏰鏞鏡鏑鏃鏇鏐鐔钁鐐鏷鑥鐓鑭鐠鑹鏹鐙鑊鐳鐶鐲鐮鐿鑔鑣鑞鑲長門閂閃閆閈閉問闖閏闈閑閎間閔閌悶閘鬧閨聞闥閩閭闓閥閣閡閫鬮閱閬闍閾閹閶鬩閿閽閻閼闡闌闃闠闊闋闔闐闒闕闞闤隊陽陰陣階際陸隴陳陘陝隉隕險隨隱隸雋難雛讎靂霧霽黴靄靚靜靨韃鞽韉韝韋韌韍韓韙韞韜韻頁頂頃頇項順須頊頑顧頓頎頒頌頏預顱領頗頸頡頰頲頜潁熲頦頤頻頮頹頷頴穎顆題顒顎顓顏額顳顢顛顙顥纇顫顬顰顴風颺颭颮颯颶颸颼颻飀飄飆飆飛饗饜飣饑飥餳飩餼飪飫飭飯飲餞飾飽飼飿飴餌饒餉餄餎餃餏餅餑餖餓餘餒餕餜餛餡館餷饋餶餿饞饁饃餺餾饈饉饅饊饌饢馬馭馱馴馳驅馹駁驢駔駛駟駙駒騶駐駝駑駕驛駘驍罵駰驕驊駱駭駢驫驪騁驗騂駸駿騏騎騍騅騌驌驂騙騭騤騷騖驁騮騫騸驃騾驄驏驟驥驦驤髏髖髕鬢魘魎魚魛魢魷魨魯魴魺鮁鮃鯰鱸鮋鮓鮒鮊鮑鱟鮍鮐鮭鮚鮳鮪鮞鮦鰂鮜鱠鱭鮫鮮鮺鯗鱘鯁鱺鰱鰹鯉鰣鰷鯀鯊鯇鮶鯽鯒鯖鯪鯕鯫鯡鯤鯧鯝鯢鯰鯛鯨鯵鯴鯔鱝鰈鰏鱨鯷鰮鰃鰓鱷鰍鰒鰉鰁鱂鯿鰠鼇鰭鰨鰥鰩鰟鰜鰳鰾鱈鱉鰻鰵鱅鰼鱖鱔鱗鱒鱯鱤鱧鱣鳥鳩雞鳶鳴鳲鷗鴉鶬鴇鴆鴣鶇鸕鴨鴞鴦鴒鴟鴝鴛鴬鴕鷥鷙鴯鴰鵂鴴鵃鴿鸞鴻鵐鵓鸝鵑鵠鵝鵒鷳鵜鵡鵲鶓鵪鶤鵯鵬鵮鶉鶊鵷鷫鶘鶡鶚鶻鶿鶥鶩鷊鷂鶲鶹鶺鷁鶼鶴鷖鸚鷓鷚鷯鷦鷲鷸鷺鸇鷹鸌鸏鸛鸘鹺麥麩黃黌黶黷黲黽黿鼂鼉鞀鼴齇齊齏齒齔齕齗齟齡齙齠齜齦齬齪齲齷龍龔龕龜誌製谘隻裡係範鬆冇嚐嘗鬨麵準鐘彆閒乾儘臟拚"

def parseSrtTime(time):
  
  time = "01:02:03,004 --> 00:00:00,070"
  begin = time.split('-->')[0].strip()
  end = time.split('-->')[1].strip()

  if match := re.compile(r'\d\d:(\d\d):\d\d,\d\d\d').search(begin):  
	  print( match.group(1), int(match.group(1)) )


def allfname(root, ext):
    names = os.listdir(root)
    # if os.path.exists( root ):
    #   p =  os.path.join( root, '*.mkv' )
    #   names = os.listdir(root) # glob.glob(p)
    #   a = 1    
    # path = r"F:\Downloads\[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no Koukousei The Animation [1280x720 x264 AAC MKV Sub(Chs,Jap)]"+ f'/*.mkv'
    # names = glob.glob(path)
    return names
  











# 有假名的是日语，没有pgroonga_tokenize 分出来没有读音的不是日语
# 没有读音的不是
# SELECT pgroonga_tokenize('并','tokenizer', 'TokenMecab("use_base_form", true,"include_reading", true)') # use_base_form 可能会把变形转成原形？
# SELECT pgroonga_tokenize('します','tokenizer', 'TokenMecab("use_base_form", true,"include_reading", true)')
  # --> {"{\"value\":\"する\",\"position\":0,\"force_prefix_search\":false,\"metadata\":{\"reading\":\"シ\"}}","{\"value\":\"ます\",\"position\":1,\"force_prefix_search\":true,\"metadata\":{\"reading\":\"マス\"}}"}

def jpQ(s):
    return len( unhana_remove(s) ) > 0


def createAnimeDB(host, port):
    with psycopg2.connect(database='postgres', user='postgres', password='postgres',host=host, port=port) as conn:
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        with conn.cursor() as cur:
            cur.execute("DROP DATABASE IF EXISTS anime;")
            cur.execute("CREATE DATABASE anime \
                WITH OWNER = postgres \
                ENCODING = 'UTF8' \
                TABLESPACE = pg_default \
                CONNECTION LIMIT = -1 \
                TEMPLATE template0;")

    with psycopg2.connect(database='anime', user='postgres', password='postgres',host=host, port=port) as conn:
        with conn.cursor() as cur:
        
            cur.execute("DROP TABLE IF EXISTS anime;")
            cur.execute("create table anime( \
                id serial primary key, \
                name text, \
                jp text, \
                zh text DEFAULT '', \
                en text DEFAULT '', \
                type text, \
                time text, \
                jp_mecab text, \
                v_jp  tsvector, \
                v_zh  tsvector, \
                v_en  tsvector \
            );")

            cur.execute("create extension pgroonga;")
            cur.execute("CREATE INDEX pgroonga_jp_index ON anime USING pgroonga (jp);")
            cur.execute("CREATE INDEX pgroonga_jpmecab_index ON anime USING pgroonga (jp_mecab);")

            cur.execute("create extension pg_jieba;")

            cur.execute("CREATE INDEX animename_index ON anime (name);")
            
            # cur.execute("create extension rum;") 
            # cur.execute("CREATE INDEX fts_rum_anime ON anime USING rum (v_jp rum_tsvector_ops);")

            # 加一个函数，只要有一个字没有读音就不是jp 
            cur.execute(
              """
CREATE OR REPLACE FUNCTION JPQ (TEXT) RETURNS INT AS
$func$
DECLARE
  js      JSON;
  total   TEXT[] := '{}';
  reading TEXT;
	s TEXT;
BEGIN
  FOREACH s IN ARRAY string_to_array($1, '|')
  LOOP
    
		FOREACH js IN ARRAY pgroonga_tokenize(s, 'tokenizer', 'TokenMecab("use_base_form", true, "include_reading", true)')
		LOOP
			reading = (js -> 'metadata' ->> 'reading');
			IF reading IS NULL THEN
					RETURN 0;
      END IF;
		
		END LOOP;
  END LOOP;
	
	RETURN 1;
	
END;
$func$ LANGUAGE plpgsql IMMUTABLE;
              """
            )

def importAnime(animename, frtname):
    dic_chs = {}

    currDir = os.path.dirname(os.path.abspath(__file__))

    
    fsrt = os.path.join(currDir, frtname)
    strs = "\n"+readstring(fsrt)+"\n"
    iters = re.finditer(r"\n\d+\n", strs, re.DOTALL)
    poss = [ i.span() for i in iters ]


    #animename = 'Danganronpa'

    chinese = []
    jpanese = []
    for i in range( len(poss) ):
        (start, end) = poss[i]
        
        n = strs[start:end]

        content = None
        if i == ( len(poss) - 1 ):
            content = strs[ end : len(strs) ]
        else:
            content = strs[ end : poss[i+1][0] ]
        
        arr = content.strip().split('\n')
        if len(arr) < 2:
          continue
        time = content.strip().split('\n')[0]
        content = content.strip().split('\n')[1]



        

        if len( re.compile(r'size=.+>(.+?)\<\/font\>').findall(content) ) > 0:
          subtitle = re.compile(r'size=.+>(.+?)\<\/font\>').findall(content)[0]
        else:
          content = re.compile(r"""face=".+?\"""").sub('', content)
          content = re.compile(r"""size="\d+\"""").sub('', content)
          content = re.compile(r"""color=".+?\"""").sub('', content)
          content = re.compile(r"""<font.+?>""").sub('', content)
          content = re.compile(r"""{\\an7}""").sub('', content)
          
          subtitle = content

        # elif match := re.compile("""(<font face=".+?" size="\d+"><font size="\d+">).+?""").search(content):
        #   m = match.group(1)
        #   subtitle = content.replace(m, "")
        # elif match := re.compile(r"""(<font face=".+?" size="\d+"><font face=".+?">{\\an\d+}<font size="\d+">).+?""").search(content):
        #   m = match.group(1)
        #   subtitle = content.replace(m, "")
        # else:
        #   raise RuntimeError('some err')

        subtitle = subtitle.replace('<b>','').replace('</b>','')
        
        chrst = chardet.detect(subtitle.encode())

        
        if chrst['encoding'] == 'ascii' and chrst['confidence'] > 0.99:
            b = 1
        elif hasHanaQ(subtitle): # 有jia ming 的是jp
          jpanese.append( (subtitle, time) )
        else:
            tmp = unchinese_remove(subtitle)
            if tmp != "":
              
              if time in dic_chs:
                continue
                #raise RuntimeError('some err')
              
              dic_chs[time] = subtitle

              tmp = "|".join( list(tmp) )
              begin = time.split('-->')[0].strip()
              end = time.split('-->')[1].strip()
              allhasjpduyingQ = False





              # with psycopg2.connect(database='anime', user='postgres', password='postgres',host=host, port=port) as conn: 
              #   with conn.cursor() as cur:
              #     sql = f"select JPQ ('{tmp}');"
              #     cur.execute( sql )
              #     row = cur.fetchone()
              #     tt = row[0]
              #     if row[0] == 1:
              #       allhasjpduyingQ = True
              #     else:
              #       allhasjpduyingQ = False

              #chinese.append( (subtitle, time) )

    # writestring('jp.txt', "\r\n".join(jpanese[0]+jpanese[1]))
    # writestring('ch.txt', "\r\n".join(chinese[0]+chinese[1]))


    with psycopg2.connect(database='anime', user='postgres', password='postgres',host=host, port=port) as conn:
        with conn.cursor() as cur:
          
            cur.execute('BEGIN;')

            for idx, tu in enumerate(jpanese):
                j = tu[0]
                zh = ""
                # if (idx < len(chinese)):
                #     zh = chinese[idx][0].replace("(", "`(`").replace(")", "`)`")
                tags = tagger.parse(j)
                #tags = tags.split('\n')
                t = tu[1]
                if (t in dic_chs):
                  zh = dic_chs[t].replace("(", "`(`").replace(")", "`)`").replace("'", "''")
                sql = f"""insert into anime(name, jp, time, jp_mecab, zh, v_zh) values('{animename}', '{j}', '{t}', '{tags}', '{zh}', to_tsvector('jiebacfg', '{zh}'));"""
                cur.execute( sql )
            
            cur.execute('COMMIT;')


    with psycopg2.connect(database='anime', user='postgres', password='postgres',host=host, port=port) as conn:
        with conn.cursor() as cur:
            #cur.execute("SELECT * FROM anime WHERE jp &@ '遅刻';")
            cur.execute("SELECT * FROM anime WHERE jp_mecab &@ 'チコク';")
            rows = cur.fetchall()
    
    # with psycopg2.connect(database='postgres', user='postgres', password='postgres',host=host, port=port) as conn:
    #     conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    #     with conn.cursor() as cur:
    #         cur.execute("DROP DATABASE IF EXISTS anime;")

    print("hi,,,")

if __name__ == "__main__":

    host = '111.229.53.195'
    port = 54322

    createAnimeDB(host, port)

    #parseSrtTime('')
    root = r"F:\Downloads\[Kamigami] Danganronpa Kibou no Gakuen to Zetsubou no Koukousei The Animation [1280x720 x264 AAC MKV Sub(Chs,Jap)]"
    #root = r"F:\Downloads\Dan"

    fnames = allfname(root, 'mkv')
    for fname in fnames:
      frtname = f"{fname}.srt"
      fname = os.path.join( root, fname )
      out_bytes = subprocess.check_output([r"ffmpeg", "-i", fname, "-map", "0:s:0", frtname])
      out_text = out_bytes.decode('utf-8')

      animename = 'Danganronpa'
      importAnime(animename, frtname)









