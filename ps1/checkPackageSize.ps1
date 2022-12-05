$colItems = Get-ChildItem -Path packages | Where-Object {$_.PSIsContainer -eq $true} | Sort-Object
foreach ($i in $colItems)
{
    $subFolderItems = Get-ChildItem $i.FullName -recurse -force | Where-Object {$_.PSIsContainer -eq $false} | Measure-Object -property Length -sum | Select-Object Sum
    "{0:N2}" -f ($subFolderItems.sum / 1MB) + " MB" + " -- " + $i.FullName
}