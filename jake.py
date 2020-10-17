# Python code obfuscated by www.development-tools.net 
 

import base64, codecs
magic = 'aW1wb3J0IHJlcXVlc3RzLGpzb24sdGltZSxzeXMscmFuZG9tLG9zDQppbXBvcnQgY29sb3JhbWENCmZyb20gY29sb3JhbWEgaW1wb3J0IEZvcmUsIEJhY2ssIFN0eWxlDQpmcm9tIHJhbmRvbSBpbXBvcnQgcmFuZGludA0KZnJvbSBkYXRldGltZSBpbXBvcnQgZGF0ZXRpbWUNCmNvbG9yYW1hLmluaXQoYXV0b3Jlc2V0PVRydWUpDQoNCnBpbGloYW4gPSBzeXMuYXJndlsxXQ0KDQp3aXRoIG9wZW4oJ2RpY2UuanNvbicsICdyJykgYXMgbXlmaWxlOg0KICAgICAgZGF0YT1teWZpbGUucmVhZCgpDQojIHBhcnNlIGZpbGUNCm9iaiA9IGpzb24ubG9hZHMoZGF0YSkNCg0KaW1wb3J0IGNvbG9yYW1hDQpmcm9tIGNvbG9yYW1hIGltcG9ydCBGb3JlLCBCYWNrLCBTdHlsZQ0KY29sb3JhbWEuaW5pdChhdXRvcmVzZXQ9VHJ1ZSkNCmhpamF1ID0gU3R5bGUuUkVTRVRfQUxMK1N0eWxlLkJSSUdIVCtGb3JlLkdSRUVODQpyZXMgPSBTdHlsZS5SRVNFVF9BTEwNCmFidTIgPSBTdHlsZS5ESU0rRm9yZS5XSElURQ0KYmlydSA9IFN0eWxlLlJFU0VUX0FMTCtTdHlsZS5CUklHSFQrRm9yZS5CTFVFDQp1bmd1MiA9IFN0eWxlLk5PUk1BTCtGb3JlLk1BR0VOVEENCnVuZ3UgPSBTdHlsZS5SRVNFVF9BTEwrU3R5bGUuQlJJR0hUK0ZvcmUuTUFHRU5UQQ0KaGlqYXUyID0gU3R5bGUuTk9STUFMK0ZvcmUuR1JFRU4NCnllbGxvdzIgPSBTdHlsZS5OT1JNQUwrRm9yZS5ZRUxMT1cNCnllbGxvdyA9IFN0eWxlLlJFU0VUX0FMTCtTdHlsZS5CUklHSFQrRm9yZS5ZRUxMT1cNCnJlZDIgPSBTdHlsZS5OT1JNQUwrRm9yZS5SRUQNCnJlZCA9IFN0eWxlLlJFU0VUX0FMTCtTdHlsZS5CUklHSFQrRm9yZS5SRUQNCmN5YW4gPSBTdHlsZS5CUklHSFQrRm9yZS5DWUFODQpjeWFuMiA9IFN0eWxlLk5PUk1BTCtGb3JlLkNZQU4NCmRlcyA9IFN0eWxlLkJSSUdIVCtGb3JlLkdSRUVOKyLjgI7wn5Sl44CPIg0Ka3VyMSA9IFN0eWxlLkJSSUdIVCtGb3JlLlJFRCsiWyINCmt1cjIgPSBTdHlsZS5CUklHSFQrRm9yZS5SRUQrIl0iDQoNCm9zLnN5c3RlbSgnY2xzJyBpZiBvcy5uYW1lPT0nbnQnIGVsc2UgJ2NsZWFyJykNCmMgPSByZXF1ZXN0cy5TZXNzaW9uKCkNCmJhbm5lciA9KGYiIiJ7eWVsbG93fQ0KCV8gIF8gXyAgXyBfICAgIF8gICAgX19fXyBfICBfIF8gICAgXyBfICBfIF9fX18gDQoJfF8vICB8ICB8IHwgICAgfCAgICB8ICB8IHxcIHwgfCAgICB8IHxcIHwgfF9fXyANCgl8IFxfIHxfX3wgfF9fXyB8ICAgIHxfX3wgfCBcfCB8X19fIHwgfCBcfCB8X19fIA0Ke2hpamF1fT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PQ0Ke3JlZH1bIHtiaXJ1fUNSRUFURUQgQlkgQU5UTyBYVVpVVOKEoiB7cmVkfV0NCntoaWphdX3CqSBUZWxlZ3JhbSB7cmVkfToge2hpamF1fUBrdWxpX29ubGluZV9jaGFubmVsDQp7aGlqYXV9wqkgWW91dHViZSAge3JlZH06IHtoaWphdX1LVUxJIE9OTGluZQ0Ke2hpamF1fVN1cHBvcnQgQnkge3JlZH06IHtoaWphdX1AQW5kaUthY2hvIEBMdWlzY3N0bCBAUm96emExNQ0Ke2hpamF1fVRoYW5rcyBGb3Ige3JlZH06IHtoaWphdX1AdXJhbmdqYXdhOTggQHJpY2t5YWxleGFuZGVybSBASmFpbmFiTG92ZQ0Ke2hpamF1fURvbmFzaSAgICAge3JlZH06IHtoaWphdX1EN3duYjQyOVg3Tll6bVNBOFh5OFdlc2NXbmo5ZHFHOG1QKERvZ2UpDQp7aGlqYXV9PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09DQp7cmVkfVt7YmlydX0gU0NSSVBUIDk5OURJQ0UgTVVMVEkgQ1VSUkVOQ1kgIHtyZWR9XQ0Ke2hpamF1fT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PVxuIiIiKQ0KICAgIA0KcHJpbnQoYmFubmVyKQ0KYmdfYWIgPSAnXHgxYlsxOzM2OzEwMG0nDQpiZ19hYjIgPSAnXHgxYlsxOzM3OzEwMG0nDQpiZ19yZCA9ICdceDFiWzE7Mzc7NDFtJw0KYmdfaWogPSAnXHgxYlswOzMwOzQybScNCmJnX2VuZCA9ICdceDFiWzBtJw0KDQprbiA9ICJcMDMzWzE7OTNtIg0Ka24yID0gIlwwMzNbMTszOzkzbSINCmFiID0gJ1wwMzNbMTs5MG0nDQppaiA9ICdcMDMzWzkybScNCnJkID0gJ1wwMzNbMTs5MW0nDQpwaCA9ICdcMDMzWzk3bScNCnJzID0gJ1wwMzNbMDswbScNCg0KDQpjID0gcmVxdWVzdHMuc2Vzc2lvbigpDQphPTANCnVybCA9ICJodHRwczovL3d3dy45OTlkb2dlLmNvbS9hcGkvd2ViLmFzcHgiDQp1YSA9IHsNCiAiT3JpZ2luIjogImZpbGU6Ly8iLA0KICJ1c2VyLWFnZW50IjogICJva2h0dHAvNC4yLjIiLA0KICJDb250ZW50LXR5cGUiOiAiYXBwbGljYXRpb24veC13d3ctZm9ybS11cmxlbmNvZGVkIiwNCiAiQWNjZXB0IjogIiovKiIsDQogIkFjY2VwdC1MYW5ndWFnZSI6ICJpZC1JRCxpZDtxPTAuOSxlbi1VUztxPTAuOCxlbjtxPTAuNyIsDQogIlgtUmVxdWVzdGVkLVdpdGgiOiAiY29tLnJlbGFuZC5yZWxhbmRpY2Vib3QiDQp9DQppZiBwaWxpaGFuID09ICdkb2dlJzoNCgljcnkgPSAiRG9nZSINCgl0YXJnZXQgPSBvYmpbIldpdGhkcmF3Il1bIldhbGxldF9kb2dlIl0NCgl3bHQgPSAiV2FsbGV0X2RvZ2UiDQppZiBwaWxpaGFuID09ICdsdGMnOg0KCWNyeSA9ICJMVEMiDQoJdGFyZ2V0ID0gb2JqWyJXaXRoZHJhdyJdWyJXYWxsZXRfbHRjIl0NCmlmIHBpbGloYW4gPT0gJ2J0Yyc6DQoJY3J5ID0gIkJUQyINCgl0YXJnZXQgPSBvYmpbIldpdGhkcmF3Il1bIldhbGxldF9idGMiXQ0KaWYgcGlsaWhhbiA9PSAnZXRoJzoNCgljcnkgPSAiRVRIIg0KCXRhcmdldCA9IG9ialsiV2l0aGRyYXciXVsiV2FsbGV0X2V0aCJdDQoJDQoJDQpkZWYgX2xvd2VyY2FzZShvYmopOg0KICAgIGlmIGlzaW5zdGFuY2Uob2JqLCBkaWN0KToNCiAgICAgICAgcmV0dXJuIHtrLmxvd2VyKCk6X2xvd2VyY2FzZSh2KSBmb3IgaywgdiBpbiBvYmouaXRlbXMoKX0NCiAgICBlbGlmIGlzaW5zdGFuY2Uob2JqLCAobGlzdCwgc2V0LCB0dXBsZSkpOg0KICAgICAgICB0ID0gdHlwZShvYmopDQogICAgICAgIHJldHVybiB0KF9sb3dlcmNhc2UobykgZm9yIG8gaW4gb2JqKQ0KICAgIGVsaWYgaXNpbnN0YW5jZShvYmosIHN0cik6DQogICAgICAgIHJldHVybiBvYmoubG93ZXIoKQ0KICAgIGVsc2U6DQogICAgICAgIHJldHVybiBvYmoNCg0KZGVmIGtvbnZlcnQocGVyc2VuLHRhcnVoYW4pOg0KICAgIGdsb2JhbCBoaWdoDQogICAgZ2xvYmFsIGxvdw0KICAgIGMgPSBzdHIoOTk5OTk5ICogZmxvYXQocGVyc2VuKSAvIDEwMCkNCiAgICBpZiB0YXJ1aGFuID09ICJoIiBvciB0YXJ1aGFuID09ICJIIjoNCiAgICAgICBuID0gc3RyKGMuc3BsaXQoIi4iKVsxXSkNCiAgICAgICBwYW5na2F0ID0gNiAtIGxlbihuKQ0KICAgICAgIGxvdyA9IGludChpbnQobikgKiAoMTAgKiogcGFuZ2thdCkpDQogICAgICAgaGlnaCA9IDk5OTk5OQ0KICAgIGlmIHRhcnVoYW4gPT0gImwiIG9yIHRhcnVoYW4gPT0gIkwiOg0KICAgICAgIGxvdyA9IDANCiAgICAgICBoaWdoID0gaW50KGMuc3BsaXQoIi4iKVswXSkNCg0KDQpkZWYgcmV2KG51bSk6DQog'
love = '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'
god = 'ICAgICAgIGlmIGNvayA9PSAzOg0KICAgICAgICAgICAgICBjaGFuY2UgPSBiZ19hYisiICIrc3RyKGhhc2lsX2NoYW5jZSkrIiAgICIrIiUiKyIgIitiZ19lbmQNCiAgICAgICAgICAgaWYgY29rID09IDQ6DQogICAgICAgICAgICAgIGNoYW5jZSA9IGJnX2FiKyIgIitzdHIoaGFzaWxfY2hhbmNlKSsiICAiKyIlIisiICIrYmdfZW5kDQogICAgICAgICAgIGlmIGNvayA9PSA1Og0KICAgICAgICAgICAgICBjaGFuY2UgPSBiZ19hYisiICIrc3RyKGhhc2lsX2NoYW5jZSkrIiAiKyIlIisiICIrYmdfZW5kDQogICAgICAgICAgIGtvbnZlcnQoaGFzaWxfY2hhbmNlLHN0cihfbG93ZXJjYXNlKHJvbGViZXQpKSkNCiAgICAgICAgZWxzZToNCiAgICAgICAgICAgY2hhbmNlID0gYmdfYWIyKyIgICIrc3RyKG9ialsiSW50ZXJmYWNlIl1bIkNoYW5jZSJdKSsiICUiKyIgIitiZ19lbmQNCiAgICAgICAgICAgDQogICAgICAgICAgIGtvbnZlcnQob2JqWyJJbnRlcmZhY2UiXVsiQ2hhbmNlIl0sc3RyKF9sb3dlcmNhc2Uocm9sZWJldCkpKQ0KDQogICAgICAgIGFtb3VudCA9IGludChhbW91bnQpDQogICAgICAgIG4rPTENCiAgICAgICAgZGF0YSA9IHsNCiAgICAgICAgICAiYSI6ICJQbGFjZUJldCIsDQogICAgICAgICAgInMiOiBqc1siU2Vzc2lvbkNvb2tpZSJdLA0KICAgICAgICAgICJQYXlJbiI6IGFtb3VudCwNCiAgICAgICAgICAiTG93IjogbG93LA0KICAgICAgICAgICJIaWdoIjogaGlnaCwNCiAgICAgICAgICAiQ2xpZW50U2VlZCI6IHNlZWQsDQogICAgICAgICAgIkN1cnJlbmN5IjogY3J5LA0KICAgICAgICAgICJQcm90b2NvbFZlcnNpb24iOiAiMiINCiAgICAgICAgfQ0KICAgICAgICBpZiBwcm9mID4gZmxvYXQob2JqWyJTdG9wIl1bIklmX1Byb2YiXSk6DQogICAgICAgICAgIHByaW50IChoaWphdSsiXG5ZYXkuISBcblByb2ZpdCBNZW5jYXBhaSBUYXJnZXQuLi4uLiFcbiIraGlqYXUrIlByb2ZpdCAiK3JlcytzdHIocHJvZikpDQogICAgICAgICAgIHN5cy5leGl0KCkNCiAgICAgICAgDQogICAgICAgIHIxID0gYy5wb3N0KHVybCxoZWFkZXJzPXVhLGRhdGE9ZGF0YSkNCiAgICAgICAganNuID0ganNvbi5sb2FkcyhyMS50ZXh0KQ0KICAgICAgICB0cnk6DQogICAgICAgICAgIHByb2YgPSAoZmxvYXQoanNuWyJTdGFydGluZ0JhbGFuY2UiXSArIGludChqc25bIlBheU91dCJdKSAtIGludChhbW91bnQpIC0ganVtYmwpLygxMCAqKiA4KSkNCiAgICAgICAgZXhjZXB0IEtleUVycm9yOg0KICAgICAgICAgICBwcmludCAoJ1x4MWJbMDszMDsxMDBtJysiICIqMTgrIk5PIE1PUkUgQkFMQU5DRSIrIiAiKjE4KydceDFiWzBtJykNCiAgICAgICAgICAgc3lzLmV4aXQoKQ0KICAgICAgICBwcm9mdyA9IGpzblsiU3RhcnRpbmdCYWxhbmNlIl0gKyBpbnQoanNuWyJQYXlPdXQiXSkgLSBpbnQoYW1vdW50KSAtIGp1bWJsDQogICAgICAgIHByb2ZsID0gc3RyKGpzblsiU3RhcnRpbmdCYWxhbmNlIl0gKyBpbnQoanNuWyJQYXlPdXQiXSkgLSBpbnQoYW1vdW50KSAtIGp1bWJsKS5yZXBsYWNlKCItIiwiIikNCiAgICAgICAganVtID0gaW50KGpzblsiUGF5T3V0Il0pIC0gaW50KGFtb3VudCkNCiAgICAgICAgYmxhbmNlID0gaW50KGpzblsiU3RhcnRpbmdCYWxhbmNlIl0pICsgaW50KGp1bSkNCg0KICAgICAgICBpZiBibGFuY2UgPiB3czoNCiAgICAgICAgICAgaWYgX2xvd2VyY2FzZShvYmpbIkludGVyZmFjZSJdWyJSYW5kb20iXVsiQXV0byJdKSA9PSAib24iOg0KICAgICAgICAgICAgICBwcmludCAoJ1x4MWJbMDszMDs0Mm0nKyIgIitzdHIocm9sZWJldCkrIiAiKydceDFiWzBtJysiICIraWorc3RyKHJldihzdHIoYW1vdW50KSkpLCJQcm9maXQiLGlqK3JldihzdHIocHJvZncpKSwiQmFsYW5jZSIsaWorc3RyKHJldihzdHIoYmxhbmNlKSkpK2hpamF1KyIgIitjcnkrcnMrIiAiK2NoYW5jZSkNCiAgICAgICAgICAgICAgcHJpbnQgKCdceDFiWzE7MzI7MTAwbScrIiAiKjE4KyJTVE9QIFRBUkdFVCBCQUxBTkNFIisiICIqMTgrJ1x4MWJbMG0nKQ0KICAgICAgICAgICBlbHNlOg0KICAgICAgICAgICAgICBwcmludCAoJ1x4MWJbMDszMDs0Mm0nKyIgIitzdHIocm9sZWJldCkrIiAiKydceDFiWzBtJysiICIraWorc3RyKHJldihzdHIoYW1vdW50KSkpLCJQcm9maXQiLGlqK3JldihzdHIocHJvZncpKSwiQmFsYW5jZSIsa24rc3RyKHJldihzdHIoYmxhbmNlKSkpK2hpamF1KyIgIitjcnkrcnMpDQogICAgICAgICAgICAgIHByaW50ICgnXHgxYlsxOzMyOzEwMG0nKyIgIioxNysiU1RPUCBUQVJHRVQgQkFMQU5DRSIrIiAiKjE3KydceDFiWzBtJykNCiAgICAgICAgICAgc3lzLmV4aXQoKQ0KDQogICAgICAgIGlmIGJsYW5jZSA8IGxzOg0KICAgICAgICAgICBwcmludCAoJ1x4MWJbMDszNzs0MW0nKyIgIitzdHIocm9sZWJldCkrIiAiKydceDFiWzBtJytyZCsiLSIrc3RyKHJldihzdHIoYW1vdW50KSkpLCJMb3NlICAiK3JkKyItIityZXYoc3RyKHByb2ZsKSksIkJhbGFuY2UiLGtuK3N0cihyZXYoc3RyKGJsYW5jZSkpKStoaWphdSsiICIrY3J5K3JzKQ0KICAgICAgICAgICBwcmludCAoJ1x4MWJbMDszNzs0MW0nKyIgIioxNCsiU1RPUCBUQVJHRVQgTE9TRSIrIiAiKjE1KydceDFiWzBtJykNCiAgICAgICAgICAgc3lzLmV4aXQoKQ0KDQogICAgICAgIGlmIGpzblsiUGF5T3V0Il0gaXMgbm90IGE6DQogICAgICAgICAgIG5vX3dpbiArPTENCiAgICAgICAgICAgbm9fbG9zZSA9IDANCiAgICAgICAgICAgYmFsID0gYmxhbmNlDQogICAgICAgICAgIGlmIHByb2YgPiAwOg0KICAgICAgICAgICAgICBpZiBfbG93ZXJjYXNlKG9ialsiSW50ZXJmYWNlIl1bIlJhbmRvbSJdWyJBdXRvIl0pID09ICJvbiI6DQogICAgICAgICAgICAgICAgIHByaW50ICgnXHgxYlswOzMwOzQybScrIiAiK3N0cihyb2xlYmV0KSsiICIrJ1x4MWJbMG0nKyIgIitpaitzdHIocmV2KHN0cihhbW91bnQpKSksIlByb2ZpdCIsaWorcmV2KHN0cihwcm9mdykpLCJCYWxhbmNlIixrbitzdHIocmV2KHN0cihiYWwpKSkraGlqYXUrIiAiK2NyeStycysiICIrY2hhbmNlKQ0KICAgICAgICAgICAgICBlbHNlOg0KICAgICAgICAgICAgICAgICBwcmludCAoJ1x4MWJbMDszMDs0Mm0nKyIgIitzdHIocm9sZWJldCkrIiAiKydceDFiWzBtJysiICIraWorc3RyKHJldihzdHIoYW1vdW50KSkpLCJQcm9maXQiLGlqK3JldihzdHIocHJvZncpKSwiQmFsYW5jZSIsa24rc3RyKHJldihzdHIoYmFsKSkpK2hpamF1KyIgIitjcnkrcnMpDQogICAgICAgICAgIGVsc2U6DQogICAgICAgICAgICAgcHJpbnQgKCdceDFiWzA7MzA7NDJtJysiICIrc3RyKHJvbGViZXQpKyIgIisnXHgxYlswbScrIiAiK2lqK3N0cihyZXYoc3RyKGFtb3VudCkpKSwiTG9zZSAgIityZCsiLSIrcmV2KHN0cihwcm9mbCkpLCJCYWxhbmNlIixrbitzdHIocmV2KHN0cihiYWwpKSkraGlqYXUrIiAiK2NyeSkNCiAgICAgICAgZWxzZToNCiAgICAgICAgICAgbm9fd2luID0gMA0KICAgICAgICAgICBub19sb3NlICs9MQ0KICAgICAgICAgICBpID0gMA0KICAgICAgICAgICBidXJzdCA9IFRydWUNCiAgICAgICAgICAgYmFsID0gYmxh'
destiny = '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'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))