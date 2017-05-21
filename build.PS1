cd $PSScriptRoot

echo "Building resourcepack .zip files"
mkdir -Force "distributables"

function ZipFiles( $zipfilename, $sourcedir )
{
	echo "$sourcedir -> $zipfilename"
	Add-Type -Assembly System.IO.Compression.FileSystem
	$sourcedir_abs=resolve-path "$sourcedir"
	$zipfilename_abs=join-path "$PSScriptRoot" "$zipfilename"
	[System.IO.Compression.ZipFile]::CreateFromDirectory($sourcedir_abs, $zipfilename_abs)
}

ZipFiles -zipfilename "distributables/CCH-Minecraft_x16.zip" -sourcedir "./x16"
#ZipFiles -zipfilename "distributables/CCH-Minecraft_x32.zip" -sourcedir "./x32"
#ZipFiles -zipfilename "distributables/CCH-Minecraft_x64.zip" -sourcedir "./x64"