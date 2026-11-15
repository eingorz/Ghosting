# Ghosting - Handbook

## Short description
Kolega si pohrál s rozložením české klávesnice. Zrekonstruuj původní zprávu a získej přístupový klíč.

---

## Description (Zadání pro studenty)
Kolega z IT rád experimentuje s mechanickými klávesnicemi a alternativním rozložením kláves. Zrovna ladil nový firmware a trochu si pohrál s keyboard layoutem na své české klávesnici.

Než odešel na oběd, poslal nám zprávu s přístupovým klíčem. Text ale na první pohled nedává smysl – očividně ho psal už s nově upraveným rozložením. Podaří se ti přijít na to, co s klávesami provedl, a zrekonstruovat původní zprávu?

```text
Jo. zjr gůsh od_ jscshpm{f,ůtsE6mX,BxvmůwUEcbf3zůrE6ůs,cůvJMúVh;;}
```

---

## Handbook / Writeup (Řešení pro učitele)

### 1. Analýza zadání
Zadání zmiňuje experimentování s **českou klávesnicí** a manipulaci s rozložením kláves (keyboard layoutem). V zašifrovaném textu se objevují typické české znaky jako `ů`, které se na standardní anglické klávesnici nevyskytují:

```text
Jo. zjr gůsh od_ jscshpm{f,ůtsE6mX,BxvmůwUEcbf3zůrE6ůs,cůvJMúVh;;}
```

Při detailním pohledu na rozložení české QWERTZ klávesnice a porovnání s očekávaným začátkem zprávy a formátem vlajky (`haxagon{...}`) je patrný jasný vzor:

* `Jo.` -> posun o 1 klávesu doleva odpovídá `Hi,` (na české klávesnici leží `J` vpravo od `H`, `o` vpravo od `i`, `.` vpravo od `,`)
* `zjr` -> `the` (na QWERTZ rozložení leží `z` hned vpravo od `t`, `j` vpravo od `h`, `r` vpravo od `e`)
* `gůsh` -> `flag` (`g` leží vpravo od `f`, `ů` vpravo od `l`, `s` vpravo od `a`, `h` vpravo od `g`)
* `od_` -> `is:` (`o` leží vpravo od `i`, `d` vpravo od `s`, `_` vpravo od `:`)
* `jscshpm{...}` -> `haxagon{...}` (`j` -> `h`, `s` -> `a`, `c` -> `x`, `s` -> `a`, `h` -> `g`, `p` -> `o`, `m` -> `n`)
* `;;` -> `==` (znak `=` je na konci horní číselné řady `;+ěščřžýáíé=`; posun o 1 doprava cyklicky přeteče zpět na začátek řady na `;`)

Každý znak v textu je tedy posunutý o **1 pozici doprava** v rámci své řady na české QWERTZ klávesnici (cyklicky – z konce řady se přechází na její začátek).

### 2. Postup řešení (Python)
Pro dešifrování je nejjednodušší napsat krátký skript v Pythonu, který definuje jednotlivé řady české QWERTZ klávesnice (včetně Shift vrstvy) a posune každý znak o `-1` (doleva):

```python
ROWS = [
    ";+ěščřžýáíé=",
    "qwertzuiopú)",
    "asdfghjklů§",
    "yxcvbnm,.-",
    "°1234567890%",
    "QWERTZUIOP/(",
    "ASDFGHJKL\"!'",
    "YXCVBNM?:_"
]

def shift_qwertz(text, shift=-1):
    result = []
    for char in text:
        found = False
        for row in ROWS:
            if char in row:
                idx = row.index(char)
                new_idx = (idx + shift) % len(row)
                result.append(row[new_idx])
                found = True
                break
        if not found:
            result.append(char)
    return "".join(result)

ciphertext = "Jo. zjr gůsh od_ jscshpm{f,ůtsE6mX,BxvmůwUEcbf3zůrE6ůs,cůvJMúVh;;}"
plaintext = shift_qwertz(ciphertext, shift=-1)

print(plaintext)
```

### 3. Výsledek
Spuštěním skriptu získáme původní zprávu obsahující vlajku:

```text
Hi, the flag is: haxagon{dmlraW5nYmVycnlqZWxvd2tleW5lamxlcHNpCg==}
```

**Flag:** `haxagon{dmlraW5nYmVycnlqZWxvd2tleW5lamxlcHNpCg==}`
