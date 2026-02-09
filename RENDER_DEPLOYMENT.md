# Render Deployment Instructions

## Environment Variables

To deploy this app to Render, you need to set the following environment variable in your Render dashboard:

### Required Environment Variable

```
DISABLE_AUDIO=1
```

This disables pygame audio initialization on the server since Render doesn't have audio devices.

## How to Set Environment Variables in Render

1. Go to your Render dashboard
2. Select your web service
3. Navigate to the **Environment** tab
4. Click **Add Environment Variable**
5. Add:
   - **Key**: `DISABLE_AUDIO`
   - **Value**: `1`
6. Click **Save Changes**

Your service will automatically redeploy with audio disabled.

## Optional: Gemini API Key

If you're using the AI feedback feature, also set:

```
GEMINI_API_KEY=your_actual_gemini_api_key_here
```

## Port Configuration

The app is already configured to use Render's `PORT` environment variable automatically. No additional configuration needed.

## Service Type

Make sure your Render service is configured as a **Web Service**, not a Background Worker, since this is a Flask web application.

## Troubleshooting

If you still see errors:
- Verify `DISABLE_AUDIO=1` is set
- Check that your service is binding to port (should see Flask startup messages in logs)
- Ensure all dependencies in `requirements.txt` are installed correctly
