# Installation Guide

## Automatic Install

```bash
bash install.sh
```

## Manual Install

### 1. Clone the repository

```bash
git clone https://github.com/stability-ai/stable-fast-3d.git
```

### 2. Install dependencies

First, install PyTorch and torchvision according to your platform:

https://pytorch.org/get-started/locally/

Then, install the remaining requirements with:

```bash
pip install -U setuptools
pip install wheel
pip install -r requirements.txt
pip install -r requirements-demo.txt
```

### 3. Access the model from HuggingFace

1. Log in to Hugging Face and request access [here](https://huggingface.co/stabilityai/stable-fast-3d).
2. Create an access token with read permissions [here](https://huggingface.co/settings/tokens).
3. Run `huggingface-cli login` in the environment and enter the token.

4. Run Gradio Demo

```bash
python gradio_app.py
```

## Common Issues in Mac

### `ModuleNotFoundError: No module named '_lzma'``

This is due to an issue with `pyenv` in Mac. You can fix it by:

```bash
brew install xz
pyenv uninstall <your python version>
pyenv install <your python version>
```

### `pydantic.errors.PydanticSchemaGenerationError`

This is due to older version of gradio. You can fix it by:

```bash
pip install --upgrade gradio
```

### `NotImplementedError: The operator 'aten::_upsample_bilinear2d_aa.out' is not currently implemented for the MPS device`

This is due to an issue with PyTorch and MPS. You can fix it by

Using either of the two commands when running the Gradio Demo:

```bash
PYTORCH_ENABLE_MPS_FALLBACK=1 python gradio_app.py
```
(This uses MPS with a fallback to CPU)
or
```bash
SF3D_USE_CPU=1 python gradio_app.py
```
(This uses CPU)