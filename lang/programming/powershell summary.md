

# String



## match



```
$t = $(docker image ls) -like "*almalinux*8.7*"
if (-not $t)
{
    Write-Host 'almalinux:8.7 not found, pull'
    docker pull almalinux:8.7
    Write-Host 'almalinux:8.7 pull success'
}

$imageExists = docker image ls | Select-String -Pattern '8.7'
if ($imageExists -eq $null) {
    Write-Host 'almalinux:8.7 not found, pull'
    docker pull almalinux:8.7
    Write-Host 'almalinux:8.7 pull success'
}
```





