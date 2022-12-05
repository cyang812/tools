$FileList = Get-ChildItem -Path packages
foreach ($File in $FileList)
{
	Set-Location -Path packages\$File
	$File
	if (((Get-ChildItem -Directory | Measure-Object).Count) -gt 5)
	{	
		
		Write-Output "This folder has more than 5 files"
		$removedFileList = Get-ChildItem | where {$_.LastWriteTime -lt (date).adddays(-30) }
		foreach ($removedFile in $removedFileList)
		{
			$removedFile
			Write-Output "has been removed"	
		}		
		Get-ChildItem | where {$_.LastWriteTime -lt (date).adddays(-30) } | Remove-Item -Recurse -Force -Confirm:$false
	}	
	Set-Location -Path ../../	
}