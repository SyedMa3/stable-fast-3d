#!/usr/bin/env python3
import os
import sys
import subprocess
import platform
from pathlib import Path
from huggingface_hub import hf_hub_download

class SF3DInstaller:
    def __init__(self):
        self.root_dir = Path.cwd()
        self.venv_dir = self.root_dir / "venv"
        self.requirements_file = self.root_dir / "requirements.txt"
        self.requirements_demo_file = self.root_dir / "requirements-demo.txt"
        self.config = {
            "venv_path": str(self.venv_dir),
            "install_date": None,
            "python_version": platform.python_version(),
            "platform": platform.system()
        }

    def check_python_version(self):
        """Check if Python version is compatible (3.8+)"""
        if sys.version_info < (3, 8):
            raise SystemError("Python 3.8 or higher is required")

    def activate_virtual_environment(self):
        """Activate the virtual environment"""
        if platform.system() == "Windows":
            activate_script = self.venv_dir / "Scripts" / "activate.bat"
        else:
            activate_script = self.venv_dir / "bin" / "activate"

        if not activate_script.exists():
            raise FileNotFoundError(f"Activation script not found at {activate_script}")

        # Set environment variables to activate the virtual environment
        os.environ["VIRTUAL_ENV"] = str(self.venv_dir)
        os.environ["PATH"] = str(self.venv_dir / ("Scripts" if platform.system() == "Windows" else "bin")) + os.pathsep + os.environ["PATH"]
        
        # Remove PYTHONHOME if it exists as it can interfere with the virtual environment
        if "PYTHONHOME" in os.environ:
            del os.environ["PYTHONHOME"]

        print(f"Virtual environment activated at {self.venv_dir}")

    def get_pip_path(self):
        """Get the pip path based on the operating system"""
        if platform.system() == "Windows":
            return str(self.venv_dir / "Scripts" / "pip.exe")
        return str(self.venv_dir / "bin" / "pip")

    def install_requirements(self):
        """Install all required dependencies"""
        pip_path = self.get_pip_path()
        print("Installing required packages...")
        
        # Upgrade pip first
        subprocess.run([pip_path, "install", "--upgrade", "pip"], check=True)
        
        # Install requirements

        subprocess.run([pip_path, "install", "torch", "torchvision"], check=True)
        subprocess.run([pip_path, "install", "-U", "setuptools"], check=True)
        subprocess.run([pip_path, "install", "wheel"], check=True)
        subprocess.run([pip_path, "install", "-r", str(self.requirements_file)], check=True)
        subprocess.run([pip_path, "install", "-r", str(self.requirements_demo_file)], check=True)

    def download_pretrained_models(self):
        config_name="config.yaml"
        weight_name="model.safetensors"
        repo_id="stabilityai/stable-fast-3d"

        print("Downloading pretrained models...")
        print(repo_id)

        hf_hub_download(repo_id, filename=config_name)
        hf_hub_download(repo_id, filename=weight_name)

    def install(self):
        """Run the complete installation process"""
        try:
            print("Starting SF3D installation...")
            
            # Installation steps
            self.check_python_version()
            self.activate_virtual_environment()
            self.install_requirements()
            self.download_pretrained_models()
            
        except Exception as e:
            print(f"Error during installation: {str(e)}")
            sys.exit(1)


def main():
    installer = SF3DInstaller()
    installer.install()

if __name__ == "__main__":
    main()