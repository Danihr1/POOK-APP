import customtkinter as ctk
from PIL import Image, ImageTk
import json
import os

class LanguageGate(ctk.CTkFrame):
    def __init__(self, parent, gate_name, flag, language_code, chatbot):
        super().__init__(parent)
        self.gate_name = gate_name
        self.flag = flag
        self.language_code = language_code
        self.chatbot = chatbot
        
        self.create_gate_ui()
        self.load_lessons()
    
    def create_gate_ui(self):
        # Gate header
        header_frame = ctk.CTkFrame(self)
        header_frame.pack(fill="x", padx=10, pady=5)
        
        gate_label = ctk.CTkLabel(
            header_frame,
            text=f"{self.flag} {self.gate_name}",
            font=("Helvetica", 16, "bold")
        )
        gate_label.pack(side="left")
        
        # Progress indicator
        self.progress_label = ctk.CTkLabel(
            header_frame,
            text="Level: 0",
            font=("Helvetica", 12)
        )
        self.progress_label.pack(side="right")
        
        # Lessons container
        self.lessons_frame = ctk.CTkFrame(self)
        self.lessons_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        # Enter gate button
        enter_button = ctk.CTkButton(
            self,
            text="Enter Gate",
            command=self.enter_gate
        )
        enter_button.pack(fill="x", padx=10, pady=5)
    
    def load_lessons(self):
        # Load lessons from JSON file
        lessons_file = f"lessons_{self.language_code}.json"
        if os.path.exists(lessons_file):
            with open(lessons_file, 'r') as f:
                self.lessons = json.load(f)
        else:
            # Default lessons structure
            self.lessons = {
                "beginner": [
                    {"id": "b1", "title": "Basic Greetings", "type": "vocabulary"},
                    {"id": "b2", "title": "Numbers 1-10", "type": "vocabulary"},
                    {"id": "b3", "title": "Common Phrases", "type": "conversation"}
                ],
                "intermediate": [
                    {"id": "i1", "title": "Past Tense", "type": "grammar"},
                    {"id": "i2", "title": "Daily Routines", "type": "vocabulary"},
                    {"id": "i3", "title": "Shopping", "type": "conversation"}
                ],
                "advanced": [
                    {"id": "a1", "title": "Idioms", "type": "vocabulary"},
                    {"id": "a2", "title": "Complex Grammar", "type": "grammar"},
                    {"id": "a3", "title": "Business Language", "type": "conversation"}
                ]
            }
            # Save default lessons
            with open(lessons_file, 'w') as f:
                json.dump(self.lessons, f)
    
    def enter_gate(self):
        # Create new window for the language gate
        gate_window = ctk.CTkToplevel()
        gate_window.title(f"{self.gate_name} - Learning Center")
        gate_window.geometry("800x600")
        
        # Create tabs for different levels
        tabview = ctk.CTkTabview(gate_window)
        tabview.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Add tabs for each level
        for level in ["beginner", "intermediate", "advanced"]:
            tab = tabview.add(level.capitalize())
            self.create_lesson_list(tab, level)
    
    def create_lesson_list(self, parent, level):
        for lesson in self.lessons[level]:
            lesson_frame = ctk.CTkFrame(parent)
            lesson_frame.pack(fill="x", padx=5, pady=2)
            
            lesson_label = ctk.CTkLabel(
                lesson_frame,
                text=f"{lesson['title']} ({lesson['type']})",
                font=("Helvetica", 12)
            )
            lesson_label.pack(side="left", padx=10)
            
            start_button = ctk.CTkButton(
                lesson_frame,
                text="Start Lesson",
                command=lambda l=lesson: self.start_lesson(l)
            )
            start_button.pack(side="right", padx=10)
    
    def start_lesson(self, lesson):
        # Create lesson window
        lesson_window = ctk.CTkToplevel()
        lesson_window.title(f"Lesson: {lesson['title']}")
        lesson_window.geometry("600x400")
        
        # Add lesson content based on type
        if lesson['type'] == "vocabulary":
            self.create_vocabulary_lesson(lesson_window, lesson)
        elif lesson['type'] == "grammar":
            self.create_grammar_lesson(lesson_window, lesson)
        elif lesson['type'] == "conversation":
            self.create_conversation_lesson(lesson_window, lesson)
    
    def create_vocabulary_lesson(self, window, lesson):
        # Add vocabulary learning interface
        content_frame = ctk.CTkFrame(window)
        content_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Add lesson content here
        # This is a placeholder - you would need to implement the actual lesson content
        label = ctk.CTkLabel(
            content_frame,
            text="Vocabulary Lesson Content",
            font=("Helvetica", 16)
        )
        label.pack(pady=20)
    
    def create_grammar_lesson(self, window, lesson):
        # Add grammar learning interface
        content_frame = ctk.CTkFrame(window)
        content_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Add lesson content here
        label = ctk.CTkLabel(
            content_frame,
            text="Grammar Lesson Content",
            font=("Helvetica", 16)
        )
        label.pack(pady=20)
    
    def create_conversation_lesson(self, window, lesson):
        # Add conversation practice interface
        content_frame = ctk.CTkFrame(window)
        content_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Add lesson content here
        label = ctk.CTkLabel(
            content_frame,
            text="Conversation Practice Content",
            font=("Helvetica", 16)
        )
        label.pack(pady=20) 