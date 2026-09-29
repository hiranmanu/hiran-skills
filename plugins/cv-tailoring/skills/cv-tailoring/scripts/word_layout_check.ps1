<#
.SYNOPSIS
  word_layout_check.ps1 - step 07 pagination check for the cv-tailoring skill.

.DESCRIPTION
  Opens the DOCX read-only in real Word (via COM) and reports what
  validate_cv.py cannot: page count, which roles sit on which page, roles split
  across a page break, and section headings stranded at the bottom of a page.
  Real Word is the only render 05-formatting.md treats as authoritative for
  pagination (LibreOffice substitutes Carlito for Calibri and paginates
  differently). Nothing is saved and no PDF is written.

  Requires Windows and Microsoft Word. Without Word, open the DOCX and check
  by eye.

  Exit codes: 0 pass, 1 fail, 2 Word unavailable (not a verdict).

  FAIL when: pages > MaxPages, any role is split across pages, any section
  heading is stranded, or fewer than MinPage1Roles roles sit fully on page 1.

.EXAMPLE
  powershell -File word_layout_check.ps1 "C:\path\Hiran_CV_2026.09.29_Softcat_PMDir.docx"
#>
param(
    [Parameter(Mandatory = $true)][string]$Path,
    [int]$MaxPages = 2,
    [int]$MinPage1Roles = 3
)

$ErrorActionPreference = "Stop"
$full = (Resolve-Path -LiteralPath $Path).Path
$headings = @("Profile Summary", "Key Skills & Competencies", "Career & Key Achievements to Date", "Qualifications, Certifications & Personal Details")

$word = $null
$doc = $null
try {
    try {
        $word = New-Object -ComObject Word.Application
    }
    catch {
        Write-Output "SKIP  Microsoft Word is not available via COM on this machine. Open the DOCX and check page count, roles on page 1 and role splits by eye."
        $global:LASTEXITCODE = 2
        exit 2
    }
    $word.Visible = $false
    $doc = $word.Documents.Open($full, $false, $true)   # ConfirmConversions=false, ReadOnly=true
    $pages = $doc.ComputeStatistics(2)                  # wdStatisticPages

    $paras = @()
    foreach ($p in $doc.Paragraphs) {
        $text = $p.Range.Text.TrimEnd([char]13, [char]7, [char]10)
        $paras += [pscustomobject]@{
            Text      = $text
            StartPage = [int]$p.Range.Characters.First.Information(3)   # wdActiveEndPageNumber
            EndPage   = [int]$p.Range.Information(3)
        }
    }

    $roles = @()
    $current = $null
    $stranded = @()
    for ($i = 0; $i -lt $paras.Count; $i++) {
        $p = $paras[$i]
        $isHeading = $headings -contains $p.Text.Trim()
        $isRole = ($p.Text -match "`t") -and ($p.Text -match "\b(19|20)\d{2}\b")

        if ($isHeading) {
            if ($current) { $roles += $current; $current = $null }
            if (($i + 1) -lt $paras.Count -and $paras[$i + 1].StartPage -ne $p.EndPage) {
                $stranded += $p.Text.Trim()
            }
            continue
        }
        if ($isRole) {
            if ($current) { $roles += $current }
            $title = ($p.Text -split "`t")[0].Trim()
            $current = [pscustomobject]@{ Title = $title; Start = $p.StartPage; End = $p.EndPage }
            continue
        }
        if ($current -and $p.Text.Trim()) {
            if ($p.EndPage -gt $current.End) { $current.End = $p.EndPage }
        }
    }
    if ($current) { $roles += $current }

    $split = @($roles | Where-Object { $_.Start -ne $_.End })
    $onPage1 = @($roles | Where-Object { $_.Start -eq 1 -and $_.End -eq 1 })

    Write-Output ""
    Write-Output ("word_layout_check.ps1 - " + [IO.Path]::GetFileName($full))
    Write-Output ("=" * 60)
    Write-Output ("Pages: {0} (cap {1})" -f $pages, $MaxPages)
    Write-Output "Roles:"
    foreach ($r in $roles) {
        $where = if ($r.Start -eq $r.End) { "page $($r.Start)" } else { "SPLIT pages $($r.Start)-$($r.End)" }
        Write-Output ("  {0,-12} {1}" -f $where, $r.Title)
    }
    Write-Output ""

    $fail = $false
    if ($pages -gt $MaxPages) { Write-Output "FAIL  page count $pages exceeds cap $MaxPages"; $fail = $true }
    else { Write-Output "PASS  page count within cap" }

    if ($split.Count -gt 0) { Write-Output ("FAIL  role(s) split across a page break: " + (($split | ForEach-Object { $_.Title }) -join "; ")); $fail = $true }
    else { Write-Output "PASS  no role split across a page break" }

    if ($stranded.Count -gt 0) { Write-Output ("FAIL  heading stranded at the bottom of a page: " + ($stranded -join "; ")); $fail = $true }
    else { Write-Output "PASS  no stranded section heading" }

    if ($onPage1.Count -lt $MinPage1Roles) { Write-Output ("FAIL  only {0} role(s) fully on page 1 (want {1}+)" -f $onPage1.Count, $MinPage1Roles); $fail = $true }
    else { Write-Output ("PASS  {0} roles fully on page 1" -f $onPage1.Count) }

    Write-Output ("=" * 60)
    Write-Output ("OVERALL: " + $(if ($fail) { "FAIL" } else { "PASS" }))
    if ($fail) { $global:LASTEXITCODE = 1 } else { $global:LASTEXITCODE = 0 }
}
finally {
    if ($doc) { $doc.Close($false); [void][Runtime.InteropServices.Marshal]::ReleaseComObject($doc) }
    if ($word) { $word.Quit(); [void][Runtime.InteropServices.Marshal]::ReleaseComObject($word) }
    [GC]::Collect(); [GC]::WaitForPendingFinalizers()
}
exit $global:LASTEXITCODE
