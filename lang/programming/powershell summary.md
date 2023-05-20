

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

$networks = docker network ls
if ($networks -notmatch 'customnetwork') {
    Write-Host 'customnetwork not found, create'
    docker network create --subnet=172.20.0.0/16 customnetwork
    Write-Host 'customnetwork create success'
}

```





