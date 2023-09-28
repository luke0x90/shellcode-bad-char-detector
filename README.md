# shellcode-bad-char-detector
Find bad chars in your shellcode
# How to use

* Locate your shellcode in memory using WinDbg.
* Copy the hexdump `dd eip L100` into the bad_chars_hunter.py file
* Add your `msfvenom` output too
* Set the aligner to bypass any `nop`s
* Run
* Copy entire console output into CyberChef->Diff
* Diff by Word

Bad chars can cause subsequent bytes to get mangled or just cause it to be replaces with another.
