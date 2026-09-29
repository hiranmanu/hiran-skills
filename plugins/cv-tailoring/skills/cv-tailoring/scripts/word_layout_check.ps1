<#
.SYNOPSIS
  word_layout_check.ps1 - step 07 layout check for the cv-tailoring skill.

.DESCRIPTION
  Opens the DOCX read-only in real Word (via COM) and measures what
  validate_cv.py cannot: page count, where each role sits, and how every
  paragraph actually wraps (line count and how full its last line is).
  Real Word is the only render 05-formatting.md treats as authoritative
  (LibreOffice substitutes Carlito for Calibri and wraps differently).
  Nothing is saved and no PDF is written.

  Requires Windows and Microsoft Word. Exit codes: 0 pass, 1 fail,
  2 Word unavailable (not a verdict).

  Rules enforced (05-formatting.md):
    - Pages <= MaxPages; at least MinPage1Roles roles fully on page 1; no role
      split across pages; no section heading stranded at a page bottom.
    - Page-1 role bullets: 1 or 2 lines. A 2-line bullet's second line must be
      at least MinLastLine full (default 40%). A fuller second line is fine.
    - Page-2 role bullets, Earlier Career and Qualifications lines: 1 line.
    - Skills rows: 1 or 2 lines; a 2-line row's second line at least MinLastLine
      full. A 1-line row is a warning (under-filled).
    - Profile paragraphs: last line at least MinProfileLast full (no 1-2 word
      orphan); total profile lines <= 7 (warning).

.EXAMPLE
  powershell -File word_layout_check.ps1 "C:\path\Hiran_CV_2026.09.29_Softcat_PMDir.docx"
#>
param(
    [Parameter(Mandatory = $true)][string]$Path,
    [int]$MaxPages = 2,
    [int]$MinPage1Roles = 3,
    [double]$MinLastLine = 0.40,
    [double]$MinProfileLast = 0.30
)

$ErrorActionPreference = "Stop"
$full = (Resolve-Path -LiteralPath $Path).Path
$H = @{
    profile = "Profile Summary"
    skills  = "Key Skills & Competencies"
    career  = "Career & Key Achievements to Date"
    quals   = "Qualifications, Certifications & Personal Details"
}
$headingSet = @($H.Values)

$word = $null
$doc = $null
$failures = New-Object System.Collections.Generic.List[string]
$warnings = New-Object System.Collections.Generic.List[string]
$rows = New-Object System.Collections.Generic.List[object]

try {
    try {
        $word = New-Object -ComObject Word.Application
    }
    catch {
        Write-Output "SKIP  Microsoft Word is not available via COM on this machine. Open the DOCX and check page count, roles on page 1, role splits and bullet wraps by eye."
        $global:LASTEXITCODE = 2
        exit 2
    }
    $word.Visible = $false
    $doc = $word.Documents.Open($full, $false, $true)   # ConfirmConversions=false, ReadOnly=true
    $pages = $doc.ComputeStatistics(2)                  # wdStatisticPages
    $ps = $doc.Sections.Item(1).PageSetup
    $pageW = [double]$ps.PageWidth
    $marginL = [double]$ps.LeftMargin
    $rightEdge = $pageW - [double]$ps.RightMargin

    # ---- measure every paragraph
    $paras = @()
    foreach ($p in $doc.Paragraphs) {
        $r = $p.Range
        $text = $r.Text.TrimEnd([char]13, [char]7, [char]10)
        $lines = [int]$r.ComputeStatistics(1)                              # wdStatisticLines
        $endPos = $doc.Range($r.End - 1, $r.End - 1)
        $endX = [double]$endPos.Information(5)                             # wdHorizontalPositionRelativeToPage
        $leftX = $marginL + [double]$p.Format.LeftIndent
        $width = $rightEdge - $leftX
        $fill = if ($width -gt 0) { [Math]::Max(0.0, [Math]::Min(1.0, ($endX - $leftX) / $width)) } else { 0.0 }
        $paras += [pscustomobject]@{
            Text      = $text
            StartPage = [int]$r.Characters.First.Information(3)            # wdActiveEndPageNumber
            EndPage   = [int]$r.Information(3)
            Lines     = $lines
            LastFill  = $fill
            Bullet    = ($p.Range.ListFormat.ListType -ne 0)
        }
    }

    # ---- walk: sections, roles, and per-paragraph rules
    $section = $null
    $roles = @()
    $current = $null
    $stranded = @()
    $profileLines = 0
    for ($i = 0; $i -lt $paras.Count; $i++) {
        $p = $paras[$i]
        $t = $p.Text.Trim()

        if ($headingSet -contains $t) {
            if ($current) { $roles += $current; $current = $null }
            $section = ($H.GetEnumerator() | Where-Object { $_.Value -eq $t } | Select-Object -First 1).Key
            if (($i + 1) -lt $paras.Count -and $paras[$i + 1].StartPage -ne $p.EndPage) { $stranded += $t }
            continue
        }

        $isRole = ($section -eq "career") -and ($p.Text -match "`t") -and ($p.Text -match "\b(19|20)\d{2}\b")
        if ($isRole) {
            if ($current) { $roles += $current }
            $current = [pscustomobject]@{ Title = ($p.Text -split "`t")[0].Trim(); Start = $p.StartPage; End = $p.EndPage }
            continue
        }
        if ($current -and $t) { if ($p.EndPage -gt $current.End) { $current.End = $p.EndPage } }
        if (-not $t) { continue }

        $short = if ($t.Length -gt 58) { $t.Substring(0, 58) + "..." } else { $t }
        $pct = [int][Math]::Round($p.LastFill * 100)

        switch ($section) {
            "profile" {
                $profileLines += $p.Lines
                if ($p.Lines -ge 2 -and $p.LastFill -lt $MinProfileLast) {
                    $failures.Add("profile paragraph ends with a short last line ($pct% full, want >= $([int]($MinProfileLast*100))%): $short")
                }
                $rows.Add([pscustomobject]@{ Where = "profile"; Lines = $p.Lines; LastLine = "$pct%"; Text = $short })
            }
            "skills" {
                if ($p.Lines -gt 2) { $failures.Add("skills row wraps to $($p.Lines) lines: $short") }
                elseif ($p.Lines -eq 2 -and $p.LastFill -lt $MinLastLine) { $failures.Add("skills row second line only $pct% full (want >= $([int]($MinLastLine*100))%): $short") }
                elseif ($p.Lines -eq 1) { $warnings.Add("skills row is a single line (under-filled): $short") }
                $rows.Add([pscustomobject]@{ Where = "skills"; Lines = $p.Lines; LastLine = "$pct%"; Text = $short })
            }
            "career" {
                if (-not $p.Bullet) { continue }
                $onPage1 = ($current -and $current.Start -eq 1)
                if ($onPage1) {
                    if ($p.Lines -gt 2) { $failures.Add("page-1 bullet wraps to $($p.Lines) lines: $short") }
                    elseif ($p.Lines -eq 2 -and $p.LastFill -lt $MinLastLine) { $failures.Add("page-1 bullet second line only $pct% full (want >= $([int]($MinLastLine*100))%): $short") }
                    $rows.Add([pscustomobject]@{ Where = "p1 bullet"; Lines = $p.Lines; LastLine = "$pct%"; Text = $short })
                }
                else {
                    if ($p.Lines -gt 1) { $failures.Add("page-2 bullet wraps ($($p.Lines) lines, must be 1): $short") }
                    $rows.Add([pscustomobject]@{ Where = "p2 bullet"; Lines = $p.Lines; LastLine = "$pct%"; Text = $short })
                }
            }
            "quals" {
                if ($p.Bullet -and $p.Lines -gt 1) { $failures.Add("Qualifications line wraps ($($p.Lines) lines, must be 1): $short") }
            }
        }
    }
    if ($current) { $roles += $current }
    if ($profileLines -gt 7) { $warnings.Add("profile is $profileLines lines (aim for 7 or fewer)") }

    $split = @($roles | Where-Object { $_.Start -ne $_.End })
    $onPage1Roles = @($roles | Where-Object { $_.Start -eq 1 -and $_.End -eq 1 })

    # ---- report
    Write-Output ""
    Write-Output ("word_layout_check.ps1 - " + [IO.Path]::GetFileName($full))
    Write-Output ("=" * 64)
    Write-Output ("Pages: {0} (cap {1})" -f $pages, $MaxPages)
    Write-Output "Roles:"
    foreach ($r in $roles) {
        $where = if ($r.Start -eq $r.End) { "page $($r.Start)" } else { "SPLIT pages $($r.Start)-$($r.End)" }
        Write-Output ("  {0,-12} {1}" -f $where, $r.Title)
    }
    Write-Output ""
    Write-Output "Measured wraps (lines / how full the last line is):"
    foreach ($x in $rows) {
        Write-Output ("  {0,-9} {1} line{2}  last line {3,4}   {4}" -f $x.Where, $x.Lines, $(if ($x.Lines -eq 1) { " " } else { "s" }), $x.LastLine, $x.Text)
    }
    Write-Output ""

    if ($pages -gt $MaxPages) { $failures.Add("page count $pages exceeds cap $MaxPages") }
    if ($split.Count -gt 0) { $failures.Add("role(s) split across a page break: " + (($split | ForEach-Object { $_.Title }) -join "; ")) }
    if ($stranded.Count -gt 0) { $failures.Add("heading stranded at the bottom of a page: " + ($stranded -join "; ")) }
    if ($onPage1Roles.Count -lt $MinPage1Roles) { $failures.Add("only $($onPage1Roles.Count) role(s) fully on page 1 (want $MinPage1Roles+)") }

    if ($failures.Count -eq 0) { Write-Output ("PASS  {0} pages, {1} roles on page 1, no split roles, every wrap within rule" -f $pages, $onPage1Roles.Count) }
    foreach ($f in $failures) { Write-Output "FAIL  $f" }
    foreach ($w in $warnings) { Write-Output "WARN  $w" }
    Write-Output ("=" * 64)
    Write-Output ("OVERALL: " + $(if ($failures.Count -gt 0) { "FAIL" } else { "PASS" }))
    $global:LASTEXITCODE = $(if ($failures.Count -gt 0) { 1 } else { 0 })
}
finally {
    if ($doc) { $doc.Close($false); [void][Runtime.InteropServices.Marshal]::ReleaseComObject($doc) }
    if ($word) { $word.Quit(); [void][Runtime.InteropServices.Marshal]::ReleaseComObject($word) }
    [GC]::Collect(); [GC]::WaitForPendingFinalizers()
}
exit $global:LASTEXITCODE
