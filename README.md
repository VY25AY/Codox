# Codox - Intelligent IDE

## Overview
Codox is a lightweight, AI-assisted code editor designed to empower developers with real-time multi-user collaboration and advanced AI-driven features. Built with a secure and intuitive workspace, Codox not only supports live code editing and file management but also enhances productivity with AI-powered linting, auto-completion, documentation generation, and syntax correction.

## Problem Statement
Modern software development demands rapid collaboration and high-quality code. Developers need tools that:
- **Enable real-time editing**: Multiple users can work simultaneously without conflicts.
- **Provide intelligent code suggestions and error corrections**: Minimize bugs and speed up coding.
- **Ensure organized workspace management**: Support both private and public workspaces with clear file/folder hierarchies.
- **Automatically synchronize code, files, and user interactions**: Eliminate manual saving and reduce merge conflicts.

Codox meets these needs by integrating advanced AI capabilities with robust real-time collaboration, empowering teams to write, review, and maintain high-quality code efficiently.

## Demo

![1](https://github.com/user-attachments/assets/1e8c2362-98da-4bf7-9dd4-34cce0c42913)
![2](https://github.com/user-attachments/assets/a5218704-3b79-49c5-90f5-b0b94befb796)
![3](https://github.com/user-attachments/assets/88841604-6297-41b0-a1dc-2c246b9adb75)
![4](https://github.com/user-attachments/assets/dfec646e-33f4-426d-bb96-9068539cee53)

## Solution Architecture
### Core Infrastructure
#### Authentication & Database
**Firebase Authentication & Realtime Database:**
- **Sign-Up/Login**: Users can register using Google or email with OTP verification.
- **Password Management**: Secure options for password reset and change.
- **Realtime Sync**: All code, files, and collaboration events are synchronized instantly using Firebase's Realtime Database and snapshot listeners.

#### AI Integration
**Google Gemini API:**
- **AI-Powered Suggestions**: Offers smart code completions and linting.
- **Auto-Documentation**: Automatically generates documentation comments.
- **Code Correction**: Detects syntax errors and suggests fixes.

**AI Chatbot:**
- Allows users to ask coding-related questions and receive interactive assistance.

### Code Editor & UI
**Monaco Editor:**
- Supports multiple programming languages with customizable themes and syntax highlighting.
- File Management: Users can create, rename, delete, and drag-and-drop reorder files and folders in real-time.

**Collaborative Features:**
- **Live Cursor Tracking**: Displays each collaborator's cursor and avatar.
- **Chat Integration**: Provides in-workspace chat for real-time communication.
- **Workspace Invitations**: Users can invite others to join public workspaces.

## Tech Stack
| Component       | Technology                        |
|---------------|---------------------------------|
| Frontend      | Next.js 15, Shadcn UI, Tailwind CSS |
| Code Editor   | Monaco Editor                    |
| Realtime Backend | Firebase Realtime Database & Firestore |
| AI Services   | Google Gemini API                |
| Authentication | Firebase Authentication (Google & Email/OTP) |
| Language      | JavaScript                        |

## Implementation Details
### Authentication & User Management
- **Google OAuth & Email/OTP**: Users can register via Google or email with OTP verification.
- **Password Management**: Supports password reset and updates.

### Real-Time Collaboration
- **Live Synchronization**: Firebase Realtime Database syncs all changes instantly.
- **Collaborative Workspace**: Invitations, notifications, and live updates for all changes.
- **Autosave Feature**: All edits are automatically saved to Firebase.

### Code Editor Features
- **Monaco Editor Integration**: Multi-language support, syntax highlighting, and customizable UI.
- **File Navigation Panel**: Recursive rendering for nested directories, real-time updates.

### AI-Driven Enhancements
- **Code Suggestions & Linting**: Smart completions and error detection.
- **Auto-Documentation & Code Correction**: AI-generated documentation and real-time syntax fixes.
- **AI Chatbot**: Embedded chatbot for coding assistance and brainstorming.

## Setting up the Project
### Clone the GitHub Repository
```bash
git clone https://github.com/VY25AY/Codox.git
```

### Open the Project Directory
```bash
cd Codox
```


 
