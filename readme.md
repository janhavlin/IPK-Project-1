
Implementační dokumentace k 1. úloze do IPK 2018/2019
Jméno a příjmení: Jan Havlín
Login: xhavli47

## Popis úlohy
Aplikace získává prostřednictvím HTTP dotazů data ohledně počasí ve zvolené lokalitě. Tato data tiskne na standardní výstup.

## Návrh řešení
Program je napsán v jazyce Python 3.6.7. Program je spouštěn pomocí příkazu make s dvěma parametry, které jsou souborem Makefile předány skriptu. Při nesprávném počtu parametrů program končí s chybou. Neznámé parametry jsou ignorovány, na pořadí parametrů nezáleží.

Skript importuje externí knihovnu pro práci se sokety a json soubory.

Program se pomocí soketu připojí na vzdálený server OpenWeatherMap a odešle HTML request. V případě úspěchu (návratový kód je roven 200) vypíše získaná data v json podobě čitelně na standardní výstup. 

## Instalace
Archiv rozbalte do libovolného adresáře. Pro správnou funkčnost jsou nezbytné programy make a python3.

## Spuštění
Program se spouští příkazem **make run api_key=*API_KLÍČ* city=*MĚSTO***, kde *API_KLÍČ* je Váš vlastní OpenWeatherMap klíč, *MĚSTO* je název města (případně státu), jehož data o počasí chcete získat.