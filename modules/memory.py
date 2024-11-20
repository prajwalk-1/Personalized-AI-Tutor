import os
import json

class UserMemory:
    def __init__(self, memory_file="user_memory.json"):
        self.memory_file = memory_file
        if not os.path.exists(memory_file):
            with open(memory_file, 'w') as f:
                json.dump({}, f)

    def load_memory(self, user_id):
        """Load user progress from memory."""
        with open(self.memory_file, 'r') as f:
            memory = json.load(f)
        return memory.get(user_id, {})

    def update_memory(self, user_id, progress):
        """Update user progress in memory."""
        with open(self.memory_file, 'r') as f:
            memory = json.load(f)
        memory[user_id] = progress
        with open(self.memory_file, 'w') as f:
            json.dump(memory, f)
