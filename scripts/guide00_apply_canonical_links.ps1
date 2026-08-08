Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$OldUrl = 'https://www.red-seal.ca/eng/contact/c.4nt.1ct.shtml'
$NewUrl = 'https://red-seal.ca/eng/about/program.shtml'

$Files = @(
    '00-foundation-guide/source/Lifelong_Opportunity_Foundation_Guide_English_v1.1_INTEGRATED_MASTER.md',
    '00-foundation-guide/source/Lifelong_Opportunity_Foundation_Guide_es-419_v1.1_INTEGRATED_MASTER.md',
    '00-foundation-guide/source/Lifelong_Opportunity_Foundation_Guide_pt-BR_v1.1_INTEGRATED_MASTER.md'
)

foreach ($File in $Files) {
    if (-not (Test-Path -LiteralPath $File)) {
        throw "Required file not found: $File"
    }

    $Content = Get-Content -LiteralPath $File -Raw -Encoding UTF8
    $OldCount = ([regex]::Matches($Content, [regex]::Escape($OldUrl))).Count
    $NewCount = ([regex]::Matches($Content, [regex]::Escape($NewUrl))).Count

    if ($OldCount -eq 1 -and $NewCount -eq 0) {
        $Updated = $Content.Replace($OldUrl, $NewUrl)
        Set-Content -LiteralPath $File -Value $Updated -Encoding UTF8 -NoNewline
    }
    elseif ($OldCount -eq 0 -and $NewCount -eq 1) {
        Write-Host "Already corrected: $File"
    }
    else {
        throw "Unexpected URL state in $File. old=$OldCount new=$NewCount"
    }
}

foreach ($File in $Files) {
    $Content = Get-Content -LiteralPath $File -Raw -Encoding UTF8
    $OldCount = ([regex]::Matches($Content, [regex]::Escape($OldUrl))).Count
    $NewCount = ([regex]::Matches($Content, [regex]::Escape($NewUrl))).Count

    if ($OldCount -ne 0 -or $NewCount -ne 1) {
        throw "Post-correction verification failed for $File. old=$OldCount new=$NewCount"
    }
}

Write-Host 'Guide 00 canonical Red Seal URL correction verified for all three language masters.'
