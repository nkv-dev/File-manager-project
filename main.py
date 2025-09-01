# Simple Web File Manager - College Project
# A clean, easy-to-understand file management system

from flask import Flask, render_template, request, send_file, redirect, flash, session
import os
import uuid

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'college-project-2025'
app.permanent_session_lifetime = 86400 * 30  # 30 days

# Configuration
BASE_STORAGE = 'storage'  # Base storage directory
os.makedirs(BASE_STORAGE, exist_ok=True)

# Get user's private folder
def get_user_folder():
    if 'user_id' not in session:
        session['user_id'] = str(uuid.uuid4())[:8]  # Generate unique ID
        session.permanent = True  # Make session persistent
        print(f"🆕 New user created: {session['user_id']}")
    
    user_folder = os.path.join(BASE_STORAGE, f"user_{session['user_id']}")
    os.makedirs(user_folder, exist_ok=True)
    return user_folder

# Helper function to get file list
def get_files(current_path=''):
    user_folder = get_user_folder()
    folder_path = os.path.join(user_folder, current_path)
    files = []
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        files.append({
            'name': item,
            'is_folder': os.path.isdir(item_path),
            'size': round(os.path.getsize(item_path) / 1024, 1) if os.path.isfile(item_path) else 0
        })
    return files

# Handle favicon requests
@app.route('/favicon.ico')
def favicon():
    return '', 204

# Recover user session
@app.route('/user/<user_id>')
def recover_session(user_id):
    if len(user_id) == 8 and os.path.exists(os.path.join(BASE_STORAGE, f'user_{user_id}')):
        session['user_id'] = user_id
        session.permanent = True
        flash(f'Welcome back! Session recovered for user {user_id}')
        return redirect('/')
    else:
        flash('Invalid user ID')
        return redirect('/')

# Admin route to see all users
@app.route('/admin')
def admin():
    users = []
    if os.path.exists(BASE_STORAGE):
        for folder in os.listdir(BASE_STORAGE):
            if folder.startswith('user_'):
                user_path = os.path.join(BASE_STORAGE, folder)
                file_count = sum([len(files) for r, d, files in os.walk(user_path)])
                users.append({'id': folder, 'files': file_count})
    return f"<h2>Active Users:</h2>{'<br>'.join([f'{u["id"]}: {u["files"]} files' for u in users])}"

# Main page - show all files
@app.route('/')
@app.route('/<path:folder_path>')
def home(folder_path=''):
    files = get_files(folder_path)
    user_id = session.get('user_id', 'Not assigned')
    return render_template('index.html', files=files, current_path=folder_path, user_id=user_id)

# Upload file
@app.route('/upload', methods=['POST'])
def upload_file():
    current_path = request.form.get('current_path', '')
    if 'file' in request.files:
        file = request.files['file']
        if file.filename:
            user_folder = get_user_folder()
            upload_path = os.path.join(user_folder, current_path)
            file.save(os.path.join(upload_path, file.filename))
            flash('File uploaded successfully!')
    return redirect('/' + current_path)

# Download file
@app.route('/download/<path:filepath>')
def download_file(filepath):
    user_folder = get_user_folder()
    return send_file(os.path.join(user_folder, filepath), as_attachment=True)

# Delete file
@app.route('/delete/<path:filepath>')
def delete_file(filepath):
    user_folder = get_user_folder()
    full_path = os.path.join(user_folder, filepath)
    try:
        if os.path.isfile(full_path):
            os.remove(full_path)
        else:
            os.rmdir(full_path)
        flash('Item deleted successfully!')
    except:
        flash('Error deleting item!')
    
    # Redirect to parent folder
    parent_path = os.path.dirname(filepath)
    return redirect('/' + parent_path)

# Create folder
@app.route('/create-folder', methods=['POST'])
def create_folder():
    current_path = request.form.get('current_path', '')
    folder_name = request.form.get('folder_name')
    if folder_name:
        user_folder = get_user_folder()
        new_folder_path = os.path.join(user_folder, current_path, folder_name)
        os.makedirs(new_folder_path, exist_ok=True)
        flash('Folder created successfully!')
    return redirect('/' + current_path)

# Run the app
if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    print("🚀 Starting Web File Manager...")
    print(f"📂 Access your files at: http://localhost:{port}")
    app.run(debug=False, host='0.0.0.0', port=port)