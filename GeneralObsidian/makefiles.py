import os
from datetime import date, timedelta

def create_diary_entries(folder):
    # Ensure the folder exists
    os.makedirs(folder, exist_ok=True)
    
    start_date = date.today()
    end_date = start_date + timedelta(days=365)  # For 1 year

    current_date = start_date
    while current_date <= end_date:
        # Use year-month-day order for proper lexicographical sorting
        filename = f"entry-{current_date.strftime('%Y-%m-%d')}.md"
        filepath = os.path.join(folder, filename)
        # Create the file with empty content (or add default content if desired)
        with open(filepath, "w", encoding="utf-8") as file:
            file.write("")  
        current_date += timedelta(days=1)

if __name__ == "__main__":
    # Replace with your desired folder path for your diary entries
    diary_folder = "./Life"
    create_diary_entries(diary_folder)

