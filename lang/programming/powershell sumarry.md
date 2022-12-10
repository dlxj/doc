

# regex

- https://petri.com/powershell-grep-select-string/
- https://lazyadmin.nl/powershell/string-contains

```
$h = Get-content $file | select-string "^ID\s+Chassis" # 返回所有匹配的行

$string -contains "how to find a word"  # True

if ($string -like "*find*") { 
  Write-host "String contains find"
}

```

