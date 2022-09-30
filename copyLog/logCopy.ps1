[string]$xmldocpath = "test.xml"

$xmldoc = New-Object "system.xml.xmldocument"
$xmldoc.load($xmldocpath)
$nodelist = $xmldoc.GetElementsByTagName("Server");

foreach ($node in $nodelist) {
    $childnodes = $node.ChildNodes
    $TesterName = $childnodes.Item(0).InnerXml.ToString()
    $Path = "\\$TesterName\c$\Data\Service\"
    $logCount = $childnodes.Item(1).InnerXml.ToString()
    $Destination = $childnodes.Item(2).InnerXml.ToString()
    $DestinationPath = "$Destination\\$TesterName"
    $dateStart = (Get-Date).adddays(-$logCount+1).ToString("MMdd")
    $dateTo = (Get-Date).ToString("MMdd")
    Write-Host $dateStart $dateTo

    #add dateStart and dateTo into a list
    $dataList = @($dateStart, $dateTo)

    foreach($data in $dataList)
    {
        Write-Host $data
        # list files in directory which file name contain today's date
        $files = Get-ChildItem -Path $Path -Filter "*$data.txt" -Recurse
        foreach ($file in $files) {
            Write-Host $files.Name
            #create a folder first if not exist
            if (!(Test-Path -Path $DestinationPath)) {
                New-Item -ItemType Directory -Path $DestinationPath
            }
            Copy-Item -Path $file.FullName -Destination  $DestinationPath -Recurse -Force
        }
    }
}