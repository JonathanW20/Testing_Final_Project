
<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="4-bit multiplier.jpg" alt="Logo">
  </a>

<h3 align="center">Formal Verification of Integer Multiplier Circuits</h3>
</div>


<!-- ABOUT THE PROJECT -->
## About The Project
This project aims to test and verify the efficiency of integer multiplier circuits through a comprehensive approach involving Formal Verification, Singular, the ABC synthesis tool, and Ideal Membership Testing. We aim to validate the functionality and adherence to ideal standards for 2-bit, 3-bit, 16-bit, and 32-bit multipliers, ensuring their reliability across various bit-widths.

<!-- ARCHIVE -->
## Archive
This GitHub repository includes the information and files required to test and verify a 2-bit, 3, bit, 16-bit, and 32-bit multipliers. The report describes our approach and process to test the circuits.
Additionally, it provides the process of the ideal membership test using Gröbner Basis and RTTO (Reverse Topological Term Order). It also includes the Python pseudocode to convert blif files to Singualr files. The steps to download and run the scripting tools are provided below. 

<!-- Scripts-->
## Running Scripts

### ABC Tool
The ABC tool can be found on Alan's [website](https://people.eecs.berkeley.edu/~alanmi/abc/). To generate a N bit circuit in the ABC synthesis tool(lib2.gen lib located 
[here](https://my.ece.utah.edu/~kalla/ECE6745/DEMO/lib2.genlib)): 
<!--*-->
1. Locate the directory of ABC. 
   ```sh
   cd directory_of_ABC
   ```
2. Run the executable file. 
   ```sh
   ./abc
   ```
3. Generate the .blif file. 
   ```sh
   gen -N N -m NBitMult.blif
   ```
4. strash
   ```sh
   strash
   ```
5. ifraig
   ```sh
   ifraig
   ```
6. resyn2
   ```sh
   resyn2
7. dch
   ```sh
   dch
   ```
8. Read the genlib library. 
   ```sh
   read lib2.genlib
   ```
8. Map 
   ```sh
   Map
   ```
9. Read the genlib library. 
   ```sh
   read lib2.genlib
   ```
10. Write the final .blif file
   ```sh
     write_blif MappedNBitMult.blif
   ```

### Python Script
1. Locate the directory of the python script. 
   ```sh
   cd directory_of_script
   ```
2. Run the Script

   ```sh
   python blifToSing.py
   ```
3. .sing file will be in the same directory as the Python Script. 

### Singular
Singular can be downloaded from this [website](https://www.singular.uni-kl.de/) then follow these steps: 
1. In the terminal type: 
   ```sh
   Singular
   ```
2. STUFF
