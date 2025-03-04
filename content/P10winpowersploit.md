Title: Windows环境渗透工具-NiShang、Empire、Powersploit
Date: 2018-06-07 01:05
Modified: 2018-06-07 01:05
Category: 安全
Tags: Windows
Slug: P10
Authors: nJcx
Summary: Windows环境渗透工具-NiShang、Empire、Powersploit~
Status: draft

#### 介绍

由于长期工作在Linux环境下，企业内网也基本是Linux的，对Windows有点生疏，所以决定学习一下Windows的相关渗透技巧~


```bash
https://github.com/samratashok/nishang.git
https://github.com/EmpireProject/Empire.git
https://github.com/PowerShellMafia/PowerSploit.git
```



```bash
── ActiveDirectory
│   ├── Add-ConstrainedDelegationBackdoor.ps1
│   └── Set-DCShadowPermissions.ps1
├── Antak-WebShell
│   ├── antak.aspx
│   └── Readme.md
├── Backdoors
│   ├── Add-ConstrainedDelegationBackdoor.ps1
│   ├── Add-RegBackdoor.ps1
│   ├── Add-ScrnSaveBackdoor.ps1
│   ├── DNS_TXT_Pwnage.ps1
│   ├── Execute-OnTime.ps1
│   ├── Gupt-Backdoor.ps1
│   ├── HTTP-Backdoor.ps1
│   ├── Invoke-ADSBackdoor.ps1
│   ├── Set-RemotePSRemoting.ps1
│   └── Set-RemoteWMI.ps1
├── Bypass
│   └── Invoke-AmsiBypass.ps1
├── CHANGELOG.txt
├── Client
│   ├── Out-CHM.ps1
│   ├── Out-Excel.ps1
│   ├── Out-HTA.ps1
│   ├── Out-Java.ps1
│   ├── Out-JS.ps1
│   ├── Out-SCF.ps1
│   ├── Out-SCT.ps1
│   ├── Out-Shortcut.ps1
│   ├── Out-WebQuery.ps1
│   └── Out-Word.ps1
├── DISCLAIMER.txt
├── Escalation
│   ├── Enable-DuplicateToken.ps1
│   ├── Invoke-PsUACme.ps1
│   └── Remove-Update.ps1
├── Execution
│   ├── Download_Execute.ps1
│   ├── Download-Execute-PS.ps1
│   ├── Execute-Command-MSSQL.ps1
│   ├── Execute-DNSTXT-Code.ps1
│   └── Out-RundllCommand.ps1
├── Gather
│   ├── Check-VM.ps1
│   ├── Copy-VSS.ps1
│   ├── FireBuster.ps1
│   ├── FireListener.ps1
│   ├── Get-Information.ps1
│   ├── Get-LSASecret.ps1
│   ├── Get-PassHashes.ps1
│   ├── Get-PassHints.ps1
│   ├── Get-WebCredentials.ps1
│   ├── Get-WLAN-Keys.ps1
│   ├── Invoke-CredentialsPhish.ps1
│   ├── Invoke-Mimikatz.ps1
│   ├── Invoke-MimikatzWDigestDowngrade.ps1
│   ├── Invoke-Mimikittenz.ps1
│   ├── Invoke-SessionGopher.ps1
│   ├── Invoke-SSIDExfil.ps1
│   ├── Keylogger.ps1
│   └── Show-TargetScreen.ps1
├── LICENSE
├── Misc
│   ├── Nishang_Logo.png
│   ├── Nishang_logo_small.png
│   └── Speak.ps1
├── MITM
│   └── Invoke-Interceptor.ps1
├── nishang.psm1
├── Pivot
│   ├── Create-MultipleSessions.ps1
│   ├── Invoke-NetworkRelay.ps1
│   └── Run-EXEonRemote.ps1
├── powerpreter
│   ├── Powerpreter.psm1
│   └── README.md
├── Prasadhak
│   └── Invoke-Prasadhak.ps1
├── README.md
├── Scan
│   ├── Invoke-BruteForce.ps1
│   └── Invoke-PortScan.ps1
├── Shells
│   ├── Invoke-ConPtyShell.ps1
│   ├── Invoke-JSRatRegsvr.ps1
│   ├── Invoke-JSRatRundll.ps1
│   ├── Invoke-PoshRatHttp.ps1
│   ├── Invoke-PoshRatHttps.ps1
│   ├── Invoke-PowerShellIcmp.ps1
│   ├── Invoke-PowerShellTcpOneLineBind.ps1
│   ├── Invoke-PowerShellTcpOneLine.ps1
│   ├── Invoke-PowerShellTcp.ps1
│   ├── Invoke-PowerShellUdpOneLine.ps1
│   ├── Invoke-PowerShellUdp.ps1
│   ├── Invoke-PowerShellWmi.ps1
│   ├── Invoke-PsGcatAgent.ps1
│   ├── Invoke-PsGcat.ps1
│   └── Remove-PoshRat.ps1
└── Utility
    ├── Add-Exfiltration.ps1
    ├── Add-Persistence.ps1
    ├── Base64ToString.ps1
    ├── ConvertTo-ROT13.ps1
    ├── Do-Exfiltration.ps1
    ├── Download.ps1
    ├── ExetoText.ps1
    ├── Invoke-Decode.ps1
    ├── Invoke-Encode.ps1
    ├── Out-DnsTxt.ps1
    ├── Parse_Keys.ps1
    ├── Remove-Persistence.ps1
    ├── Start-CaptureServer.ps1
    ├── StringToBase64.ps1
    └── TexttoExe.ps1
```




```bash

├── AntivirusBypass
│   ├── AntivirusBypass.psd1
│   ├── AntivirusBypass.psm1
│   ├── Find-AVSignature.ps1
│   └── Usage.md
├── CodeExecution
│   ├── CodeExecution.psd1
│   ├── CodeExecution.psm1
│   ├── Invoke-DllInjection.ps1
│   ├── Invoke-ReflectivePEInjection.ps1
│   ├── Invoke-ReflectivePEInjection_Resources
│   │   ├── DemoDLL
│   │   │   ├── DemoDLL
│   │   │   │   ├── DemoDLL.cpp
│   │   │   │   ├── DemoDLL.h
│   │   │   │   ├── DemoDLL.vcxproj
│   │   │   │   ├── DemoDLL.vcxproj.filters
│   │   │   │   ├── dllmain.cpp
│   │   │   │   ├── ReadMe.txt
│   │   │   │   ├── stdafx.cpp
│   │   │   │   ├── stdafx.h
│   │   │   │   └── targetver.h
│   │   │   └── DemoDLL.sln
│   │   ├── DemoDLL_RemoteProcess
│   │   │   ├── DemoDLL_RemoteProcess
│   │   │   │   ├── DemoDLL_RemoteProcess.cpp
│   │   │   │   ├── DemoDLL_RemoteProcess.vcxproj
│   │   │   │   ├── DemoDLL_RemoteProcess.vcxproj.filters
│   │   │   │   ├── dllmain.cpp
│   │   │   │   ├── ReadMe.txt
│   │   │   │   ├── stdafx.cpp
│   │   │   │   ├── stdafx.h
│   │   │   │   └── targetver.h
│   │   │   └── DemoDLL_RemoteProcess.sln
│   │   ├── DemoExe
│   │   │   ├── DemoExe_MD
│   │   │   │   ├── DemoExe_MD.cpp
│   │   │   │   ├── DemoExe_MD.vcxproj
│   │   │   │   ├── DemoExe_MD.vcxproj.filters
│   │   │   │   ├── ReadMe.txt
│   │   │   │   ├── stdafx.cpp
│   │   │   │   ├── stdafx.h
│   │   │   │   └── targetver.h
│   │   │   ├── DemoExe_MDd
│   │   │   │   ├── DemoExe_MDd.cpp
│   │   │   │   ├── DemoExe_MDd.vcxproj
│   │   │   │   ├── DemoExe_MDd.vcxproj.filters
│   │   │   │   ├── ReadMe.txt
│   │   │   │   ├── stdafx.cpp
│   │   │   │   ├── stdafx.h
│   │   │   │   └── targetver.h
│   │   │   └── DemoExe.sln
│   │   ├── ExeToInjectInTo
│   │   │   ├── ExeToInjectInTo
│   │   │   │   ├── ExeToInjectInTo.cpp
│   │   │   │   ├── ExeToInjectInTo.vcxproj
│   │   │   │   ├── ExeToInjectInTo.vcxproj.filters
│   │   │   │   ├── ReadMe.txt
│   │   │   │   ├── stdafx.cpp
│   │   │   │   ├── stdafx.h
│   │   │   │   └── targetver.h
│   │   │   └── ExeToInjectInTo.sln
│   │   └── Shellcode
│   │       ├── readme.txt
│   │       ├── x64
│   │       │   ├── CallDllMain.asm
│   │       │   ├── ExitThread.asm
│   │       │   ├── GetFuncAddress.asm
│   │       │   └── LoadLibraryA.asm
│   │       └── x86
│   │           ├── CallDllMain.asm
│   │           ├── ExitThread.asm
│   │           └── GetProcAddress.asm
│   ├── Invoke-Shellcode.ps1
│   ├── Invoke-WmiCommand.ps1
│   └── Usage.md
├── Exfiltration
│   ├── Exfiltration.psd1
│   ├── Exfiltration.psm1
│   ├── Get-GPPAutologon.ps1
│   ├── Get-GPPPassword.ps1
│   ├── Get-Keystrokes.ps1
│   ├── Get-MicrophoneAudio.ps1
│   ├── Get-TimedScreenshot.ps1
│   ├── Get-VaultCredential.ps1
│   ├── Get-VaultCredential.ps1xml
│   ├── Invoke-CredentialInjection.ps1
│   ├── Invoke-Mimikatz.ps1
│   ├── Invoke-NinjaCopy.ps1
│   ├── Invoke-TokenManipulation.ps1
│   ├── LogonUser
│   │   └── LogonUser
│   │       ├── logon
│   │       │   ├── dllmain.cpp
│   │       │   ├── logon.cpp
│   │       │   ├── logon.vcxproj
│   │       │   ├── logon.vcxproj.filters
│   │       │   ├── ReadMe.txt
│   │       │   ├── stdafx.cpp
│   │       │   ├── stdafx.h
│   │       │   └── targetver.h
│   │       ├── LogonUser
│   │       │   ├── LogonUser.cpp
│   │       │   ├── LogonUser.vcxproj
│   │       │   ├── LogonUser.vcxproj.filters
│   │       │   ├── ReadMe.txt
│   │       │   ├── stdafx.cpp
│   │       │   ├── stdafx.h
│   │       │   └── targetver.h
│   │       └── LogonUser.sln
│   ├── NTFSParser
│   │   ├── NTFSParser
│   │   │   ├── NTFS_Attribute.h
│   │   │   ├── NTFS_Common.h
│   │   │   ├── NTFS_DataType.h
│   │   │   ├── NTFS_FileRecord.h
│   │   │   ├── NTFS.h
│   │   │   ├── NTFSParser.cpp
│   │   │   ├── NTFSParser.vcxproj
│   │   │   ├── NTFSParser.vcxproj.filters
│   │   │   ├── ReadMe.txt
│   │   │   ├── stdafx.cpp
│   │   │   ├── stdafx.h
│   │   │   └── targetver.h
│   │   ├── NTFSParserDLL
│   │   │   ├── dllmain.cpp
│   │   │   ├── NTFS_Attribute.h
│   │   │   ├── NTFS_Common.h
│   │   │   ├── NTFS_DataType.h
│   │   │   ├── NTFS_FileRecord.h
│   │   │   ├── NTFS.h
│   │   │   ├── NTFSParserDLL.cpp
│   │   │   ├── NTFSParserDLL.vcxproj
│   │   │   ├── NTFSParserDLL.vcxproj.filters
│   │   │   ├── ReadMe.txt
│   │   │   ├── stdafx.cpp
│   │   │   ├── stdafx.h
│   │   │   └── targetver.h
│   │   └── NTFSParser.sln
│   ├── Out-Minidump.ps1
│   ├── Usage.md
│   └── VolumeShadowCopyTools.ps1
├── LICENSE
├── Mayhem
│   ├── Mayhem.psd1
│   ├── Mayhem.psm1
│   └── Usage.md
├── Persistence
│   ├── Persistence.psd1
│   ├── Persistence.psm1
│   └── Usage.md
├── PowerSploit.psd1
├── PowerSploit.psm1
├── PowerSploit.pssproj
├── PowerSploit.sln
├── Privesc
│   ├── Get-System.ps1
│   ├── PowerUp.ps1
│   ├── Privesc.psd1
│   ├── Privesc.psm1
│   └── README.md
├── README.md
├── Recon
│   ├── Dictionaries
│   │   ├── admin.txt
│   │   ├── generic.txt
│   │   └── sharepoint.txt
│   ├── Get-ComputerDetails.ps1
│   ├── Get-HttpStatus.ps1
│   ├── Invoke-Portscan.ps1
│   ├── Invoke-ReverseDnsLookup.ps1
│   ├── PowerView.ps1
│   ├── README.md
│   ├── Recon.psd1
│   └── Recon.psm1
├── ScriptModification
│   ├── Out-CompressedDll.ps1
│   ├── Out-EncodedCommand.ps1
│   ├── Out-EncryptedScript.ps1
│   ├── Remove-Comments.ps1
│   ├── ScriptModification.psd1
│   ├── ScriptModification.psm1
│   └── Usage.md
└── Tests
    ├── CodeExecution.tests.ps1
    ├── Exfiltration.tests.ps1
    ├── PowerSploit.tests.ps1
    ├── Privesc.tests.ps1
    └── Recon.tests.ps1

```
