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
[![](https://badgen.net/badge/icon/Follow%20@jhaledev/1DA1F2?icon=twitter&label)](https://twitter.com/intent/user?screen_name=jhaledev)

Create [Gource animations](https://gource.io/) for an entire organization's repositories!

## Setup
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
   wget https://github.com/acaudwell/Gource/releases/download/gource-0.54/gource-0.54.tar.gz
   tar -xzvf gource-0.54.tar.gz  
   ```
6. Create a GitHub Personal Access Token (classic) with the `repo` scope.


## Usage

### Configuration

Make a copy of the file `config.json.dist` with the name `config.json`.
 - Set the `token` to the token you created in the [setup](#setup).
 - Set the `organization` to the GitHub username of the org whose repos you want
  to animate.
