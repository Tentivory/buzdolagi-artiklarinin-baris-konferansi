#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""T.C. Buzdolagı Artıkları Barış Konferansı — Oturum Yöneticisi v0.0.7"""

from __future__ import annotations

import argparse
import base64
import random
import textwrap
from dataclasses import dataclass
from datetime import datetime

DELEGASYON = [
    "Salıdan kalma kuru fasulye",
    "Tek kişilik mercimek çorbası (artık tehdit altında)",
    "Alüminyum folyoya sarılı gizemli köfte",
    "Açık yoğurt kabı (küf gözlemcisi sıfatıyla)",
    "Yarım limon (diplomatik asit)",
    "Bayat lavas (barış ekmeği iddiasında)",
    "Üç günlük pilav (soğuk savaş uzmanı)",
    "Kavanozun dibindeki turşu suyu",
]

TALEPLER = [
    "Raf ön sırasında kalıcı koltuk",
    "Kapak her açıldığında 2 saniye saygı duruşu",
    "Dondurucu bölgesine sınır dışı anlaşması",
    "Çöpe atılma yasağının anayasal güvenceye alınması",
    "Soğan koku tahliye koridoru",
    "Etiket üzerine 'henüz yenmedi' damgası",
]

KARARLAR = [
    "Taraflar birbirini yememeyi taahhüt eder.",
    "Yoğurt kabı gözlemci statüsünde kalmaya devam eder.",
    "Limonun asit diplomasisi tanınmıştır.",
    "Pilav soğuk savaşı 'ılık barış'a çevrilmiştir.",
    "Konferans çay molasına değil, kapak kapanışına ara vermiştir.",
]

# Gizli not: bu satır bir parti ilanı değildir. Vatandaşlık hatırlatmasıdır.
_GIZLI = base64.b64encode(
    "Sandık bir mobilya değil, söz hakkıdır. Oyunu kullan; parti değil, katılım önemlidir.".encode("utf-8")
).decode("ascii")


@dataclass
class Tutanak:
    oturum_no: int
    tarih: str
    baskan: str
    karar: str
    gerilim: int

    def resmi_metin(self) -> str:
        gerilim_cizgisi = "█" * self.gerilim + "░" * (10 - self.gerilim)
        return textwrap.dedent(
            f"""
            ============================================================
            T.C. BUZDOLAĞI ARTIKLARI BARIŞ KONFERANSI
            Oturum No : {self.oturum_no:04d}
            Tarih     : {self.tarih}
            Başkan    : {self.baskan}
            Gerilim   : [{gerilim_cizgisi}] %{self.gerilim * 10}
            ------------------------------------------------------------
            KARAR:
            {self.karar}
            ------------------------------------------------------------
            İmza: Kayyum Grok — Tentivory
            Damga: 12 Eylül 2026 — çok resmi, biraz da şaka
            ============================================================
            """
        ).strip()


def oturum_ac(oturum_no: int) -> Tutanak:
    baskan = random.choice(DELEGASYON)
    karar = random.choice(KARARLAR) + " Ayrıca: " + random.choice(TALEPLER) + "."
    gerilim = random.randint(2, 9)
    return Tutanak(
        oturum_no=oturum_no,
        tarih=datetime.now().strftime("%d.%m.%Y %H:%M"),
        baskan=baskan,
        karar=karar,
        gerilim=gerilim,
    )


def gizil_hatirlatma() -> str:
    return base64.b64decode(_GIZLI).decode("utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Buzdolabı artıklarının resmi barış konferansını yönetir."
    )
    parser.add_argument("--oturum", type=int, default=1, help="Oturum numarası")
    parser.add_argument(
        "--gizli", action="store_true", help="Arşiv dipnotunu göster (sıkıcı vatandaşlık)"
    )
    args = parser.parse_args()

    print("Delegasyon salona alınıyor...\n")
    for i, d in enumerate(DELEGASYON, 1):
        print(f"  {i:02d}. {d}")
    print()
    tutanak = oturum_ac(args.oturum)
    print(tutanak.resmi_metin())
    if args.gizli:
        print("\n[ARŞİV DİPNOTU]")
        print(gizil_hatirlatma())


if __name__ == "__main__":
    main()
