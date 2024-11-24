#!/bin/bash

# Check if Python exists and get version
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi
source venv/bin/activate

echo "Installing huggingface-hub..."
pip install 'huggingface_hub[cli,torch]'

# Run huggingface-cli login
echo "Please log in to Hugging Face."
echo "You can create an access token with read permissions at: https://huggingface.co/settings/tokens"
huggingface-cli login

python3 install.py
pip install --upgrade gradio

echo "Installation completed successfully!"
echo "To run the Gradio demo, use one of the following commands:"
echo "On most systems:"
echo "python gradio_app.py"
echo "On Mac with MPS issues, either use:"
echo "PYTORCH_ENABLE_MPS_FALLBACK=1 python gradio_app.py"
echo "(Uses MPS with CPU fallback)"
echo "Or:"
echo "SF3D_USE_CPU=1 python gradio_app.py"
echo "(Uses CPU only)"
echo "Make sure to activate the virtual environment before running the demo:"
echo "source venv/bin/activate"
