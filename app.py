from flask import Flask, render_template, request, redirect, url_for, flash
from models import Business, BusinessDirectory
from datetime import datetime

app = Flask(__name__)
app.secret_key = "csc202_secret_key_2025"

# Global directory instance (acts as our in-memory database)
directory = BusinessDirectory()


# Pre-populate with some sample businesses
sample_businesses = [
    Business("Mama Titi's Kitchen", "Food & Beverage", "Authentic home-cooked Nigerian meals. Catering and takeaway available.", "Bodija, Ibadan", "0801-234-5678"),
    Business("CodeCraft Academy", "Education & Tech", "Coding bootcamp for beginners and intermediate learners. Python, Web Dev, and Data Science.", "Ring Road, Ibadan", "0902-345-6789"),
    Business("GreenLeaf Farms", "Agriculture", "Fresh organic vegetables delivered to your door. Weekly subscription boxes available.", "Akobo, Ibadan", "0703-456-7890"),
    Business("SwiftRide Logistics", "Transport & Delivery", "Same-day parcel delivery across Ibadan and environs. Reliable and affordable.", "Dugbe, Ibadan", "0812-567-8901"),
    Business("Sparkle Laundry Hub", "Services", "Professional laundry and dry cleaning with 24-hour turnaround.", "UI Gate, Ibadan", "0906-678-9012"),
]

for biz in sample_businesses:
    directory.add_business(biz)

@app.route("/")
def home():
    """Home page showing all businesses and recently added."""
    category_filter = request.args.get("category", "")
    if category_filter:
        businesses = directory.filter_by_category(category_filter)
    else:
        businesses = directory.get_all()

    recently_added = directory.get_recently_added(3)
    categories = directory.get_categories()
    can_undo = directory.can_undo()

    return render_template(
        "index.html",
        businesses=[b.to_dict() for b in businesses],
        recently_added=[b.to_dict() for b in recently_added],
        categories=categories,
        selected_category=category_filter,
        total_count=directory.count(),
        can_undo=can_undo,
        now=datetime.now().strftime("%B %d, %Y"),
    )
