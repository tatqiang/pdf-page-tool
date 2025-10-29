# MS Word Page Number Auto-Fix Feature

## ⚠️ FEATURE REMOVED

**NOTE:** The MS Word page number auto-detection feature has been removed from this tool.

## Current Functionality

This tool now only:

1. **Replaces page number tags** - Converts {{p-x}}, {{pg-xofy}}, etc. to actual numbers
2. **Fixes Table of Contents** - Updates TOC page numbers using PDF links
3. **Adds page numbers** - Optionally adds page numbers to pages without tags

## Alternative Approach

If you need to fix MS Word-generated page numbers, you can:

1. **Use page number tags instead** - Add {{p-x}}, {{pg-x}}, etc. tags to your document before converting to PDF
2. **Manual replacement** - Use the tool's option to add page numbers to all pages without placeholders

## Supported Tag Formats

| Syntax       | Display    |
|-------------|-----------|
| {{p-x}}     | x         |
| {{p-x/y}}   | x / y     |
| {{p-xofy}}  | x of y    |
| {{pg-x}}    | Page x    |
| {{pg-x/y}}  | Page x/y  |
| {{pg-xofy}} | Page x of y |

Use these tags in your document headers/footers before converting to PDF for automatic page number replacement.
