# PowerShell Commands Cheat Sheet

## **File and Folder Operations**
### **Navigating the File System**
- `Get-Location` (`pwd`): Display the current directory.
- `Set-Location` (`cd`): Change the current directory.
  ```powershell
  Set-Location C:\Users\YourName
  ```
- `Get-ChildItem` (`ls`, `dir`): List files and directories.
  ```powershell
  Get-ChildItem -Path C:\Users -Recurse
  ```

### **File and Folder Management**
- `New-Item`: Create a new file or folder.
  ```powershell
  New-Item -Path "C:\Temp\newfile.txt" -ItemType File
  ```
- `Remove-Item` (`rm`, `del`): Delete a file or folder.
  ```powershell
  Remove-Item -Path "C:\Temp\newfile.txt"
  ```
- `Copy-Item` (`cp`): Copy files or folders.
  ```powershell
  Copy-Item -Path "C:\Source\file.txt" -Destination "C:\Destination"
  ```
- `Move-Item` (`mv`): Move or rename files or folders.
  ```powershell
  Move-Item -Path "C:\Temp\file.txt" -Destination "C:\NewFolder\file.txt"
  ```

---

## **Viewing and Editing File Content**
- `Get-Content` (`cat`, `type`): Read file content.
  ```powershell
  Get-Content -Path "C:\Temp\file.txt"
  ```
- `Set-Content`: Overwrite file content.
  ```powershell
  Set-Content -Path "C:\Temp\file.txt" -Value "Hello, World!"
  ```
- `Add-Content`: Append content to a file.
  ```powershell
  Add-Content -Path "C:\Temp\file.txt" -Value "Additional line."
  ```
- `Out-File`: Redirect command output to a file.
  ```powershell
  Get-Process | Out-File -FilePath "C:\Temp\processes.txt"
  ```

---

## **Process and System Management**
- `Get-Process` (`ps`): List running processes.
  ```powershell
  Get-Process | Sort-Object -Property CPU -Descending
  ```
- `Stop-Process`: Stop a process by name or ID.
  ```powershell
  Stop-Process -Name "notepad"
  ```
- `Start-Process`: Start a new process.
  ```powershell
  Start-Process "notepad.exe"
  ```
- `Get-Service`: List services on the system.
  ```powershell
  Get-Service | Where-Object {$_.Status -eq "Running"}
  ```
- `Stop-Service`: Stop a service.
  ```powershell
  Stop-Service -Name "Spooler"
  ```
- `Start-Service`: Start a stopped service.
  ```powershell
  Start-Service -Name "Spooler"
  ```

---

## **System Information**
- `Get-Host`: Display information about the PowerShell environment.
- `Get-History`: Show command history for the session.
- `Clear-Host` (`cls`): Clear the console screen.
- `Get-EventLog`: Retrieve event logs.
  ```powershell
  Get-EventLog -LogName Application -Newest 10
  ```
- `Get-ComputerInfo`: Display detailed system information.

---

## **Variables and Objects**
- `$variableName`: Create a variable.
  ```powershell
  $name = "PowerShell"
  ```
- `Get-Variable`: List all variables.
- `Remove-Variable`: Remove a variable.
  ```powershell
  Remove-Variable -Name "name"
  ```
- `Select-Object`: Select properties of objects.
  ```powershell
  Get-Process | Select-Object -Property Name, CPU
  ```
- `Sort-Object`: Sort objects by property.
  ```powershell
  Get-Process | Sort-Object -Property CPU -Descending
  ```

---

## **Loops and Conditions**
### **For Loop**
```powershell
for ($i = 0; $i -lt 5; $i++) {
    Write-Output "Iteration $i"
}
```

### **While Loop**
```powershell
$i = 0
while ($i -lt 5) {
    Write-Output "Iteration $i"
    $i++
}
```

### **If Statement**
```powershell
if ($a -gt $b) {
    Write-Output "$a is greater than $b"
} elseif ($a -eq $b) {
    Write-Output "$a is equal to $b"
} else {
    Write-Output "$a is less than $b"
}
```

### **ForEach Loop**
```powershell
$items = 1..5
foreach ($item in $items) {
    Write-Output "Item: $item"
}
```

---

## **User Management**
- `Get-LocalUser`: List local user accounts.
  ```powershell
  Get-LocalUser
  ```
- `New-LocalUser`: Create a new local user.
  ```powershell
  New-LocalUser -Name "JohnDoe" -Password (Read-Host -AsSecureString "Enter Password") -FullName "John Doe"
  ```
- `Remove-LocalUser`: Remove a local user account.
  ```powershell
  Remove-LocalUser -Name "JohnDoe"
  ```
- `Set-LocalUser`: Modify a local user.
  ```powershell
  Set-LocalUser -Name "JohnDoe" -PasswordNeverExpires $true
  ```

---

## **Networking**
- `Test-Connection` (`ping`): Test network connectivity.
  ```powershell
  Test-Connection -ComputerName google.com -Count 4
  ```
- `Get-NetIPAddress`: Retrieve IP addresses.
  ```powershell
  Get-NetIPAddress
  ```
- `Get-NetAdapter`: Display network adapter details.
  ```powershell
  Get-NetAdapter
  ```
- `Get-DnsClient`: Display DNS client information.
  ```powershell
  Get-DnsClient
  ```
- `Resolve-DnsName`: Perform DNS lookups.
  ```powershell
  Resolve-DnsName -Name google.com
  ```

---

## **Scripts and Automation**
- **Run a Script**:
  ```powershell
  .\script.ps1
  ```
- **Set Execution Policy**:
  ```powershell
  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
  ```
- **Parameters in Scripts**:
  ```powershell
  param (
      [string]$Name,
      [int]$Age
  )
  Write-Output "Name: $Name, Age: $Age"
  ```

---

## **Other Useful Commands**
- `Measure-Object`: Measure properties of objects (e.g., count, sum).
  ```powershell
  Get-ChildItem | Measure-Object
  ```
- `Export-Csv`: Export data to a CSV file.
  ```powershell
  Get-Process | Select-Object Name, CPU | Export-Csv -Path "C:\Temp\processes.csv" -NoTypeInformation
  ```
- `Import-Csv`: Import data from a CSV file.
  ```powershell
  $data = Import-Csv -Path "C:\Temp\processes.csv"
  ```
- `Write-Output`: Print text to the console.
  ```powershell
  Write-Output "Hello, PowerShell!"
  ```
- `Write-Host`: Print text with formatting.
  ```powershell
  Write-Host "Hello, World!" -ForegroundColor Green
  ```

