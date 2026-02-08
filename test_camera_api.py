#!/usr/bin/env python3

import cv2
import time
import requests
import json

def test_camera_direct():
    print("Testing camera directly...")
    camera = cv2.VideoCapture(0)
    
    if not camera.isOpened():
        print("❌ Camera not available")
        return False
        
    # Let camera warm up
    for i in range(5):
        ret, frame = camera.read()
        if ret:
            print(f"✅ Camera frame {i+1}: {frame.shape}")
        else:
            print(f"❌ Failed to read frame {i+1}")
        time.sleep(0.1)
    
    camera.release()
    return True

def test_api_response():
    print("\nTesting API response...")
    try:
        start = time.time()
        response = requests.get('http://localhost:5001/api/current_pose', timeout=5)
        end = time.time()
        
        print(f"✅ Response status: {response.status_code}")
        print(f"⏱️  Response time: {end-start:.2f}s")
        
        if response.ok:
            data = response.json()
            print("📄 Response data:")
            print(json.dumps(data, indent=2))
        else:
            print("❌ API error response")
            
    except Exception as e:
        print(f"❌ API Error: {e}")

if __name__ == "__main__":
    test_camera_direct()
    test_api_response()