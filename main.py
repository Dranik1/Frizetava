import itertools
import datetime
from datetime import time

class Pakalpojums:
    Pakalpojuma_kategorija=""
    Pakalpojuma_nosaukums=""
    Pakalpojuma_atlaide=""
    Pakalpojuma_cena=0

    id_iter=itertools.count()

    def __init__(self, pak_kat=None, pak_nos=None, pak_atl=None, pak_cena=10):
        self.Pakalpojums_id=next(self.id_iter)+1
        self.Pakalpojuma_kategorija=pak_kat
        self.Pakalpojuma_nosaukums=pak_nos
        self.Pakalpojuma_atlaide=pak_atl
        self.Pakalpojuma_cena_stunda=pak_cena
        self.Laiks_pieejams=True

    def Pakalpojums_info(self):
        return [
            self.Pakalpojuma_kategorija, self.Pakalpojuma_nosaukums, self.Pakalpojuma_atlaide, self.Pakalpojuma_cena_stunda
        ]
    
    