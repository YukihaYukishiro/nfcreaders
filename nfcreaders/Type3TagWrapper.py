import nfc.tag.tt3 as tt3

class T3TData:

    def __init__(self,tag):
        # データがtt3であることを保証する
        if not isinstance(tag,tt3.Type3Tag):
            raise Type3TagExeption(tag)
        self._tag = tag
        self._id = tag.idm
        self._pmm =tag.pmm
        self._sys =tag.sys

    def __str__(self):
        return f"ID:{self._id.hex()} Pmm:{self._pmm.hex()} Sys:{self._sys.to_bytes(length=2).hex()}"
    
    @property
    def id(self):
        return self._id.hex()
    
    @property
    def pmm(self):
        return self._pmm.hex()
    
    @property
    def sys(self):
        return self._sys.to_bytes(length=2).hex()

    @property
    def id_bytes(self):
        return self._id
    
    @property
    def pmm_bytes(self):
        return self._pmm
    
    @property
    def sys_bytes(self):
        return self._sys.to_bytes(length=2)

    @property
    def sys_raw(self):
        return self._sys

    @property
    def tag(self):
        return self.tag

    def json(self)->dict: 
        id_hex=self._id.hex()
        pmm_hex=self._pmm.hex()
        sys_hex=self._sys.to_bytes(length=2).hex()

        return {'id':id_hex,'pmm':pmm_hex,'sys':sys_hex}
    
class NfcTypeError(Exception):
    def __init__(self, arg):
        self.arg = arg

class Type3TagExeption(NfcTypeError):
    def __str__(self):
        return (
            f"[{self.arg}] is not Type3Tag.\nOnly Type3Tag is available here."
        )