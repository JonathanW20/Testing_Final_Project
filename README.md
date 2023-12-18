
<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="4-bit multiplier.jpg" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Formal Verification of Integer Multiplier Circuits</h3>
</div>


<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

Here's a blank template to get started: To avoid retyping too much info. Do a search and replace with your text editor for the following: `github_username`, `repo_name`, `twitter_handle`, `linkedin_username`, `email_client`, `email`, `project_title`, `project_description`

<!-- Scripts-->
## Running Scripts

### ABC Tool
To generate a N bit circuit in the ABC synthesis tool(lib2.gen lib located [here](https://my.ece.utah.edu/~kalla/ECE6745/DEMO/lib2.genlib)): 
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
4. Strash
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
1. In any folder type in: 
   ```sh
   Singular
   ```
2. STUFF


<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_


<!-- ROADMAP -->
## Roadmap
- [ ] Feature 1
- [ ] Feature 2
- [ ] Feature 3

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
