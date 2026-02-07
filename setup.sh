#!/bin/bash

# FlowState Setup Script
# Installs all dependencies and sets up PostgreSQL with pgvector

set -e  # Exit on error

echo "════════════════════════════════════════════════════════════"
echo "  FlowState Setup - Hand Rehabilitation Tracking System"
echo "════════════════════════════════════════════════════════════"
echo ""

# Check if running on macOS
if [[ "$OSTYPE" != "darwin"* ]]; then
    echo "⚠️  This script is designed for macOS"
    echo "   For other systems, install dependencies manually"
    exit 1
fi

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check Homebrew
echo "1. Checking Homebrew..."
if ! command_exists brew; then
    echo "❌ Homebrew not found. Installing..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
else
    echo "✓ Homebrew installed"
fi

# Check Python
echo ""
echo "2. Checking Python..."
if ! command_exists python3; then
    echo "❌ Python 3 not found. Installing..."
    brew install python@3.9
else
    PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
    echo "✓ Python $PYTHON_VERSION installed"
fi

# Create virtual environment
echo ""
echo "3. Setting up virtual environment..."
if [ ! -d ".venv" ]; then
    python3 -m venv .venv
    echo "✓ Virtual environment created"
else
    echo "✓ Virtual environment already exists"
fi

# Activate virtual environment
source .venv/bin/activate

# Install Python dependencies
echo ""
echo "4. Installing Python packages..."
pip install --upgrade pip

# Core dependencies
echo "   Installing core packages..."
pip install flask opencv-python mediapipe numpy

# ML dependencies
echo "   Installing ML packages..."
pip install scikit-learn scipy pandas

# Database dependencies
echo "   Installing database packages..."
pip install psycopg2-binary

echo "✓ Python packages installed"

# Install PostgreSQL
echo ""
echo "5. Setting up PostgreSQL..."
if ! command_exists psql; then
    echo "   Installing PostgreSQL..."
    brew install postgresql@15
    brew services start postgresql@15
    echo "✓ PostgreSQL installed and started"
else
    echo "✓ PostgreSQL already installed"
    # Check if running
    if ! pgrep -x "postgres" > /dev/null; then
        echo "   Starting PostgreSQL..."
        brew services start postgresql
    fi
fi

# Install pgvector
echo ""
echo "6. Setting up pgvector..."
if ! brew list pgvector &>/dev/null; then
    echo "   Installing pgvector..."
    brew install pgvector
    echo "✓ pgvector installed"
else
    echo "✓ pgvector already installed"
fi

# Create database
echo ""
echo "7. Creating FlowState database..."
if psql -lqt | cut -d \| -f 1 | grep -qw flowstate; then
    echo "✓ Database 'flowstate' already exists"
else
    createdb flowstate
    echo "✓ Database 'flowstate' created"
fi

# Enable pgvector extension
echo ""
echo "8. Enabling pgvector extension..."
psql -d flowstate -c "CREATE EXTENSION IF NOT EXISTS vector;" 2>/dev/null || echo "⚠️  pgvector extension setup - will be enabled on first use"

# Download MediaPipe model if not present
echo ""
echo "9. Downloading MediaPipe model..."
if [ ! -f "FlowState/hand_landmarker.task" ]; then
    cd FlowState
    curl -L -o hand_landmarker.task \
        https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task
    cd ..
    echo "✓ MediaPipe model downloaded"
else
    echo "✓ MediaPipe model already exists"
fi

# Test imports
echo ""
echo "10. Testing installation..."
python3 -c "
import cv2
import mediapipe as mp
import flask
import sklearn
import psycopg2
print('✓ All Python packages working')
" || echo "⚠️  Some imports failed - check error above"

# Summary
echo ""
echo "════════════════════════════════════════════════════════════"
echo "  Setup Complete!"
echo "════════════════════════════════════════════════════════════"
echo ""
echo "Quick Start Commands:"
echo ""
echo "  # Activate virtual environment"
echo "  source .venv/bin/activate"
echo ""
echo "  # Run web app (SQLite)"
echo "  python FlowState/app_with_data.py"
echo ""
echo "  # Setup PostgreSQL database"
echo "  python FlowState/database_postgres.py"
echo ""
echo "  # Train ML models (after collecting data)"
echo "  python FlowState/train_models.py"
echo ""
echo "  # Setup pgvector similarity search"
echo "  python FlowState/pgvector_integration.py create"
echo ""
echo "Documentation:"
echo "  • README.md - Main documentation"
echo "  • ML_TRAINING_GUIDE.md - ML training guide"
echo "  • PGVECTOR_GUIDE.md - Vector search guide"
echo ""
echo "Web Interface: http://localhost:5001"
echo ""
