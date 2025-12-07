#!/bin/bash

# AI Revenue Sharing Platform - Quick Setup Script
# This script sets up the development environment

echo "🚀 Setting up AI Revenue Sharing Platform..."
echo ""

# Check Python version
echo "📋 Checking Python version..."
python_version=$(python3 --version 2>&1 | awk '{print $2}')
required_version="3.9.0"

if [ "$(printf '%s\n' "$required_version" "$python_version" | sort -V | head -n1)" != "$required_version" ]; then 
    echo "❌ Error: Python 3.9 or higher is required"
    echo "   Current version: $python_version"
    echo "   Please install Python 3.9+ from https://www.python.org/downloads/"
    exit 1
fi
echo "✅ Python $python_version detected"
echo ""

# Create virtual environment
echo "📦 Creating virtual environment..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "✅ Virtual environment created"
else
    echo "ℹ️  Virtual environment already exists"
fi
echo ""

# Activate virtual environment
echo "🔌 Activating virtual environment..."
source venv/bin/activate || . venv/Scripts/activate
echo "✅ Virtual environment activated"
echo ""

# Upgrade pip
echo "⬆️  Upgrading pip..."
pip install --upgrade pip > /dev/null 2>&1
echo "✅ pip upgraded"
echo ""

# Install dependencies
echo "📚 Installing dependencies..."
pip install -r requirements.txt
if [ $? -eq 0 ]; then
    echo "✅ All dependencies installed successfully"
else
    echo "❌ Error installing dependencies"
    exit 1
fi
echo ""

# Create .env file if it doesn't exist
if [ ! -f ".env" ]; then
    echo "📝 Creating .env file..."
    cp .env.example .env
    echo "✅ .env file created"
    echo "⚠️  IMPORTANT: Edit .env and add your ANTHROPIC_API_KEY"
    echo ""
else
    echo "ℹ️  .env file already exists"
    echo ""
fi

# Create necessary directories
echo "📁 Creating project directories..."
mkdir -p assets utils config docs
echo "✅ Directories created"
echo ""

# Check if Streamlit is installed
if command -v streamlit &> /dev/null; then
    echo "✅ Streamlit is installed"
    streamlit_version=$(streamlit version | head -n 1)
    echo "   Version: $streamlit_version"
else
    echo "❌ Streamlit installation failed"
    exit 1
fi
echo ""

# Success message
echo "🎉 Setup completed successfully!"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📖 Next Steps:"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "1. Edit .env file and add your ANTHROPIC_API_KEY:"
echo "   nano .env"
echo ""
echo "2. Run the application:"
echo "   streamlit run app.py"
echo ""
echo "3. Open your browser at:"
echo "   http://localhost:8501"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📚 Documentation:"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "README.md         - Full documentation"
echo "DEPLOYMENT.md     - Deployment guide"
echo "INVESTOR_PITCH.md - Investment overview"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🆘 Need Help?"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📧 Email: support@airevshare.com"
echo "💬 Discord: discord.gg/airevshare"
echo "📚 Docs: docs.airevshare.com"
echo ""
echo "🚀 Happy building!"