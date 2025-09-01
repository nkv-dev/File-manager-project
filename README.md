# 🚀 Simple Web File Manager - College Project

A clean, secure web-based file management system built with Python Flask featuring **private user sessions** and **folder navigation**.

## ⭐ Key Features

### 📁 **File Management**
- ✅ **Upload Files** - Upload any file type securely
- ✅ **Download Files** - One-click file downloads
- ✅ **Delete Files/Folders** - Safe removal with confirmation
- ✅ **Create Folders** - Organize files in nested directories
- ✅ **Folder Navigation** - Browse through folder hierarchy

### 🔒 **Privacy & Security**
- ✅ **Private User Sessions** - Each user gets isolated storage
- ✅ **Session-Based Folders** - Files separated by unique user IDs
- ✅ **Security Disclaimer** - Warns against sensitive file uploads
- ✅ **Safe File Handling** - Secure file operations

### 🎨 **User Interface**
- ✅ **Clean Design** - Modern, intuitive interface
- ✅ **Responsive Layout** - Works on mobile and desktop
- ✅ **Feature Sidebar** - Showcases project capabilities
- ✅ **User ID Display** - Shows current session identifier
- ✅ **Breadcrumb Navigation** - Easy folder navigation

## 🛠️ Technologies Used

- **Backend**: Python Flask, UUID for sessions
- **Frontend**: HTML5, CSS3, JavaScript
- **File Handling**: Python OS module, secure file operations
- **Styling**: Pure CSS (no external frameworks)
- **Session Management**: Flask sessions

## 📁 Project Structure

```
web-file-manager/
├── main.py              # Main Flask application
├── templates/
│   └── index.html       # Frontend template with sidebar
├── storage/             # Base storage directory
│   ├── user_a1b2c3d4/   # User 1's private files
│   └── user_e5f6g7h8/   # User 2's private files
├── requirements.txt     # Python dependencies
├── Procfile            # Deployment configuration
└── README.md           # This documentation
```

## 🚀 Quick Start

### **Local Development**

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd web-file-manager
   ```

2. **Install Python** (3.7 or higher)

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   python main.py
   ```

5. **Open your browser**:
   ```
   http://localhost:5000
   ```

### **Production Deployment**

#### **Render (Recommended)**
1. Push code to GitHub
2. Connect GitHub to Render
3. Create Web Service
4. Build Command: `pip install -r requirements.txt`
5. Start Command: `python main.py`

#### **Railway**
1. Push to GitHub
2. Connect Railway to your repo
3. Deploy automatically

#### **PythonAnywhere**
1. Upload files to their platform
2. Create Flask web app
3. Point to main.py

## 🔧 Configuration

### **Environment Variables**
- `PORT` - Server port (default: 5000)
- `FLASK_ENV` - Environment (development/production)

### **Customization Options**
```python
# In main.py
app.secret_key = 'your-secret-key'  # Change for production
BASE_STORAGE = 'storage'            # Base storage directory
```

## 🎯 How It Works

### **Session Management**
1. **First Visit** - System generates unique 8-character user ID
2. **Private Folder** - Creates `storage/user_[ID]/` directory
3. **Session Persistence** - ID stored in browser session
4. **File Isolation** - All operations confined to user's folder

### **File Operations**
- **Upload** - Files saved to user's current directory
- **Download** - Secure file serving with proper headers
- **Delete** - Safe removal with error handling
- **Navigation** - Breadcrumb-based folder browsing

### **Security Features**
- **Path Validation** - Prevents directory traversal attacks
- **File Sanitization** - Secure filename handling
- **User Isolation** - Complete separation of user data
- **Disclaimer** - Warns against sensitive file uploads

## ⚠️ Known Limitations

### **Current Issues**
- **Session Storage** - Files lost when browser session ends
- **No Authentication** - Anyone can access with session ID
- **File Size Limits** - No upload size restrictions implemented
- **No File Validation** - Accepts any file type
- **Memory Usage** - Large files may cause issues

### **Not Suitable For**
- Production file storage
- Sensitive document management
- Multi-user persistent storage
- Large file uploads (>100MB)

## 🔒 Security Considerations

### **⚠️ Important Warnings**
- **Demo Purpose Only** - Not for production use
- **No Encryption** - Files stored in plain text
- **Session-Based** - Data not permanently stored
- **No Access Control** - Basic session isolation only

### **Safe Usage**
- Use only test files
- Avoid personal documents
- Don't upload sensitive data
- Treat as temporary storage

## 🎓 Educational Value

### **Learning Objectives**
- **Web Development** - Full-stack Flask application
- **File Handling** - Python file operations
- **Session Management** - User state management
- **Frontend Design** - Responsive web interfaces
- **Security Awareness** - Basic web security concepts

### **Perfect For**
- College web development projects
- Python programming assignments
- Full-stack development learning
- Portfolio demonstrations
- Understanding file systems

## 🔧 Advanced Customization

### **Add User Authentication**
```python
# Replace session-based with login system
from flask_login import LoginManager, login_required
```

### **Add File Validation**
```python
# Restrict file types
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
```

### **Add Database Storage**
```python
# Store file metadata in database
from flask_sqlalchemy import SQLAlchemy
```

### **Add File Preview**
```javascript
// Add image/text preview functionality
function previewFile(filename) { ... }
```

## 📊 Performance Notes

- **Lightweight** - Minimal dependencies
- **Fast** - Direct file system operations
- **Scalable** - Session-based user separation
- **Memory Efficient** - No database overhead

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Built for educational purposes
- Inspired by modern file management systems
- Designed for college-level learning

---

**⚠️ Disclaimer: This is a demo application. Do not use for sensitive data or production environments.**

**Made with ❤️ for learning and educational purposes**