#!/usr/bin/env python3
"""Clone marimo examples from the marimo repo (mirrors CI behavior)."""

import os
import shutil
import subprocess


def setup_examples() -> None:
    """Clone marimo examples from the marimo repo."""
    print("🔄 Setting up examples from marimo-team/marimo...")

    # Clean up any existing examples dir (but preserve notebooks)
    if os.path.exists("examples"):
        print("  Removing existing examples/ directory...")
        shutil.rmtree("examples")

    # Clone marimo repo with sparse checkout
    print("  Cloning marimo repo (sparse checkout)...")
    clone_cmd = [
        "git",
        "clone",
        "--depth",
        "1",
        "--filter=blob:none",
        "--sparse",
        "https://github.com/marimo-team/marimo.git",
        "marimo",
    ]

    result = subprocess.run(clone_cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"❌ Failed to clone marimo repo: {result.stderr}")
        raise SystemExit(1)

    # Set sparse checkout to only get examples
    print("  Setting sparse checkout for examples/...")
    sparse_cmd = ["git", "-C", "marimo", "sparse-checkout", "set", "examples"]
    result = subprocess.run(sparse_cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"❌ Failed to set sparse checkout: {result.stderr}")
        shutil.rmtree("marimo", ignore_errors=True)
        raise SystemExit(1)

    # Move examples out of marimo dir
    print("  Moving examples to ./examples/...")
    shutil.move("marimo/examples", "examples")

    # Copy local notebooks into examples/notebooks
    if os.path.exists("notebooks"):
        print("  Copying local notebooks to examples/notebooks/...")
        shutil.copytree("notebooks", "examples/notebooks", dirs_exist_ok=True)

    # Clean up cloned repo
    shutil.rmtree("marimo", ignore_errors=True)

    print("✅ Examples setup complete!")


if __name__ == "__main__":
    setup_examples()
