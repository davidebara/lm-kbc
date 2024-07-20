# LM-KBC Challenge Solution

## Overview

This repository contains the solution to the LM-KBC challenge posed in the [dataset2024 GitHub repository](https://github.com/lm-kbc/dataset2024).

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/davidebara/lm-kbc.git
    cd lm-kbc
    ```

2. Create a virtual environment and install the required dependencies:
    ```bash
    conda create -n lm-kbc-2024 python=3.12.1
    ```

    ```bash
    conda activate lm-kbc-2024
    pip install -r requirements.txt
    ```

3. Run the main script:
    ```bash
    from huggingface_hub import login
    login(token="INSERT_TOKEN_HERE")

    python baseline.py -c configs/baseline-llama-3-8b-instruct.yaml -i data/test.jsonl
    ```
4. Format the predictions:
    ```bash
    python pred_script.py
    ```