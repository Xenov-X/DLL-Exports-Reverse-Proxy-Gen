# DLL reverse proxy generator (a.k.a DLL exports forward generator)
## DLL Hijacking
> When dumping a correctly named DLL in the correct location for execution, just don't cut it.

So you've found an application with an insecure search path, but the DLL you can hijack is critical for functionality. What if your DLL could forward the application requests to the legitimate target DLL, maintaining all functionality AND run your code? 

Linking DLLs with "#pragma comment" is nothing new. Still, while experimenting, I found no tool that would generate a formatted list of exported functions quickly and easily. I forked a tool from 2007 that looked like it used to work, updated it to work with the latest dumpbin.exe included in Visual Studio, and ensured that it handles escaping backslashes correctly in the output header file. 

This tool will identify all exported functions within the target DLL and generate a correctly formed header file for your custom DLL. The repository includes a sample .cpp file for a very simple calc.exe PoC DLL. 

## How to use the tool?
### Requirements
* Python 3
* Have dumpbin.exe in PATH. 
  * This is a component of Visual Studio, and due to licensing restrictions, it cannot be packaged with this tool. Default location is: "C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.25.28610\bin\Hostx64\x64\dumpbin.exe"


### Usage
```
usage: DLL_Rev_Proxy_Gen.py [-h] [-o DIR] dll_names [dll_names ...]

DLL Reverse Proxy Generator

positional arguments:
  dll_names             DLL(s) to process.

options:
  -h, --help            show this help message and exit
  -o DIR, --output-dir DIR
                        Specify output directory.
```

#### Example
> Python DLL_Rev_Proxy_Gen.py "C:\Windows\System32\ncrypt.dll"  

> Output to: ./ncrypt_fwd.h


## License

This tool is released under a 3-clause BSD License, in addition to the requirements of the original creators' CPOL licensing detailed below.
[KPMG LLP](http://www.kpmg.co.uk/cyber) has made some minor improvements to functionality.

## Credits
The original source project was produced by Kontza in 2007, released under "The Code Project Open License (CPOL) 1.02"

Additional KPMG updates developed by Aaron Dobie.
