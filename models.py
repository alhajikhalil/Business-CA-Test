from datetime import datetime


class Business:
    """Represents a local business or startup."""

    def __init__(self, name, category, description, location, contact):
        self.name = name
        self.category = category
        self.description = description
        self.location = location
        self.contact = contact
        self.timestamp = datetime.now()
        self.id = int(self.timestamp.timestamp() * 1000)

    def get_summary(self):
        """Returns a short summary string for the business."""
        return f"{self.name} ({self.category}) - {self.location}"

    def time_since_added(self):
        """Returns a human-readable string of how long ago this was added."""
        delta = datetime.now() - self.timestamp
        seconds = int(delta.total_seconds())
        if seconds < 60:
            return "just now"
        elif seconds < 3600:
            minutes = seconds // 60
            return f"{minutes} minute{'s' if minutes != 1 else ''} ago"
        elif seconds < 86400:
            hours = seconds // 3600
            return f"{hours} hour{'s' if hours != 1 else ''} ago"
        else:
            days = seconds // 86400
            return f"{days} day{'s' if days != 1 else ''} ago"

    def to_dict(self):
        """Convert business to dictionary for template rendering."""
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "location": self.location,
            "contact": self.contact,
            "timestamp": self.timestamp.strftime("%B %d, %Y at %I:%M %p"),
            "time_since": self.time_since_added(),
        }
