# FlowState - Real-Time Hand Tracking & Movement Analysis

FlowState is a comprehensive rehabilitation and movement analysis system that combines real-time hand tracking, AI-powered pose detection, sound feedback, and detailed analytics. It features both a React frontend for data visualization and a Python backend for real-time processing.

## 🚀 Quick Start

### Prerequisites

Before running FlowState, ensure you have the following installed:

- **Python 3.9+** (required for backend)
- **Node.js 18+** & npm (required for frontend)
- **Webcam** (for hand tracking)
- **Audio output** (for sound feedback)

### Installation Steps

#### 1. Clone the Repository
```bash
git clone <repository-url>
cd FlowState
```

#### 2. Set Up Python Backend
```bash
# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install Python dependencies
pip install -r requirements.txt

# Download MediaPipe hand tracking model
curl -L -o hand_landmarker.task https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task
```

#### 3. Set Up Environment Variables
```bash
# Copy the example environment file
cp .env.example .env

# Edit .env file with your API keys (optional - Gemini AI integration)
# GEMINI_API_KEY=your_api_key_here (get from Google AI Studio)
```

#### 4. Install Frontend Dependencies
```bash
npm install
```

#### 5. Run the Application

**Option A: Full Stack (Recommended)**
```bash
# Terminal 1: Start Python backend server
source .venv/bin/activate
python app_with_data.py

# Terminal 2: Start React development server
npm run dev
```

**Option B: Backend Only (Hand tracking + Analytics)**
```bash
source .venv/bin/activate
python app_with_data.py
# Open http://localhost:5001/freestyle for hand tracking interface
```

**Option C: Frontend Only (Data visualization)**
```bash
npm run dev
# Open http://localhost:5173 for React interface
```

## 🎯 How to Use

### Hand Tracking & Sound Generation
1. Navigate to http://localhost:5001/freestyle
2. Allow camera permissions when prompted
3. Show your hand to the camera
4. Make different hand poses:
   - **1 finger** → Plays E note
   - **2 fingers** → Plays D note  
   - **3 fingers** → Plays C note
5. Your movements are automatically recorded and analyzed

### Analytics Dashboard
1. Navigate to http://localhost:5173 (if running frontend)
2. View real-time analytics:
   - Movement quality metrics
   - Joint analysis
   - Session history
   - Progress tracking

## 🛠️ Technologies Used

**Backend:**
- Flask (Python web framework)
- MediaPipe (Google's hand tracking)
- PyTorch (ML pose classification)
- OpenCV (computer vision)
- SQLite (data storage)
- Pygame (audio generation)

**Frontend:**
- React + TypeScript
- Vite (build tool)
- Tailwind CSS (styling)
- shadcn/ui (UI components)
- Chart.js (data visualization)

**AI/ML:**
- Custom pose classification model
- Google Gemini AI (optional analysis)
- Movement quality algorithms

## 📊 Features

- ✅ Real-time hand landmark detection (21 points)
- ✅ AI-powered pose classification (palm, 1, 2, 3, fist)
- ✅ Sound generation based on hand poses
- ✅ Movement quality analysis (speed, smoothness, tremor)
- ✅ Joint-by-joint tracking and scoring
- ✅ Session recording and replay
- ✅ Progress tracking and analytics
- ✅ Web-based dashboard
- ✅ Export capabilities for research

## 🔧 Configuration

### Camera Settings
- Default: Uses system default camera (index 0)
- To change: Modify `cap = cv2.VideoCapture(0)` in `app_with_data.py`

### Sound Settings
- Volume and frequency can be adjusted in the pose detection section
- Disable sound by setting `SOUND_ENABLED = False`

### Database
- Default: SQLite (`flowstate.db`)
- PostgreSQL support available (see `database_postgres.py`)

## 🐛 Troubleshooting

### Common Issues

**Camera not working:**
```bash
# Check camera permissions
# Try different camera index: cv2.VideoCapture(1), cv2.VideoCapture(2), etc.
```

**Python dependencies failing:**
```bash
# Make sure you're in the virtual environment
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

**Port conflicts:**
```bash
# Kill existing processes
lsof -ti:5001 | xargs kill -9  # Backend port
lsof -ti:5173 | xargs kill -9  # Frontend port
```

**No sound output:**
```bash
# Install pygame audio dependencies
pip install pygame
# Check system audio settings
```

### Performance Tips

- **Better accuracy:** Ensure good lighting and camera positioning
- **Smoother performance:** Close unnecessary applications
- **Lower latency:** Use a dedicated USB camera instead of laptop webcam

## 📝 Development

### Running Tests
```bash
# Python backend tests
python test_pose_analytics.py
python test_shakiness_analytics.py

# Frontend tests
npm test
```

### Building for Production
```bash
# Build React frontend
npm run build

# Serve static files with Flask
# (Frontend builds to dist/ folder, served by Flask)
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 🆘 Support

If you encounter issues or have questions:

1. Check the troubleshooting section above
2. Review the terminal output for error messages
3. Ensure all dependencies are properly installed
4. Verify camera and microphone permissions

For additional support, please open an issue in the repository.
