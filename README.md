<!--
 Copyright (c) 2023 Joseph Hale
 
 This Source Code Form is subject to the terms of the Mozilla Public
 License, v. 2.0. If a copy of the MPL was not distributed with this
 file, You can obtain one at http://mozilla.org/MPL/2.0/.
-->

# Gource Org

<!-- BADGES -->
[![](https://badgen.net/github/license/thehale/github-issue-import)](https://github.com/thehale/github-issue-import/blob/master/LICENSE)
[![](https://badgen.net/badge/icon/Sponsor/pink?icon=github&label)](https://github.com/sponsors/thehale)
[![](https://img.shields.io/badge/LinkedIn-thehale-0A66C2?logo=linkedin)](https://linkedin.com/in/thehale)

Create [Gource animations](https://gource.io/) for an entire organization's repositories!

<details>
    <summary>Installation</summary>

1. Install Python 3.8 or later
2. Create a virtual environment
    ```bash
    python -m venv .venv
    ```
3. [Activate the virtual environment](https://docs.python.org/3/library/venv.html#how-venvs-work)
    ```
    # bash
    source .venv/bin/activate
    # Windows (Powershell)
    .venv/Scripts/Activate.ps1
    # Windows (cmd)
    .venv/Scripts/activate.bat
    ```
4. Install dependencies
    ```
    pip install -r requirements.txt
    ```
5. Install `gource`
   ```
   # Ubuntu 20.04
   sudo apt install gource 
   ```
6. Install `ffmpeg`
   ```
   # Ubuntu 20.04
   sudo apt install ffmpeg
   ```
7. Create a GitHub Personal Access Token (classic) with the `repo` scope.

</details>


## Usage

### Configuration

Make a copy of the file `config.json.dist` with the name `config.json`.
 - Set the `token` to the token you created in the [setup](#setup).
 - Set the `organization` to the GitHub username of the org whose repos you want
  to animate.

#### Authors

After running the script once, you can run the following command to list all 
the authors found across all repositories.

```bash
cat gource.log | cut -d '|' -f 2 | sort | uniq 
```

Place these names in the config to deduplicate/rename authors


### Creating the Animation
Run the script
```
python gource_org.py
```

## License

This project is licensed under the [Mozilla Public License v2.0](./LICENSE)

Note, however, that it requires `gource` and `ffmpeg` to be installed on your
system. Since `gource` is licensed under GPL-3.0, the combined work may need to
be used under the terms of the GPL-3.0 (consult a lawyer for your specific
case).
