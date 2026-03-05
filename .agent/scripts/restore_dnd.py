import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

dnd_func = """
    function isDndActive() {
      if (!state.settings.dndEnabled) return false;

      const now = new Date();
      const currentTime = now.getHours() * 60 + now.getMinutes();

      const [startH, startM] = state.settings.dndStart.split(':').map(Number);
      const [endH, endM] = state.settings.dndEnd.split(':').map(Number);

      const startTime = startH * 60 + startM;
      const endTime = endH * 60 + endM;

      if (startTime > endTime) {
        // Overnight (e.g., 22:00 - 07:00)
        return currentTime >= startTime || currentTime < endTime;
      } else {
        return currentTime >= startTime && currentTime < endTime;
      }
    }
"""

# Check if it's already there (though we just found out it isn't)
if 'function isDndActive()' not in content:
    content = content.replace('    // ========================================\n    // EXPORT', dnd_func + '\n    // ========================================\n    // EXPORT')
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
