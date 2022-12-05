$FileList = Get-ChildItem -Path packages
foreach ($File in $FileList)
{
	Set-Location -Path packages\$File
	$File
	if (((Get-ChildItem -Directory | Measure-Object).Count) -gt 5)
	{			
		Write-Output "This folder has more than 5 files"
		Get-ChildItem | where {$_.LastWriteTime -lt (date).adddays(-30) }
	}	
	Set-Location -Path ../../	
}