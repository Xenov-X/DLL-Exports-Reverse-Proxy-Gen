# DLL reverse proxy generator (a.k.a DLL exports forward generator)
##DLL Hijacking
> For when dumping a correctly named DLL in the correct location for execution just isn't going to cut it.

So you've found an application with an insecure search path, but the DLL that you can hijack is critical for functionality. What if your DLL could forward the applications requests to the legitimate target DLL maintaining all functionality AND run your code? 

The technique of linking DLLs with "#pragma comment" is nothing new, but while experimenting, I found there wasn't a tool which would generate the list of export functions quickly and easily. i forked a tool from 2007, which looked like it used to work, and have updated it to work with the latest dumpbin.exe included in visual studio. 

This tool will identify all exported functions within the target DLL, and generate a correctly formed header file to be used in your custom DLL. Included in the repository is a sample .cpp file for a very simple calc.exe PoC DLL. 

## How to use the tool?
- Have dumpbin.exe in PATH. 
*This is a
  *s


## License

This tool is released under a 3-clause BSD License, in addition to the requirements of the original creators CPOL licencing detailed below.
Some minor improvements have been made by [KPMG LLP] (http://www.kpmg.co.uk/cyber) for functionality.

## Credits
The original source project was produced by Kontza in 2007, released under "The Code Project Open License (CPOL) 1.02"

Additional KPMG updates developed by Aaron Dobie.