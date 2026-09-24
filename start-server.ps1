$ErrorActionPreference = 'Stop'
$server = Join-Path $PSScriptRoot 'server'
$paper = Join-Path $server 'paper-1.16.5-794.jar'
$runtime = Join-Path $server 'runtime'
$java = if (Test-Path -LiteralPath $runtime) {
    Get-ChildItem -LiteralPath $runtime -Filter java.exe -Recurse |
        Where-Object { $_.FullName -match '\\bin\\java\.exe$' } |
        Select-Object -First 1 -ExpandProperty FullName
}
if (-not $java -and $env:JAVA_HOME) {
    $candidate = Join-Path $env:JAVA_HOME 'bin\java.exe'
    if (Test-Path -LiteralPath $candidate) { $java = $candidate }
}
if (-not $java) {
    $command = Get-Command java.exe -ErrorAction SilentlyContinue
    if ($command) { $java = $command.Source }
}
if (-not $java) { throw 'Java not found; install Java 16 or place it under server/runtime' }
if (-not (Test-Path -LiteralPath $paper)) { throw "Paper JAR not found: $paper" }
Push-Location $server
try {
    & $java -Xms1G -Xmx2G -jar $paper --nogui
} finally {
    Pop-Location
}
