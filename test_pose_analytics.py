#!/usr/bin/env python3
"""
Test script to check if pose statistics are being returned by the analytics API
"""

import requests
import json

def test_analytics_with_poses():
    """Fetch analytics and display pose statistics"""
    
    print("=" * 60)
    print("🧪 Testing Pose Detection in Analytics")
    print("=" * 60)
    print()
    
    # Call analytics API
    url = "http://localhost:5001/api/user/default_user/analytics"
    
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            
            print("✅ Analytics API Response Received")
            print()
            
            # Check for pose statistics
            if 'poseStatistics' in data:
                pose_stats = data['poseStatistics']
                
                if pose_stats:
                    print("📊 POSE STATISTICS FROM MOST RECENT SESSION:")
                    print("-" * 60)
                    print()
                    
                    # Sort by count (most common first)
                    sorted_poses = sorted(pose_stats.items(), 
                                         key=lambda x: x[1]['count'], 
                                         reverse=True)
                    
                    # Emoji mapping
                    pose_emojis = {
                        'palm': '🖐️',
                        '1': '☝️',
                        '2': '✌️',
                        '3': '🤟',
                        'fist': '✊'
                    }
                    
                    total_detections = sum(stats['count'] for _, stats in sorted_poses)
                    
                    for pose_name, stats in sorted_poses:
                        emoji = pose_emojis.get(pose_name, '👋')
                        count = stats['count']
                        confidence = stats['averageConfidence']
                        percentage = stats['percentage']
                        
                        # Create bar chart
                        bar_length = int(percentage / 2)  # Scale to 50 chars max
                        bar = '█' * bar_length
                        
                        print(f"{emoji} {pose_name.upper():8s} │ {count:3d} times │ {percentage:5.1f}% │ Conf: {confidence:.2f}")
                        print(f"           │ {bar}")
                        print()
                    
                    print("-" * 60)
                    print(f"Total pose detections: {total_detections}")
                    print()
                    
                    # Show interpretation
                    print("💡 INTERPRETATION:")
                    if total_detections > 20:
                        print("✅ Good session! Multiple poses detected with variety")
                    elif total_detections > 10:
                        print("⚠️  Moderate session - try holding poses longer")
                    else:
                        print("❌ Low detection - make sure poses are clear and confident")
                    
                else:
                    print("⚠️  No poses detected in most recent session")
                    print("   Make sure to:")
                    print("   1. Show your hand to the camera")
                    print("   2. Make clear poses (palm, 1, 2, 3, fist)")
                    print("   3. Hold each pose for 1-2 seconds")
            else:
                print("⚠️  'poseStatistics' not found in API response")
                print("   This might be an old session recorded before pose detection")
            
            print()
            print("-" * 60)
            print()
            
            # Show overall scores
            if 'overallScores' in data:
                print("📈 OVERALL MOVEMENT SCORES:")
                scores = data['overallScores']
                print(f"  Smoothness:  {scores.get('smoothness', 0)}/100")
                print(f"  ROM:         {scores.get('rom', 0)}/100")
                print(f"  Trajectory:  {scores.get('trajectory', 0)}/100")
                print(f"  Consistency: {scores.get('consistency', 0)}/100")
            
            print()
            
        elif response.status_code == 404:
            print("❌ No sessions found for default_user")
            print()
            print("📹 To record a session:")
            print("   1. Open http://localhost:5001 in browser")
            print("   2. Show your hand to the camera")
            print("   3. Make different poses (palm, 1, 2, 3, fist)")
            print("   4. Wait for auto-stop or move hand away")
            print("   5. Run this script again")
        else:
            print(f"❌ Error: HTTP {response.status_code}")
            print(response.text)
    
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to Flask server")
        print()
        print("Make sure the server is running:")
        print("  cd FlowState/")
        print("  python3 app_with_data.py")
    
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
    
    print()
    print("=" * 60)

if __name__ == "__main__":
    test_analytics_with_poses()
