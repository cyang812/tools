oh-my-posh init pwsh --config "$env:POSH_THEMES_PATH/atomicBit.omp.json" | Invoke-Expression

Write-Host -Foreground Green "`n[ZLocation] knows about $((Get-ZLocation).Keys.Count) locations.`n"

# Default proxy host
$global:proxyHost = "127.0.0.1"
$global:defaultProxyPort = 12334

function proxy {
    param (
        [int]$Port = $global:defaultProxyPort
    )

    $proxyUrl = "http://$($global:proxyHost):$Port"

    $env:http_proxy  = $proxyUrl
    $env:https_proxy = $proxyUrl

    [System.Net.WebRequest]::DefaultWebProxy = New-Object System.Net.WebProxy($proxyUrl)

    Write-Host "Proxy enabled: $proxyUrl" -ForegroundColor Green
}

function unproxy {
    $env:http_proxy  = $null
    $env:https_proxy = $null

    [System.Net.WebRequest]::DefaultWebProxy = $null

    Write-Host "Proxy disabled" -ForegroundColor Yellow
}

function check-proxy {
    if ($env:http_proxy -or $env:https_proxy) {
        Write-Host "Current proxy settings:" -ForegroundColor Cyan
        Write-Host "HTTP Proxy : $env:http_proxy"
        Write-Host "HTTPS Proxy: $env:https_proxy"
    } else {
        Write-Host "No proxy is currently set." -ForegroundColor Cyan
    }
}

# Import the Chocolatey Profile that contains the necessary code to enable
# tab-completions to function for `choco`.
# Be aware that if you are missing these lines from your profile, tab completion
# for `choco` will not function.
# See https://ch0.co/tab-completion for details.
$ChocolateyProfile = "$env:ChocolateyInstall\helpers\chocolateyProfile.psm1"
if (Test-Path($ChocolateyProfile)) {
  Import-Module "$ChocolateyProfile"
}
