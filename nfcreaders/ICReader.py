import nfc

class NFCTagReader:
    
    def __init__(self,connecter='usb'):
        # self._clf NFCタグの読み取り用クラスの定義
        # self._reader_type リーダーの接続方法
        # self._returndata 戻り値の一時保管用

        self._clf = nfc.ContactlessFrontend()
        self._reader_type = connecter 
        self._returndata = None

    #コールバック関数
    def _on_connect(self,tag,on_release:bool):
        
        # 取得したタグを一時保存
        self._returndata = tag
        return on_release #True Falseの選択
    
    def wait_for_contact(self,on_release=False):

        # 読み取り機の起動
        self._clf.open(self._reader_type)
        
        # カード読み取り
        try:
            # 読み取りを待機する
            self._clf.connect(rdwr={'on-connect':lambda tag :self._on_connect(tag,on_release)})
        finally:
            # 読み取りを終了
            self._clf.close()
            # 値の返却
            return self._returndata
    
